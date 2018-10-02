"""The question match algorithm."""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
# from sklearn.cross_validation import train_test_split
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

    def run_best_match(self, question):
        # Run the process of finding the best match
        self.question = question
        self.load_file()
        self.load_ref_file()
        self.clean_data(self.df)
        # self.show_data_distribution(self.df)

        results = self.model(self.df, self.question)
        return results[0]
        
    def load_file(self):
        # Load labeled data, remove commas and rename column
        path = "../../resource/labeled_data.csv"
        df = pd.read_csv(os.path.join(os.path.dirname(__file__), path), sep='|', encoding = "ISO-8859-1")
        df = df.rename(index = str, columns = {"question_text": "question", "code,,": "code"})
        df["code"] = df["code"].str.replace(",,","")
        df["code"] = df["code"].str.replace(",","")
        df["code"] = df["code"].str.replace(" ","")
        self.df = df

    def load_ref_file(self):
        # Load reference question data, remove commas and rename column
        path = "../../resource/reference_questions.csv"
        df_ref = pd.read_csv(os.path.join(os.path.dirname(__file__), path), sep='|', encoding = "ISO-8859-1")
        df_ref = df_ref.rename(index=str, columns={"question_text": "question", "code,,": "code"})
        df_ref["code"] = df_ref["code"].str.replace(",,","")
        df_ref["code"] = df_ref["code"].str.replace(",","")
        df_ref["code"] = df_ref["code"].str.replace(" ","")
        df_ref = df_ref.sort_values(by = ["code"])
        self.df_ref = df_ref

    def clean_data(self, df):
        # Remove duplicates, nan value
        df.loc[:] = df.drop_duplicates()  # df.loc[:] Prevent the warning of "A value is trying to be set on a copy of a slice from a DataFrame"
        df["question"][df["question"]==""] = np.nan
        df["code"][df["code"]==""] = np.nan
        df = df.dropna()
        self.question_code_df = df['code'].drop_duplicates()
        self.df = df
    
    # def show_data_distribution(self, df):
    #     # (Optional) Show data distribution of df
    #     # Warning: It will stuck in VSCode terminal
    #     fig = plt.figure(figsize=(8,6))
    #     df.groupby('code').code.count().plot.bar(ylim=0)
    #     plt.show()
        
    # def train(self, classifier, X, y):
    #     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
    #     # print(X_train[:5], y_train[:5])
    #     # print(X_test[:5], y_test[:5])
    #     classifier.fit(X_train, y_train)
    #     print("Accuracy: %s" % classifier.score(X_test, y_test))
    #     return classifier

    def model(self, df, question):
        X_train, X_test, y_train, y_test = train_test_split(df['question'], df['code'], random_state = 0)
        count_vect = CountVectorizer()
        X_train_counts = count_vect.fit_transform(X_train)
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        clf = MultinomialNB().fit(X_train_tfidf, y_train)
        return clf.predict(count_vect.transform([question]))
    
    