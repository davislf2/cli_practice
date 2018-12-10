"""The data preprocessing stage."""

import pandas as pd
import numpy as np
import os
from pathlib import Path


class Preprocessing(object):
    def load_file(self):
        # Load labeled data, remove commas and rename column
        path = "../../resource/labeled_data.csv"
        df = pd.read_csv(
            os.path.join(os.path.dirname(__file__), path),
            sep='|',
            encoding="ISO-8859-1")
        df = df.rename(
            index=str, columns={
                "question_text": "question",
                "code,,": "code"
            })
        df["code"] = df["code"].str.replace(",,", "")
        df["code"] = df["code"].str.replace(",", "")
        df["code"] = df["code"].str.replace(" ", "")
        return df

    def load_ref_file(self):
        # Load reference question data, remove commas and rename column
        path = "../../resource/reference_questions.csv"
        df_ref = pd.read_csv(
            os.path.join(os.path.dirname(__file__), path),
            sep='|',
            encoding="ISO-8859-1")
        df_ref = df_ref.rename(
            index=str, columns={
                "question_text": "question",
                "code,,": "code"
            })
        df_ref["code"] = df_ref["code"].str.replace(",,", "")
        df_ref["code"] = df_ref["code"].str.replace(",", "")
        df_ref["code"] = df_ref["code"].str.replace(" ", "")
        df_ref = df_ref.sort_values(by=["code"])
        return df_ref

    def clean_data(self, df):
        # Remove duplicates, nan value
        df.loc[:] = df.drop_duplicates(
        )  # df.loc[:] Prevent the warning of "A value is trying to be set on a copy of a slice from a DataFrame"
        df['question'].replace('', np.nan, inplace=True)
        df['code'].replace('', np.nan, inplace=True)
        df = df.dropna()
        self.question_code_df = df['code'].drop_duplicates()
        return df
