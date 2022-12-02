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
            index.data_use = False
        for index in self.__nodes:
            index.node_name = "--------"
            index.node_bin = False
            index.node_use = False
            index.del_address_data()
        print("Disk was successfully formatted...")

    def service_show_disc(self):
        for index in self.__nodes:
            print("Node: " + str(index.node_order))
            print("Node name: " + index.node_name)
            print("Assigned blocks: " + str(index.node_register) + "\n")
        for index in self.__data:
            print("Data block: " + str(index.data_order))
            print("Data in block: " + index.data_data)
            if index.data_use:
                print("In use")
            else:
                print("Free\n")

    def service_average_capacity(self):
        __free_bytes = 0
        __free_blocks = 0
        for index in self.__data:
            if not index.data_use:
                __free_blocks += 1
            for character in index.data_data:
                if character == "-":
                    __free_bytes += 1
        print("Free bytes: " + str(__free_bytes) + "/160")
        print("Free blocks: " + str(__free_blocks) + "/10")

    def __str__(self):
        return "I am the Service layer"


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
        self.__interface.service_show_disc()

    def average_capacity(self):
        self.__interface.service_average_capacity()

    def __str__(self):
        return "I am the Application layer"
