#!/usr/bin/python3
""" module for the class Base """
import json


class Base:
    """ Base object """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize Base class checking the id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """method to save the list of objects in a file.json """
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                tmp_dict = cls.to_dictionary(obj)
                list_dicts.append(tmp_dict)
            json_L_of_D = cls.to_json_string(list_dicts)
        else:
            json_L_of_D = "[]"

        filename = cls.__name__ + ".json"

        with open(filename, "w") as file:
            num_char = file.write(json_L_of_D)

    @staticmethod
    def to_json_string(list_dictionaries):
        """ method to make the dictionaries in a JSON string representation """
        ret_list = []
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        if type(list_dictionaries) != list:
            ret_list.append(list_dictionaries)
        else:
            ret_list = list_dictionaries
        return json.dumps(ret_list)

    @staticmethod
    def from_json_string(json_string):
        """function that returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if dictionary is not None and len(dictionary) > 0:
            if cls.__name__ == 'Rectangle':
                obj = cls(1, 1)
            if cls.__name__ == 'Square':
                obj = cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """ function that returns a list of instances deserializes in JSON """
        try:
            with open('{}.json'.format(cls.__name__), 'r') as f:
                f_contents = f.read()
                list_objs_dicts = cls.from_json_string(f_contents)
                list_objs = []
                for obj_dict in list_objs_dicts:
                    obj = cls.create(**obj_dict)
                    list_objs += [obj]
                return list_objs
        except ValueError:
            return []
