#!/usr/bin/python3
""" Command interpreter (the `Console`) to manager the AirBnB objects
"""
import cmd


class Console(cmd.Cmd):
    """Represents the Base model for all other classes in the project

    Attributes:
        prompt (str): Displays a `(hbnb`) prompt and waits for a command
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Called when nothing is typed before hitting enter
        """
        pass

    def do_EOF(self, arg):
        """Cleanly exits the program by the `EOF` signal
        """
        print("")
        return True

    def do_quit(self, arg):
        """Quits the program
        """
        return True


if __name__ == "__main__":
    Console().cmdloop()
