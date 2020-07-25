import json


class Parser:
    def __init__(self, filename):
        self.__filename = filename
        self.__json_data = self.__load_data()

    def __load_data(self):
        f = open(self.__filename)
        return json.load(f)

    def get_data(self):
        return self.__json_data
