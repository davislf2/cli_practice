"""Tests for preprocessing stage."""

from unittest import TestCase
from qmatch.nlp import preprocessing
import pandas as pd


class TestPreprocessing(TestCase):
    prep = None
    b = None
    df = None
    df_ref = None

    def setUp(self):
        self.__class__.prep = preprocessing.Preprocessing()

    def test_load_file(self):
        self.__class__.df = self.__class__.prep.load_file()
        self.assertEqual(self.__class__.df.shape, (298, 2))

    def test_load_ref_file(self):
        self.__class__.df_ref = self.__class__.prep.load_ref_file()
        self.assertEqual(self.__class__.df_ref.shape, (4, 2))

    def test_clean_data(self):
        self.test_load_file()
        self.__class__.df = self.__class__.prep.clean_data(self.__class__.df)
        self.assertEqual(self.__class__.df.shape, (295, 2))
