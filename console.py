#!/usr/bin/python3
"""
Script containing the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class inheriting from the cmd.Cmd class

    It contains this methods:
        quit - exits the program
        help - lists all methods contained

    Our cutom prompt is (hbnb)
    """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Ctrl-D to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id"""
        from models import storage
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        my_list = self._split(line)

        class_map = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }

        if len(my_list) < 1:
            print("** class name missing **")
            HBNBCommand().cmdloop()

        if (my_list[0] not in class_map):
            print("** class doesn't exist **")
            HBNBCommand().cmdloop()

        for class_name in class_map:
            if class_name == my_list[0]:
                obj = class_map[class_name]()
                print(obj.id)
                storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance"""

        from models import storage

        my_list = self.__check(line)

        my_dict = storage.all()

        my_key = f"{my_list[0]}.{my_list[1]}"

        try:
            obj = my_dict[my_key]
            obj_dict = obj.to_dict()
            print(
                f"[{obj_dict['__class__']}] ({obj_dict['id']}) {obj.__dict__}"
            )
        except KeyError:
            print("** no instance found **")
            HBNBCommand().cmdloop()

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        from models import storage

        my_list = self.__check(line)
        my_dict = storage.all()

        my_key = f"{my_list[0]}.{my_list[1]}"

        try:
            del my_dict[my_key]
            storage.save()
        except KeyError:
            print("** no instance found **")
            HBNBCommand().cmdloop()

    def do_all(self, line):
        """Prints all string representation of all instances
        Based or not based on class name"""
        from models import storage

        my_list = self._split(line)
        my_dict = storage.all()
        new_list = []

        if my_list == [] and len(my_dict) > 0:
            for key in my_dict:
                obj_dict = my_dict[key].to_dict()
                print_str = self.handle_print(my_dict[key], obj_dict)
                new_list.append(print_str)
            print(new_list)

        elif len(my_list) == 1:
            for key in my_dict:
                obj_dict = my_dict[key].to_dict()
                if (obj_dict["__class__"] == my_list[0]):
                    print_str = self.handle_print(my_dict[key], obj_dict)
                    new_list.append(print_str)
            print(new_list)

    def handle_print(self, obj, obj_dict):
        """Handles printing the obj"""
        return (f"[{obj_dict['__class__']}] ({obj_dict['id']}) {obj.__dict__}")

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        from models import storage

        my_list = self.__check(line)
        my_dict = storage.all()

        if len(my_list) == 2:
            print("** attribute name missing **")
            HBNBCommand().cmdloop()

        elif len(my_list) == 3:
            print("** value missing **")
            HBNBCommand().cmdloop()

        new_list = my_list[:4]

        my_key = f"{new_list[0]}.{new_list[1]}"

        try:
            obj = my_dict[my_key]
            obj.__dict__[new_list[2]] = new_list[3]
            storage.save()
        except KeyError:
            print("** no instance found **")
            HBNBCommand().cmdloop()

    @staticmethod
    def _split(line):
        """splits my line using spaces
        Return a dict"""
        import shlex

        return shlex.split(line)

    def __check(self, line):
        """Performs checks for the use input"""

        class_list = [
            "BaseModel",
            "User",
            "City",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review",
        ]

        my_list = self._split(line)

        if len(my_list) == 0:
            print("** class name missing **")
            HBNBCommand().cmdloop()

        if my_list[0] not in class_list:
            print("** class doesn't exist **")
            HBNBCommand().cmdloop()

        if len(my_list) == 1:
            print("** instance id missing **")
            HBNBCommand().cmdloop()

        return my_list


if __name__ == "__main__":
    HBNBCommand().cmdloop()
