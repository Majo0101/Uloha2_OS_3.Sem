from data import Node
from data import DataBlock


class Services:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.__nodes = []
        self.__data = []
        for index in range(i):
            self.__nodes.append(Node(index))
        for index in range(j):
            self.__data.append(DataBlock(index))

    def service_format_disc(self):
        for index in self.__data:
            index.data_data = "----------------"
        for index in self.__nodes:
            index.node_name = "--------"
            index.del_address_data()
        print("Disk was successfully formatted...")


class AppLayer:
    __interface = Services(5, 10)

    def __init__(self):
        pass

    def format_disc(self):
        self.__interface.service_format_disc()

    def write_file(self):
        print("Write file")

    def remove_file(self):
        print("Remove file")

    def copy_file(self):
        print("Copy file")

    def show_disc(self):
        print("Show disc")

    def average_capacity(self):
        print("Average capacity")

    def __str__(self):
        return "I am Application Layer"
