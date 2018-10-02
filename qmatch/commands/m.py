"""The match command."""


from json import dumps

from .base import Base
from ..nlp import best_match

class M(Base):
    """Say hello, world!"""

    def run(self):
        question = self.options["<question>"]

        # from ..nlp.best_match import load_file
        # print("return ",load_file(question))
        
        b = best_match.BestMatch()
        # b.load_file()
        print(b.run_best_match(question))
        
        # print(b.df.head())
        # print(b.run_best_match(question).head())
    
