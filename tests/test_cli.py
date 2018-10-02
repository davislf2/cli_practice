"""Tests for our main qmatch CLI module."""

from subprocess import PIPE, Popen as popen
from unittest import TestCase
from unittest import SkipTest
import unittest

from qmatch import __version__ as VERSION

class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['qmatch', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue(b'Usage:' in output)

        output = popen(['qmatch', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue(b'Usage:' in output)

class TestVersion(TestCase):
    def test_returns_version_information(self):
        # try:
        output = popen(['qmatch', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(str(output.strip(), encoding = "utf-8"), VERSION)
        # except NotImplementedError:
        #     raise SkipTest()

# class TestError(TestCase):
    # def test_not_implemented(self):
        # raise NotImplementedError('You must implement the run() method yourself!')

if __name__ == "__main__":
    unittest.main()