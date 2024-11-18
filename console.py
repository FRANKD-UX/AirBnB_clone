#!/usr/bin/env python3

import cmd
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the AirBnB clone project"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["State", "City", "Place", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return

        class_name = args[0]
        new_obj = globals()[class_name]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """Shows the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["State", "City", "Place", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroys an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["State", "City", "Place", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if obj:
            storage.delete(obj)
            storage.save()
            print("** instance deleted **")
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["State", "City", "Place", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if obj:
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(obj, args[2], args[3])
            obj.save()
            print("** instance updated **")
        else:
            print("** no instance found **")

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program on EOF"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
