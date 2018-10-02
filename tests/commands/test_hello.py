"""Tests for our `qmatch hello` subcommand."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


class TestHello(TestCase):
    def test_returns_multiple_lines(self):
        output = popen(['qmatch', 'hello'], stdout=PIPE).communicate()[0]
        lines = output.decode('utf-8').split('\n')
        self.assertTrue(len(lines) != 1)

    def test_returns_hello_world(self):
        output = popen(['qmatch', 'hello'], stdout=PIPE).communicate()[0]
        self.assertTrue(b'Hello, world!' in output)
