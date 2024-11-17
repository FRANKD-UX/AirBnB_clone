#!/usr/bin/python3
"""Module for command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB project"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D) to exit the program"""
        return True

    def emptyline(self):
        """Override the default behavior for empty lines"""
        pass

    def do_help(self, arg):
        """Override the help command to display help message"""
        print("This is the help command for the HBNB command interpreter.")


if __name__ == '__main__':
    """Start the command interpreter"""
    HBNBCommand().cmdloop()
