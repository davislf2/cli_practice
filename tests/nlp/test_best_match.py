"""Tests for best_match module."""

from subprocess import PIPE, Popen as popen
from unittest import TestCase
from qmatch.nlp import best_match
import pandas as pd

class TestBestMatch(TestCase):
    b = None
    df = None

    def setUp(self):
        self.__class__.b = best_match.BestMatch()

    def test_load_file(self):
        # b = best_match.BestMatch()
        self.__class__.b.load_file()
        self.__class__.df = self.__class__.b.df
        self.assertEqual(self.__class__.df.shape, (298, 2))
        
    def test_clean_data(self):
        self.test_load_file()
        self.__class__.b.clean_data(self.__class__.df)
        self.__class__.df = self.__class__.b.df
        self.assertEqual(self.__class__.df.shape, (295, 2))