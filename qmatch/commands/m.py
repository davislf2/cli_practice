"""The match command."""


from json import dumps

from .base import Base


class M(Base):
    """Say hello, world!"""

    def run(self):
        question = self.options["<question>"]
        print(question)
        # print("I know what I need to do to be successful in my role|ALI.5")
        # print('Hello, world!')
        # print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
