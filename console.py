#!/usr/bin/python3
""" Command interpreter (the `HBNBCommand`) to manager the AirBnB objects
"""
import cmd


class HBNBCommand(cmd.Cmd):
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
        """`EOF` signal to exit the program
        """
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
