"""The question match algorithm."""

import pandas as pd
import numpy as np
import os

class BestMatch(object):

    def __init__(self):
        self.df = None

    def run_best_match(self, question):
        self.question = question
        self.load_file()
        self.clean_data(self.df)
        
        results = self.question
        return results

    def load_file(self):
        # Load data, remove commas and rename column
        path = "../../resource/labeled_data.csv"
        df = pd.read_csv(os.path.join(os.path.dirname(__file__), path), sep='|', encoding = "ISO-8859-1")
        df = df.rename(index = str, columns = {"question_text": "question", "code,,": "code"})
        df["code"] = df["code"].str.replace(",,","")
        df["code"] = df["code"].str.replace(",","")
        df["code"] = df["code"].str.replace(" ","")
        self.df = df

    def clean_data(self, df):
        # Remove duplicates, nan value
        # df = self.df
        df.loc[:] = df.drop_duplicates()  # df.loc[:] Prevent the warning of "A value is trying to be set on a copy of a slice from a DataFrame"
        df["question"][df["question"]==""] = np.nan
        df["code"][df["code"]==""] = np.nan
        df = df.dropna()
        self.df = df
    

    