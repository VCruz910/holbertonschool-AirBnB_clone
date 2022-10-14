#!/usr/bin/python3
"""
Entry point for the
Command Interpreter.
"""

import cmd, json, shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Processor for the Commands.
    """

    intro = 'Welcome to Holberton BnB Command.'
    prompt = '(hbnb)'
    LClass = ['BaseModel', 'User', 'Amenity',
            'Place', 'City', 'State', 'Review']
    LCmd = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, ARG):
        """
        Parses command imputs
        for the console.
        """
        if '.' in ARG and '(' in ARG and ')' in ARG:
            CLS = ARG.split('.')
            CMD = CLS[1].split('(')
            ARGS = CMD[1].split(')')
            if CLS[0] in HBNBCommand.LClass and CMD[0] in HBNBCommand.LCmd:
                ARG = CMD[0] + ' ' + CLS[0] + ' ' + ARGS[0]
        return (ARG)

    def help_help(self):
        """
        Prints the help command description.
        """
        print("Provides description of a given command")

    def emptyline(self):
        """
        Does nothing when the
        line is empty.
        """
        pass

    def do_count(self, NameCLASS):
        """
        Counts number of instances
        of a class.
        """
        COUNT = 0
        ALL_OBJ = storage.all()
        for KEY, VALUE in ALL_OBJ.items():
            CLS = KEY.split('.')
            if CLS[0] == NameCLASS:
                COUNT = COUNT + 1
        print(COUNT)

    def do_create(self, TPModel):
        """
        Creates an instance
        according to a given
        class.
        """

        if not TPModel:
            print("** class name missing **")
        elif TPModel not in HBNBCommand.LClass:
            print("** class doesn't exist **")
        else:
            DICT = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'City': City, 'Amenity': Amenity, 'State': State,
                    'Review': Review}
            MyModel = DICT[TPModel]()
            print(MyModel.id)
            MyModel.save()

    def do_show(self, ARG):
        """
        Shows string representation
        of an instance passed.
        """

        if not ARG:
            print("** class name missing **")
            return

        ARGS = ARG.split(' ')

        if ARGS[0] not in HBNBCommand.LClass:
            print("** class doesn't exist **")
        elif len(ARGS) == 1:
            print("** instance id missing **")
        else:
            ALL_OBJ = storage.all()
            for KEY, VALUE in ALL_OBJ.items():
                OBName = VALUE.__class__.__name__
                OBid = VALUE.id
                if OBName == ARGS[0] and OBid == ARGS[1].strip('"'):
                    print(VALUE)
                    return
            print("** no instance found **")

    def do_destroy(self, ARG):
        """
        Deletes an instance passed.
        """

        if not ARG:
            print("** class name missing **")
            return

        ARGS = ARG.split(' ')

        if ARGS[0] not in HBNBCommand.LClass:
            print("** class doesn't exist **")
        elif len(ARGS) == 1:
            print("** instance id missing **")
        else:
            ALL_OBJ = storage.all()
            for KEY, VALUE in ALL_OBJ.items():
                OBName = VALUE.__class__.__name__
                OBid = VALUE.id
                if OBName == ARGS[0] and OBid == ARGS[1].strip('"'):
                    del VALUE
                    del storage._FileStorage__objects[KEY]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, ARG):
        """
        Prints string represention
        of all instances of a
        given class.
        """

        if not ARG:
            print("** class name missing **")
            return

        ARGS = ARG.split(' ')

        if ARGS[0] not in HBNBCommand.LClass:
            print("** class doesn't exist **")
        else:
            ALL_OBJ = storage.all()
            LInstances = []
            for KEY, VALUE in ALL_OBJ.items():
                OBName = VALUE.__class__.__name__
                if OBName == ARGS[0]:
                    LInstances += [VALUE.__str__()]
            print(LInstances)

    def do_update(self, ARG):
        """
        Updates an instance based
        on the class name and id.
        """

        if not ARG:
            print("** class name missing **")
            return

        A = ""
        for ARGV in ARG.split(','):
            A = A + ARGV

        ARGS = shlex.split(A)

        if ARGS[0] not in HBNBCommand.LClass:
            print("** class doesn't exist **")
        elif len(ARGS) == 1:
            print("** instance id missing **")
        else:
            ALL_OBJ = storage.all()
            for KEY, OBJC in ALL_OBJ.items():
                OBName = OBJC.__class__.__name__
                OBid = OBJC.id
                if OBName == ARGS[0] and OBid == ARGS[1].strip('"'):
                    if len(ARGS) == 2:
                        print("** attribute name missing **")
                    elif len(ARGS) == 3:
                        print("** value missing **")
                    else:
                        setattr(OBJC, ARGS[2], ARGS[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """
        Quit command to exit
        the command interpreter.
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit
        the command interpreter.
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
