#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for managing AirBnB objects.
    """
    prompt = '(hbnb) '

    def do_create(self, arg):
        """
        Create a new instance of BaseModel,
        save it to JSON file, and print the id.
        Usage: create <class name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != 'BaseModel':
            print("** class doesn't exist **")
            return
        instance = BaseModel()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an
        instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != 'BaseModel':
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instances = storage.all()
        if key not in instances:
            print("** no instance found **")
            return
        print(instances[key])

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and
        id, save the change to the JSON file.
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != 'BaseModel':
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instances = storage.all()
        if key not in instances:
            print("** no instance found **")
            return
        del instances[key]
        storage.save()

    def do_all(self, arg):
        """
        Print all string representations of all
        instances based on or not on the class name.
        Usage: all <class name> or all
        """
        args = arg.split()
        if args:
            class_name = args[0]
            if class_name != 'BaseModel':
                print("** class doesn't exist **")
                return
            instances = storage.all()
            print([str(instances[key])
                   for key
                   in instances
                   if key.startswith(class_name)])
        else:
            instances = storage.all()
            print([str(instances[key]) for key in instances])

    def do_update(self, arg):
        """
        Update an instance based on the class name
        and id by adding or updating an attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != 'BaseModel':
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instances = storage.all()
        if key not in instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3].strip('"')
        setattr(instances[key], attribute_name, attribute_value)
        instances[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
