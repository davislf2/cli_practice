"""The question match algorithm."""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


class BestMatch(object):
    def __init__(self):
        self.question = None
        self.df = None
        self.df_ref = None
        self.question_code_df = None

    def run_best_match(self, question, df, df_ref):
        # Run the process of finding the best match
        self.question = question
        self.df = df
        self.df_ref = df_ref
        results = self.model(self.df, self.df_ref, self.question)
        return results

    def model(self, df, df_ref, question):

        # Split data into test and train sets
        X_train, X_test, y_train, y_test = train_test_split(
            df['question'], df['code'], random_state=0)

        # Count Vectorising
        count_vect = CountVectorizer()
        X_train_counts = count_vect.fit_transform(X_train)

        # TF-IDF
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

        # Multinomial Naive Bayes Model Fit
        clf = MultinomialNB().fit(X_train_tfidf, y_train)

        # Classification model prediction for single result
        # res = clf.predict(count_vect.transform([question]))
        # respond = df_ref.loc[df_ref['code'].isin(res.tolist())]
        # respond.question

        # Classification model prediction for probability results
        res_prob = clf.predict_proba(count_vect.transform([question]))

        # Add probabilty column to the original df
        df_new = df_ref.copy()
        df_new['prob'] = res_prob[0, :]

        # Choose the top 2 results
        return df_new.nlargest(2, 'prob')
