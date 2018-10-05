"""The match command."""

from json import dumps
import pandas as pd

from .base import Base
from ..nlp import preprocessing
from ..nlp import best_match

class Match(Base):
    """Match the commands"""

    def run(self):
        question = self.options["<question>"]

        # Preprocessing data: load and cleaning
        prep = preprocessing.Preprocessing()
        df = prep.load_file()
        df_ref = prep.load_ref_file()
        df = prep.clean_data(df)

        # Best match algorithm
        best = best_match.BestMatch()
        result = best.run_best_match(question, df, df_ref)

        self.align_print("Questions", "Probability")
        for index, row in result.iterrows():
            self.align_print(row['question'], row['prob'])
    
    def align_print(self, x, y):
        line_new = '{:<90}  {:<12}'.format(x, y)
        print(line_new)
