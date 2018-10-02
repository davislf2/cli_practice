"""The match command."""


from json import dumps
import pandas as pd

from .base import Base
from ..nlp import best_match

class M(Base):
    """Say hello, world!"""

    def run(self):
        question = self.options["<question>"]

        # from ..nlp.best_match import load_file
        # print("return ",load_file(question))
        
        b = best_match.BestMatch()
        # print(b.run_best_match(question))
        result = b.run_best_match(question)

        self.align_print("Questions", "Probability")
        for index, row in result.iterrows():
            self.align_print(row['question'], row['prob'])

        # print(b.df_ref.head())
        # print(b.run_best_match(question).head())
    
    def align_print(self, x, y):
        line_new = '{:<90}  {:<12}'.format(x, y)
        print(line_new)
