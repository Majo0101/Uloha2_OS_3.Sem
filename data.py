class Node:
    def __init__(self, x):
        self.__used_node = False
        self.__file_name = "--------"
        self.__in_order = x
        self.__bin = False
        self.__address_data = []

    def get_used_node(self):
        return self.__used_node

    def set_used_node(self, x):
        self.__used_node = x

    def get_file_name(self):
        return self.__file_name

    def set_file_name(self, x):
        self.__file_name = x

    def get_in_order(self):
        return self.__in_order

    def get_bin(self):
        return self.__bin

    def set_bin(self, x):
        self.__bin = x

    def get_address_data(self):
        return self.__address_data

    def set_address_data(self, x):
        self.__address_data.extend(x)

    def del_address_data(self):
        self.__address_data.clear()

    node_use = property(get_used_node, set_used_node)
    node_name = property(get_file_name, set_file_name)
    node_order = property(get_in_order)
    node_bin = property(get_bin, set_bin)
    node_register = property(get_address_data, set_address_data)

    def __str__(self):
        return "I am Node " + str(self.__in_order)


class DataBlock:
    def __init__(self, x):
        self.__used_block = False
        self.__data_block = "----------------"
        self.__in_order = x

    def get_used_block(self):
        return self.__used_block

    def set_used_block(self, x):
        self.__used_block = x

    def get_data_block(self):
        return self.__data_block

    def set_data_block(self, x):
        self.__data_block = x

    def get_in_order(self):
        return self.__in_order

    data_use = property(get_used_block, set_used_block)
    data_data = property(get_data_block, set_data_block)
    data_order = property(get_in_order)

    def __str__(self):
        return "I am a Data block " + str(self.__in_order)
