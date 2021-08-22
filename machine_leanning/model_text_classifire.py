from config.db import MongoDB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from pythainlp.tokenize import word_tokenize
import re

client = 'mongodb://127.0.0.1:27017'
db = MongoDB(database_name='Mango', uri=client)
collection = 'intents'


def intent_model(p_text=str, query=str):
    data = db.find(collection=collection, query={'access_token': query})
    data = list(data)
    sum_text = []
    ans_text = [x['answer'] for x in data]
    embedding = [x for x in range(len(ans_text))]
    for text in data:
        txt = ''
        for v in text['question']:
            txt += v
        sum_text.append(txt)
    if len(sum_text) == 1 and len(ans_text) == 1:
        return {'require': 'ต้องสร้าง Intent อย่างน้อย 2 Intent ก่อนถึงจะสามารถใช้งานบอทได้ครับ'}
    sum_text = [re.sub(re.compile(r'\s+'), '', i) for i in sum_text]
    tf_vect = TfidfVectorizer(tokenizer=word_tokenize)
    x_train_vect = tf_vect.fit_transform(sum_text)
    my_classifire = LogisticRegression(penalty='none')
    my_classifire.fit(x_train_vect, embedding)
    x_test_vect = tf_vect.transform([p_text])
    prediction = my_classifire.predict(x_test_vect)
    proba = my_classifire.predict_proba(x_test_vect)[0][prediction]
    nameIntent = data[prediction[0]]
    return {'predict': prediction, 'confident': proba, 'answers': ans_text, 'name': nameIntent.get('name')}
