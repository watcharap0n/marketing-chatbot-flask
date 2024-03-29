import pandas as pd
from typing import Any, Optional
from datetime import datetime
import numpy as np
from bson import ObjectId
from config.object_str import CutId


def f(x):
    if (x > 4) and (x <= 8):
        return 'Early Morning'
    elif (x > 8) and (x <= 12):
        return 'Morning'
    elif (x > 12) and (x <= 16):
        return 'Noon'
    elif (x > 16) and (x <= 20):
        return 'Eve'
    elif (x > 20) and (x <= 24):
        return 'Night'
    elif (x <= 4):
        return 'Late Night'


class DataColumnFilter:
    """
    Example

    start = '2021-06-06'
    end = '2021-06-07'

    sorting = DataColumnFilter(collection=collection, after_start_date=start, before_end_date=end)
    df = sorting.createDataFrame()

    """

    def __init__(
            self, database: Any,
            collection: str,
            after_start_date: Optional[str] = None,
            before_end_date: Optional[str] = None,
            channel: Optional[str] = None,
            product: Optional[str] = None,
            tag: Optional[list] = None,
            id: Optional[list] = None,
            path_excel: Any = None
    ):
        self.database = database
        self.collection = collection
        self.after_start_date = after_start_date
        self.before_end_date = before_end_date
        self.channel = channel
        self.product = product
        self.tag = tag
        self.id = id
        self.path_excel = path_excel

    @staticmethod
    def location_data(dataframe, key, value, result):
        dataframe[key].loc[dataframe[key] == value] = result

    def filter_data(self, dataframe):
        self.location_data(dataframe=dataframe, key='channel', value='contact', result='Contact')
        self.location_data(dataframe=dataframe, key='product', value='Mango ERP (Construction)', result='Construction')
        self.location_data(dataframe=dataframe, key='product', value='Mango ERP (Real Estate)', result='RealEstate')
        self.location_data(dataframe=dataframe, key='product', value='Pusit (Consulting)', result='Consulting')

    def filter(self):
        data = self.database.find(self.collection, {})
        data = list(data)
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'])
        self.filter_data(df)
        df1 = df.reset_index()[['date']]
        df1['year'] = [df1.iloc[i, 0].year for i in range(len(df1))]
        df1['month'] = [df1.iloc[i, 0].month for i in range(len(df1))]
        df1['day'] = [df1.iloc[i, 0].day for i in range(len(df1))]
        df1['english_day'] = df1.date.dt.strftime('%a')
        df1 = df1.drop(['date'], axis=1)
        df1 = df1.astype({
            'month': 'category',
            'day': 'category',
            'english_day': 'category'
        })
        df1 = df1.replace(np.nan, '')
        dfs = df.merge(df1, left_index=True, right_index=True)
        dfs = dfs.sort_values(by='date')
        dfs = dfs.reset_index()
        dfs.drop(['index'], axis=1)
        return dfs

    def filter_datetime_time_of_day(self):
        data = self.database.find(self.collection, {})
        data = list(data)
        df = pd.DataFrame(data)
        df = df.drop(['collection', 'year', 'month', 'english_day', 'day', 'index'], axis=1)
        df = df.replace(np.nan, '', regex=True)
        events = df.loc[df['channel'] == 'event Impact']
        df.drop(events.index, inplace=True)
        df = df.reset_index()[['channel', 'product', 'date', 'time']]
        dfs = df.reset_index()[['date', 'time']]
        dfs['date'] = pd.to_datetime(dfs['date'])
        dfs['time'] = pd.to_datetime(dfs['time'], format='%H:%M:%S')
        dfs['time'] = dfs['time'].dt.tz_localize('UTC').dt.tz_convert('Asia/Bangkok')
        dfs['date'] = dfs['date'].dt.tz_localize('UTC').dt.tz_convert('Asia/Bangkok')
        dfs['year'] = [dfs.iloc[i, 0].year for i in range(len(dfs))]
        dfs['month'] = [dfs.iloc[i, 0].month for i in range(len(dfs))]
        dfs['day'] = [dfs.iloc[i, 0].day for i in range(len(dfs))]
        dfs['english_day'] = dfs.date.dt.strftime('%a')
        dfs['hour'] = [dfs.iloc[i, 1].hour for i in range(len(dfs))]
        dfs['min'] = [dfs.iloc[i, 1].minute for i in range(len(dfs))]
        dfs['sec'] = [dfs.iloc[i, 1].second for i in range(len(dfs))]
        dfs['time_of_day'] = dfs['hour'].apply(f)
        x = dfs.merge(df[['channel', 'product']], left_index=True, right_index=True)
        x = x.astype({
            'month': 'category',
            'day': 'category',
            'english_day': 'category',
            'hour': 'category',
            'min': 'category',
            'sec': 'category',
            'time_of_day': 'category',
        })
        return x

    @staticmethod
    def filter_of_chart(df, condition=False, of_months_products=False,
                        of_monthly=False, year=None, month=None,
                        channel=None, product=None):
        if condition:
            if of_months_products:
                new = df.groupby(['channel', 'month', 'year', 'product']).size()
                count = new.reset_index()
                count = count.rename(columns={0: 'count'})
                year = count['year'] == year
                channel = count['channel'] == channel
                product = count['product'] == product
                ym2 = year & channel & product
                return count.loc[ym2]
            elif of_monthly:
                new = df.groupby(['channel', 'month', 'year']).size()
                count = new.reset_index()
                count = count.rename(columns={0: 'count'})
                channel = count['channel'] == channel
                year = count['year'] == year
                ym2 = year & channel
                return count.loc[ym2]
            else:
                new = df.groupby(['channel', 'month', 'year', 'day']).size()
                count = new.reset_index()
                count = count.rename(columns={0: 'count'})
                year = count['year'] == year
                month = count['month'] == month
                channel = count['channel'] == channel
                ym2 = year & month & channel
                return count.loc[ym2]
        new = df.groupby(['channel']).size()
        count = new.reset_index()
        count = count.rename(columns={0: 'count'})
        return count

    @staticmethod
    def duplicated_email_tel(df):
        df = df.replace(np.nan, '', regex=True)
        df['date'] = df['date'].dt.strftime('%d/%m/%Y')
        tel = df['tel'][df['tel'].duplicated()]
        email = df['email'][df['email'].duplicated()]
        tel_index = tel.index
        email_index = email.index
        for i, v in zip(tel_index, tel):
            df.loc[i, 'tag'] = np.array([[f'ซ้ำ {v}']])
        for i, v in zip(email_index, email):
            pre = df.loc[i, 'tag']
            if isinstance(pre, list):
                pre.append(f'ซ้ำ {v}')

        return df

    def sorting_table(self, dfs):
        if self.channel and not self.product and not self.before_end_date and not self.tag:
            dfs = dfs.loc[dfs['channel'] == self.channel]
            dfs['date'] = dfs['date'].dt.strftime('%d/%m/%Y')
            dfs = dfs.replace(np.nan, '', regex=True)
            return dfs

        elif self.product and not self.channel and not self.before_end_date and not self.tag:
            dfs = dfs.loc[dfs['product'] == self.product]
            dfs['date'] = dfs['date'].dt.strftime('%d/%m/%Y')
            dfs = dfs.replace(np.nan, '', regex=True)
            return dfs

        elif self.tag and not self.channel and not self.before_end_date and not self.product:
            dfs = dfs[dfs['tag'].apply(lambda x: x == self.tag)]
            dfs['date'] = dfs['date'].dt.strftime('%d/%m/%Y')
            result = dfs.replace(np.nan, '', regex=True)
            return result

        elif self.product and self.channel and self.tag:
            dfs = dfs.loc[dfs['channel'] == self.channel]
            dfs = dfs.loc[dfs['product'] == self.product]
            dfs = dfs[dfs['tag'].apply(lambda x: x == self.tag)]
            dfs['date'] = dfs['date'].dt.strftime('%d/%m/%Y')
            dfs = dfs.replace(np.nan, '', regex=True)
            return dfs

        elif self.product and self.channel:
            dfs = dfs.loc[dfs['channel'] == self.channel]
            dfs = dfs.loc[dfs['product'] == self.product]
            dfs['date'] = dfs['date'].dt.strftime('%d/%m/%Y')
            dfs = dfs.replace(np.nan, '', regex=True)
            return dfs

        elif self.product and self.tag:
            dfs = dfs.loc[dfs['product'] == self.product]
            dfs = dfs[dfs['tag'].apply(lambda x: x == self.tag)]
            dfs['date'] = dfs['date'].dt.strftime('%d/%m/%Y')
            dfs = dfs.replace(np.nan, '', regex=True)
            return dfs

        elif self.channel and self.tag:
            dfs = dfs.loc[dfs['channel'] == self.channel]
            dfs = dfs[dfs['tag'].apply(lambda x: x == self.tag)]
            dfs['date'] = dfs['date'].dt.strftime('%d/%m/%Y')
            dfs = dfs.replace(np.nan, '', regex=True)
            return dfs

        elif self.before_end_date and self.channel:
            dfs = dfs.loc[dfs['channel'] == self.channel]

        elif self.before_end_date and self.product:
            dfs = dfs.loc[dfs['product'] == self.product]

        elif self.before_end_date and self.tag:
            dfs = dfs[dfs['tag'].apply(lambda x: x == self.tag)]

        elif self.before_end_date and self.product and self.tag:
            dfs = dfs.loc[dfs['product'] == self.product]
            dfs = dfs[dfs['tag'].apply(lambda x: x == self.tag)]

        elif self.before_end_date and self.channel and self.tag:
            dfs = dfs.loc[dfs['channel'] == self.product]
            dfs = dfs[dfs['tag'].apply(lambda x: x == self.tag)]

        elif self.product and self.channel and self.tag and self.before_end_date:
            dfs = dfs[dfs['tag'].apply(lambda x: x == self.tag)]
            dfs = dfs.loc[dfs['channel'] == self.channel]
            dfs = dfs.loc[dfs['product'] == self.product]

        d = datetime.strptime(self.after_start_date, '%Y-%m-%d')
        self.after_start_date = "{}-{}-{}".format(d.year, d.month, d.day)

        d = datetime.strptime(self.before_end_date, '%Y-%m-%d')
        self.before_end_date = "{}-{}-{}".format(d.year, d.month, d.day)

        after_start_date = dfs['date'] >= self.after_start_date
        before_end_date = dfs['date'] <= self.before_end_date
        between_two_dates = after_start_date & before_end_date
        filtered_dates = dfs.loc[between_two_dates]
        filtered_dates['date'] = filtered_dates['date'].dt.strftime('%d/%m/%Y')
        filtered_dates = filtered_dates.replace(np.nan, '', regex=True)
        return filtered_dates

    def export_excel(self):
        data = []
        for i in self.id:
            v = self.database.find_one(self.collection, query={'id': i})
            v = dict(v)
            data.append(v)

        index = len(data)
        index = [i + 1 for i in range(index)]
        df = pd.DataFrame(data, index=index)
        df = df.replace(np.nan, '', regex=True)
        self.filter_data(df)
        df = df.drop(['id'], axis=1)
        writer = pd.ExcelWriter('static/excels/customers.xlsx')
        df.to_excel(writer, sheet_name='Sheet1')
        return writer

    def import_excel(self, username: Optional[str] = None, uid: Optional[str] = None):
        file = pd.read_excel(self.path_excel, engine='openpyxl')
        df = pd.DataFrame(file)
        df = df.replace(np.nan, '', regex=True)
        self.filter_data(df)
        df['userId'] = ''
        df['username'] = username
        df['uid'] = uid
        _d = datetime.now()
        df["date"] = _d.strftime("%d/%m/%y")
        df["time"] = _d.strftime("%H:%M:%S")
        ids = range(len(df))
        ids_lst = [CutId(_id=ObjectId()).dict()['id'] for v in ids]
        df["id"] = ids_lst
        data = df.to_dict('records')
        self.database.insert_many(self.collection, data)

    @staticmethod
    def last_date_today(df):
        _d = datetime.now()
        last_datetime = df['date'] == _d.strftime("%d/%m/%y")
        df = df.replace(np.nan, '', regex=True)
        return df.loc[last_datetime]
