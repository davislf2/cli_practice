"""The match command."""


from json import dumps

from .base import Base


class M(Base):
    """Say hello, world!"""

    def run(self):
        sentence = self.options["<question>"]
        print(sentence)
        # print('Hello, world!')
        # print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
