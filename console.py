#!/usr/bin/python3

"""
Script containing the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class inheriting from the cmd.Cmd class

    It contains this methods:
        quit - exits the program
        help - lists all methods contained

    Our cutom prompt is (hbnb)
    """

    prompt = "(hbnb)"

    def do_EOF(self, line):
        """Ctrl-D to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
