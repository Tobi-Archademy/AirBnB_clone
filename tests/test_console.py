#!/usr/bin/python3
"""Unittest module to test `console.py`

Classes:
    TestHBNBCommand_prompt
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_quit
"""
import io
import sys
import unittest
from contextlib import redirect_stdout
from console import HBNBCommand


class TestHBNBCommand_prompt(unittest.TestCase):
    """Unittests for testing HBNBCommand prompting
    """

    def test_prompt_output(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_prompt_with_emptyline(self):
        s = io.StringIO()
        with redirect_stdout(s):
            HBNBCommand().onecmd("")
        output = s.getvalue()
        self.assertEqual("", output.strip())


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing HBNBCommand `help`
    """

    def test_help_quit(self):
        msg = "Quit command to exit the program"
        s = io.StringIO()
        with redirect_stdout(s):
            HBNBCommand().onecmd("help quit")
        output = s.getvalue()
        self.assertEqual(msg, output.strip())

    def test_help_EOF(self):
        msg = "`EOF` signal to exit the program"
        s = io.StringIO()
        with redirect_stdout(s):
            HBNBCommand().onecmd("help EOF")
        output = s.getvalue()
        self.assertEqual(msg, output.strip())
