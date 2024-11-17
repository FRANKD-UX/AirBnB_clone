#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name != 'BaseModel':
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
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
        instances = storage.all(BaseModel)
        key = f"BaseModel.{instance_id}"
        if key not in instances:
            print("** no instance found **")
            return
        print(instances[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        Ex: $ destroy BaseModel 1234-1234-1234
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
        instances = storage.all(BaseModel)
        key = f"BaseModel.{instance_id}"
        if key not in instances:
            print("** no instance found **")
            return
        del instances[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        on or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        if arg:
            class_name = arg.split()[0]
            if class_name != 'BaseModel':
                print("** class doesn't exist **")
                return
            instances = storage.all(BaseModel)
            print([str(instances[key])
                   for key
                   in instances if key.startswith('BaseModel')])
        else:
            instances = storage.all(BaseModel)
            print([str(instances[key])
                   for key in instances if key.startswith('BaseModel')])

    def do_update(self, arg):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute.
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
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
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]

        instances = storage.all(BaseModel)
        key = f"BaseModel.{instance_id}"
        if key not in instances:
            print("** no instance found **")
            return

        # Type cast the attribute value
        try:
            if isinstance(getattr(instances[key], attribute_name), int):
                attribute_value = int(attribute_value)
            elif isinstance(getattr(instances[key], attribute_name), float):
                attribute_value = float(attribute_value)
        except ValueError:
            pass  # Let the attribute remain as string if it can't be cast

        setattr(instances[key], attribute_name, attribute_value)
        instances[key].save()

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program when the EOF signal is received"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
