#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
"""file that controls the entry point of command interpreter"""


class HBNBCommand(cmd.Cmd):
    """a custom prompt"""
    __classes = ("BaseModel",)
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
