#!/usr/bin/python3
"""Unittest module to test `console.py`

Classes:
    TestConsole_prompt
    TestConsole_help
    TestConsole_exit
    TestConsole_quit
"""
import io
import sys
import unittest
from contextlib import redirect_stdout
from console import Console


class TestConsole_prompt(unittest.TestCase):
    """Unittests for testing Console prompting
    """

    def test_prompt_output(self):
        self.assertEqual("(hbnb) ", Console.prompt)

    def test_prompt_with_emptyline(self):
        s = io.StringIO()
        with redirect_stdout(s):
            Console().onecmd("")
        output = s.getvalue()
        self.assertEqual("", output.strip())


class TestConsole_help(unittest.TestCase):
    """Unittests for testing Console `help`
    """

    def test_help_quit(self):
        msg = "Quits the program"
        s = io.StringIO()
        with redirect_stdout(s):
            Console().onecmd("help quit")
        output = s.getvalue()
        self.assertEqual(msg, output.strip())

    def test_help_EOF(self):
        msg = "Cleanly exits the program by the `EOF` signal"
        s = io.StringIO()
        with redirect_stdout(s):
            Console().onecmd("help EOF")
        output = s.getvalue()
        self.assertEqual(msg, output.strip())
