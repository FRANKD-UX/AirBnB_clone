#!/usr/bin/python3
"""Module for the AirBnB clone command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone"""

    prompt = "(hbnb) "  # Sets the command prompt

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Overrides the default behavior to do nothing on empty input"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
