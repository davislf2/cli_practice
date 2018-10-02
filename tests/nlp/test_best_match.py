"""Tests for best_match module."""

from subprocess import PIPE, Popen as popen
from unittest import TestCase
from qmatch.nlp import best_match
import pandas as pd

class TestBestMatch(TestCase):
    b = None
    df = None
    df_ref = None

    def setUp(self):
        self.__class__.b = best_match.BestMatch()

    def test_load_file(self):
        self.__class__.b.load_file()
        self.__class__.df = self.__class__.b.df
        self.assertEqual(self.__class__.df.shape, (298, 2))

    def test_load_ref_file(self):
        self.__class__.b.load_ref_file()
        self.__class__.df_ref = self.__class__.b.df_ref
        self.assertEqual(self.__class__.df_ref.shape, (4, 2))

    def test_clean_data(self):
        self.test_load_file()
        self.__class__.b.clean_data(self.__class__.df)
        self.__class__.df = self.__class__.b.df
        self.assertEqual(self.__class__.df.shape, (295, 2))

    def test_model(self):
        self.test_clean_data()
        self.test_load_ref_file()
        question = "I understand what I need to do to move up at StarWars"
        result = self.__class__.b.model(self.__class__.df, self.__class__.df_ref, question)
        q0 = "I know what I need to do to be successful in my role"
        q1 = "The information I need to do my job effectively is readily available"
        p0 = 0.9312706418495941
        p1 = 0.06823556535816563
        self.assertEqual(q0, result['question'][0])
        self.assertEqual(q1, result['question'][1])
        self.assertEqual(p0, result['prob'][0])
        self.assertEqual(p1, result['prob'][1])
