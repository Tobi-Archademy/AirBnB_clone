#!/usr/bin/python3
""" Command interpreter to manager the AirBnB objects
"""
import cmd, sys
import string


class BaseModel(cmd.Cmd):
    """Represents the Base model for all other classes in the project
    """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Cleanly exits the program
        """
        return True

    def do_quit(self, arg):
        """Quits the program
        """
        sys.exit(1)


if __name__ == "__main__":
    BaseModel().cmdloop()
