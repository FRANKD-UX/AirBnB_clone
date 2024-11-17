#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_help(self, arg):
        """List available commands with "help" or
        detailed help for a command"""
        return super().do_help(arg)


if __name__ == "__main__":
    import sys

    if sys.stdin.isatty():
        # Interactive mode
        HBNBCommand().cmdloop()
    else:
        # Non-interactive mode
        HBNBCommand(stdin=sys.stdin).cmdloop()
