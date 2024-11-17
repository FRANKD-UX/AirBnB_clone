#!/usr/bin/python3
"""Module for command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = globals()[arg]
        except KeyError:
            print("** class doesn't exist **")
            return
        instance = class_name()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg and arg not in globals():
            print("** class doesn't exist **")
            return
        all_instances = []
        for key, instance in storage.all().items():
            if not arg or key.startswith(arg):
                all_instances.append(str(instance))
        print(f"[{', '.join(all_instances)}]")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]

        # Cast the attribute value to the correct type
        if isinstance(getattr(instance, attribute_name), str):
            setattr(instance, attribute_name, attribute_value)
        elif isinstance(getattr(instance, attribute_name), int):
            setattr(instance, attribute_name, int(attribute_value))
        elif isinstance(getattr(instance, attribute_name), float):
            setattr(instance, attribute_name, float(attribute_value))

        instance.save()


if __name__ == '__main__':
    """Start the command interpreter
    """
    HBNBCommand().cmdloop()
