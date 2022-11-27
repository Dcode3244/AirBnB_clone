#!/usr/bin/env python3
""" contains the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBcommand(cmd.Cmd):
    """command interpreter for HBNB"""
    __classList = ["BaseModel", "User",
                   "Place", "State",
                   "City", "Amenity",
                   "Review"]

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """quit command exits the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command exits the program\n"""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, cls):
        """createa a new instance of BaseModel, and
        saves it (to the JSON file) and prints the id\n"""
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
        on the class name and id\n"""
        objD = models.storage.all()
        argList = args.split()
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
        """deletes an instance based on the class name and id \n"""
        objD = models.storage.all()
        argList = args.split()
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
        argList = arg.split()
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
        argList = arg.split()
        if len(argList) == 0:
            print("** class name missing **")
        elif argList[0] not in HBNBcommand.__classList:
            print("** class doesn't exist **")
        elif len(argList) < 2:
            print("** instance id missing **")
        elif argList[0] + "." + argList[1] not in objD:
            print("** no instance found **")
        elif len(argList) < 3:
            print("** attribute name missing **")
        elif len(argList) < 4:
            print("** value missing **")
        else:
            for obj in objD.values():
                obj.__dict__[argList[2]] = str(argList[3][1:len(argList[3]) - 1])
                models.storage.save()


if __name__ == '__main__':
    HBNBcommand().cmdloop()
