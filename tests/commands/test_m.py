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
        self.assertTrue(b'ALI.5' in output)
