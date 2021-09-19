from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd
from attacut import tokenize


def model_spam(text):
    df = pd.read_excel('machine_leanning/datasets_spam.xlsx')
    df = df.drop('Unnamed: 0', axis=1)
    df = df.replace(np.nan, '', regex=True)
    vectorizer = CountVectorizer(tokenizer=tokenize)
    vectorize_message = vectorizer.fit_transform(df['message'].values)
    vectorizer.get_feature_names()
    classifier = MultinomialNB()
    targets = df['label'].values
    classifier.fit(vectorize_message, targets)
    examples = [text]  # example ตรงนี้ ถ้าสร้างใหม่ให้มี , ตามด้วย 'test'
    example_counts = vectorizer.transform(examples)
    predictions = classifier.predict(example_counts)
    print(predictions)
    return list(predictions)
