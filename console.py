#!/usr/bin/env python3

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        new_instance = self.__classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        class_name, *args = arg.split()
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if not args:
            print("** instance id missing **")
            return
        instance_id = args[0]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance"""
        if not arg:
            print("** class name missing **")
            return
        class_name, *args = arg.split()
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if not args:
            print("** instance id missing **")
            return
        instance_id = args[0]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg:
            class_name = arg.split()[0]
            if class_name not in self.__classes:
                print("** class doesn't exist **")
                return
            instances = [str(obj) for key, obj in storage.all(
            ).items() if isinstance(obj, self.__classes[class_name])]
        else:
            instances = [str(obj) for obj in storage.all().values()]
        print(instances)

    def do_update(self, arg):
        """Updates an instance"""
        if not arg:
            print("** class name missing **")
            return
        class_name, *args = arg.split()
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if not args:
            print("** instance id missing **")
            return
        instance_id = args[0]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 2:
            print("** attribute name missing **")
            return
        attribute_name = args[1]
        if len(args) < 3:
            print("** value missing **")
            return
        attribute_value = args[2]
        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()
