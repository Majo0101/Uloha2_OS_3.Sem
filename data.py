class Node:
    def __init__(self, in_order):
        self.__file_name = "--------"
        self.__in_order = in_order

    def __str__(self):
        return "I am Node"


class DataBlock:
    def __init__(self):
        self.__used_block = False
        self.__data_block = "----------------"

    def get_used_block(self):
        return self.__used_block

    def set_used_block(self, x):
        self.__used_block = x

    def get_data_block(self):
        return self.__data_block

    def set_data_block(self, x):
        self.__data_block = x

    in_use = property(get_used_block, set_used_block)
    io_data = property(get_data_block, set_data_block)

    def __str__(self):
        return "I am a Data block"
