#!/usr/bin/python3
"""a program contains the entry point of the command interpreter"""

import cmd
import json
from models import storage
from models.base_model import BaseModel
import re


class HBNBCommand(cmd.Cmd):
    """a class for command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """quit to exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            n = storage.classes()[line]()
            n.save()
            print(n.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            phrase = line.split(' ')
            if phrase[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(phrase) < 2:
                print("** instance id missing **")
            else:
                key = f"{phrase[0]}.{phrase[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            phrase = line.split(' ')
            if phrase[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(phrase) < 2:
                print("** instance id missing **")
            else:
                key = f"{phrase[0]}.{phrase[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
       if line != "":
            phrase = line.split(' ')
            if phrase[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                k = [str(obj) for key, obj in storage.all().items()
                     if type(obj).__name__ == phrase[0]]
                print(k) 
        else:
            k = [str(obj) for key, obj in storage.all().items()]
            print(k)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return

        reg_ex = r'^(\S+)\s+(\S+)\s+(\S+)\s+"([^"]*)"'
        match = re.match(reg_ex, line)
        if not match:
            print("** class name missing **")
            return

        classname, uid, attribute, value = match.groups()

        if classname not in storage.classes():
            print("** class doesn't exist **")
        elif not uid:
            print("** instance id missing **")
        else:
            clu = f"{classname}.{uid}"
            if clu not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[clu], attribute, value)
                storage.all()[clu].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
