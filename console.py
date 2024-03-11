#!/usr/bin/python3

"""Script containing the entry point of the command interpreter

The commands therein follow the standards set by
    'cmd' python module
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

    # A list of commands that will be executed like:
    #   <class name>.cmd()
    __ad_cmd = [
        "all",
        "count",
        "show",
        "destroy",
        "update",
    ]

    def precmd(self, line):
        cmd_called = ""
        try:
            cmd_called = (
                line.split()[0]
                .split(
                    "(",
                )[0]
                .split(".", 1)[1]
            )
        except IndexError:
            pass
        # First check if that the command is actually in the list
        if cmd_called not in HBNBCommand.__ad_cmd:
            return cmd.Cmd.precmd(self, line)

        # Now reconstruct the arguments to pass on
        new_line = ""

        # First get the className
        class_called = line.split(".")[0]

        # Then get the values in the () to be passed
        values_passed = ""

        new_line = f"{cmd_called} {class_called} {values_passed}"

        return cmd.Cmd.precmd(self, new_line)

    def do_EOF(self, line):
        """Ctrl-D to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_count(self, line):
        """Return the number of instances of a class"""

        from models import storage

        count = 0
        for key, val in storage._FileStorage__objects.items():
            if line == key.split(".")[0]:
                count += 1
        print(count)

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

        my_list_len = len(my_list)

        if my_list_len == 0:
            print("** class name missing **")

        elif my_list_len and my_list[0] not in class_map:
            print("** class doesn't exist **")

        else:
            for class_name in class_map:
                if class_name == my_list[0]:
                    obj = class_map[class_name]()
                    print(obj.id)
                    storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance"""

        from models import storage

        my_list = self.__check(line)

        if my_list != []:
            my_dict = storage.all()

            my_key = f"{my_list[0]}.{my_list[1]}"

            try:
                obj = my_dict[my_key]
                obj_dict = obj.to_dict()
                print(self.handle_print(obj, obj_dict))
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        from models import storage

        my_list = self.__check(line)
        my_dict = storage.all()

        if my_list != []:
            my_key = f"{my_list[0]}.{my_list[1]}"

            try:
                del my_dict[my_key]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        Based or not based on class name"""
        from models import storage

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
        my_dict = storage.all()
        new_list = []

        if len(my_list) == 0:
            for key in my_dict:
                obj_dict = my_dict[key].to_dict()
                print_str = self.handle_print(my_dict[key], obj_dict)
                new_list = [print_str] + new_list
            print(new_list)

        elif len(my_list) == 1:
            if my_list[0] not in class_list:
                print("** class doesn't exist **")
            else:
                for key in my_dict:
                    obj_dict = my_dict[key].to_dict()
                    if obj_dict["__class__"] == my_list[0]:
                        print_str = self.handle_print(my_dict[key], obj_dict)
                        new_list = [print_str] + new_list
                print(new_list)

    def handle_print(self, obj, obj_dict):
        """Handles printing the obj"""
        return f"[{obj_dict['__class__']}] ({obj_dict['id']}) {obj.__dict__}"

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        from models import storage

        my_list = self.__check(line)
        my_dict = storage.all()

        if my_list != []:
            if len(my_list) == 2:
                print("** attribute name missing **")

            elif len(my_list) == 3:
                print("** value missing **")

            else:
                new_list = my_list[:4]

                my_key = f"{new_list[0]}.{new_list[1]}"

                try:
                    obj = my_dict[my_key]
                    obj.__dict__[new_list[2]] = new_list[3]
                    storage.save()
                except KeyError:
                    print("** no instance found **")

    def default(self, line):
        """Handles other commands"""

        import json

        from models import storage

        my_list = line.split('.')
        if my_list[1] == "all()":
            self.do_all(my_list[0])

        elif my_list[1] == "count()":
            count = 0
            my_dict = storage.all()
            for key, value in my_dict.items():
                if value.to_dict()["__class__"] == my_list[0]:
                    count += 1
            print(count)

        elif my_list[1][:4] == "show":
            stop = len(my_list[1]) - 1
            key = my_list[1][5:stop]
            self.do_show(f"{my_list[0]} {key}")

        elif my_list[1][:7] == "destroy":
            stop = len(my_list[1]) - 1
            key = my_list[1][8:stop]
            self.do_destroy(f"{my_list[0]} {key}")

        elif my_list[1][:6] == "update":
            stop = len(my_list[1]) - 1

            values = my_list[1][7:stop]

            new_list = values.split(",")

            len_id = len(new_list[0])

            update_values = values[len_id + 2:stop]

            if update_values[0] != '{':
                str_values = "".join(item for item in new_list)
                self.do_update(f"{my_list[0]} {str_values}")

            elif update_values[0] == '{':
                my_dict = json.loads(update_values.replace("'", '"'))

                for key, value in my_dict.items():
                    print(f"{my_list[0]} {new_list[0]} {key} {value}")
                    self.do_update(f"{my_list[0]} {new_list[0]} {key} {value}")

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
        my_list_len = len(my_list)

        if my_list_len == 0:
            print("** class name missing **")
            return []

        elif my_list_len and my_list[0] not in class_list:
            print("** class doesn't exist **")
            return []

        elif my_list_len == 1:
            print("** instance id missing **")
            return []

        return my_list


if __name__ == "__main__":
    # Ensure that even ctrl+c is handled "correctly"
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        pass
