"""Tests for our `qmatch m <question>` subcommand."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


class TestM(TestCase):
    def test_returns_multiple_lines(self):
        question = "I understand what I need to do to move up at StarWars"
        output = popen(['qmatch', 'm', question], stdout=PIPE).communicate()[0]
        lines = output.decode('utf-8').split('\n')
        self.assertTrue(len(lines) != 1)

    def test_returns_best_match(self):
        question = "I understand what I need to do to move up at StarWars"
        output = popen(['qmatch', 'm', question], stdout=PIPE).communicate()[0]

        result = ""
        result += self.align_print("Questions", "Probability")
        result += self.align_print("I know what I need to do to be successful in my role", "0.9312706418495941")
        result += self.align_print("The information I need to do my job effectively is readily available", "0.06823556535816563")

        self.assertTrue(result.encode() in output)

    def align_print(self, x, y):
        line_new = '{:<90}  {:<12}\n'.format(x, y)
        return line_new