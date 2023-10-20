#!/usr/bin/python3
"""importing all necessary classes to be used"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
"""file that controls the entry point of command interpreter"""


class HBNBCommand(cmd.Cmd):
    """a custom prompt"""
    prompt = "(hbnb) "
    __classes = ("BaseModel", "User", "State", "Place",
                 "City", "Amenity", "Review")

    def do_quit(self, arg):
        """quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        return True

    def emptyline(self):
        """shouldn’t execute anything"""
        return

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(f"{args[0]}")()
            print(new_obj.id)
        storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{args[0]}.{args[1]}"]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split()

        if len(args) == 0:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            dic = storage.all().items()
            print([str(val) for key, val in dic if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
         by adding or updating attribute save the change into the JSON file
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            object_cls_name = args[0]
            object_id = args[1]
            object_key = f"{object_cls_name}.{object_id}"
            object_ = storage.all()[object_key]

            attribute_name = args[2]
            attribute_value = args[3]

            if attribute_value[0] == '"':
                attribute_value = attribute_value[1:-1]

            if hasattr(object_, attribute_name):
                attribute_type = type(getattr(object_, attribute_name))

                if attribute_type in [str, int, float]:
                    attribute_value = attribute_type(attribute_value)
                    setattr(object_, attribute_name, attribute_value)
            else:
                setattr(object_, attribute_name, attribute_value)
            storage.save()

    def default(self, arg):
        """retrieve all instances of a class by using:
           <class name>.all()
        """
        args = arg.split(".")
        if args[0] in self.__classes:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                dic = storage.all().items()
                num_list = [val for key, val in dic if key.startswith(args[0])]
                print(len(num_list))
            elif args[1].startswith("show"):
                _id = args[1].split('"')[1]
                self.do_show(f"{args[0]} {_id}")
            elif args[1].startswith("destroy"):
                _id = args[1].split('"')[1]
                self.do_destroy(f"{args[0]} {_id}")
            elif args[1].startswith("update"):
                _id = args[1].split('"')[1]
                attr_name = args[1].split(', ')[1]
                attr_value = args[1].split(', ')[2][0:-1]
                self.do_update(f"{args[0]} {_id} {attr_name} {attr_value}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
