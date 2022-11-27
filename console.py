#!/usr/bin/python3
""" contains the entry point of the command interpreter """

import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBcommand(cmd.Cmd):
    """command interpreter for HBNB"""
    __classList = {
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
    }

    prompt = "(hbnb) "

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """quit command exits the program"""
        return True

    def do_EOF(self, arg):
        """EOF command exits the program"""
        print()
        return True

    def emptyline(self):
        """Does notting when empty line is received"""
        pass

    def do_create(self, cls):
        """createa a new instance of BaseModel, and
        saves it (to the JSON file) and prints the id"""
        if len(cls) == 0:
            print("** class name missing **")
        elif cls not in HBNBcommand.__classList:
            print("** class doesn't exist **")
        else:
            new = eval(cls)()
            models.storage.save()
            print(new.id)

    def do_show(self, args):
        """prints the string representation of an instance based
        on the class name and id"""
        objD = models.storage.all()
        argList = parse(args)
        if len(argList) == 0:
            print("** class name missing **")
        elif argList[0] not in HBNBcommand.__classList:
            print("** class doesn't exist **")
        elif len(argList) < 2:
            print("** instance id missing **")
        elif argList[0] + "." + argList[1] not in objD:
            print("** no instance found **")
        else:
            key = argList[0] + "." + argList[1]
            obj = objD[key]
            print(obj)

    def do_destroy(self, args):
        """deletes an instance based on the class name and id"""
        objD = models.storage.all()
        argList = parse(args)
        if len(argList) == 0:
            print("** class name missing **")
        elif argList[0] not in HBNBcommand.__classList:
            print("** class doesn't exist **")
        elif len(argList) < 2:
            print("** instance id missing **")
        elif argList[0] + "." + argList[1] not in objD:
            print("** no instance found **")
        else:
            key = argList[0] + "." + argList[1]
            obj = objD[key]
            del objD[key]
            models.storage.save()

    def do_all(self, arg):
        """ prints all string representation of all instances based or not
        on the class name"""
        objD = models.storage.all()
        argList = parse(arg)
        objList = []
        if len(argList) > 0 and argList[0] not in HBNBcommand.__classList:
            print("** class doesn't exist **")
        else:
            objList = []
            if len(argList) == 0:
                for obj in objD.values():
                    objList.append(obj.__str__())
            else:
                for obj in objD.values():
                    if argList[0] == (obj.to_dict())["__class__"]:
                        objList.append(obj.__str__())
            print(objList)

    def do_update(self, arg):
        """ updates an instance based on the class name and id by adding or
        updating attribute (save the change to the JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>
        """
        objD = models.storage.all()
        argL = parse(arg)

        if len(argL) == 0:
            print("** class name missing **")
        elif argL[0] not in HBNBcommand.__classList:
            print("** class doesn't exist **")
        elif len(argL) < 2:
            print("** instance id missing **")
        elif argL[0] + "." + argL[1] not in objD:
            print("** no instance found **")
        elif len(argL) < 3:
            print("** attribute name missing **")
        elif len(argL) < 4:
            try:
                type(eval(argL[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argL) == 4:
            obj = objD["{}.{}".format(argL[0], argL[1])]
            if argL[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argL[2]])
                obj.__dict__[argL[2]] = valtype(argL[3])
            else:
                obj.__dict__[argL[2]] = argL[3]
        elif type(eval(argL[2])) == dict:
            obj = objD["{}.{}".format(argL[0], argL[1])]
            for k, v in eval(argL[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        models.storage.save()

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in models.storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBcommand().cmdloop()
