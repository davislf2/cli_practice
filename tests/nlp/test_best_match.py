"""Tests for best_match module."""

from subprocess import PIPE, Popen as popen
from unittest import TestCase
from qmatch.nlp import best_match
import pandas as pd

class TestBestMatch(TestCase):
    def test_load_file(self):
        b = best_match.BestMatch()
        b.load_file()
        self.assertTrue( b.df.shape == (298, 2))

