#!/usr/bin/python3
import cmd
"""file that controls the entry point of command interpreter"""

class HBNBCommand(cmd.Cmd):
    """a custom prompt"""
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
