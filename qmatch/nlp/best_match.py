"""The question match algorithm."""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

class BestMatch(object):

    def __init__(self):
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
        
        results = self.question
        return results
        
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

    
    