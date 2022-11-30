class Node:
    def __init__(self, in_order):
        self.__file_name = "--------"
        self.__in_order = in_order
        self.__bin = False
        self.__address_data = []

    def get_file_name(self):
        return self.__file_name

    def set_file_name(self, x):
        self.__file_name = x

    def get_in_order(self):
        return self.__in_order

    def set_in_order(self, x):
        self.__in_order = x

    def get_bin(self):
        return self.__bin

    def set_bin(self, x):
        self.__bin = x

    def get_address_data(self):
        return self.__address_data

    def set_address_data(self, x):
        self.__address_data.append(x)

    def del_address_data(self):
        self.__address_data.clear()

    node_name = property(get_file_name, set_file_name)
    node_order = property(get_in_order, set_in_order)
    node_bin = property(get_bin, set_bin)
    node_register = property(get_address_data, set_address_data, del_address_data)

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

    data_use = property(get_used_block, set_used_block)
    data_data = property(get_data_block, set_data_block)

    def __str__(self):
        return "I am a Data block"
