"""Tests for best_match module."""

from unittest import TestCase
from qmatch.nlp import best_match
from qmatch.nlp import preprocessing
from tests.nlp import test_preprocessing
import pandas as pd

class TestBestMatch(TestCase):
    prep = None
    best = None
    df = None
    df_ref = None

    def setUp(self):
        self.__class__.prep = preprocessing.Preprocessing()
        self.__class__.best = best_match.BestMatch()

    def test_model(self):
        self.__class__.df = self.__class__.prep.load_file()
        self.__class__.df_ref = self.__class__.prep.load_ref_file()
        self.__class__.df = self.__class__.prep.clean_data(self.__class__.df)
        question = "I understand what I need to do to move up at StarWars"
        result = self.__class__.best.model(self.__class__.df, self.__class__.df_ref, question)
        q0 = "I know what I need to do to be successful in my role"
        q1 = "The information I need to do my job effectively is readily available"
        p0 = 0.9312706418495941
        p1 = 0.06823556535816563
        self.assertEqual(q0, result['question'][0])
        self.assertEqual(q1, result['question'][1])
        self.assertEqual(p0, result['prob'][0])
        self.assertEqual(p1, result['prob'][1])
