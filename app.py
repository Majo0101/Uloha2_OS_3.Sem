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
        print("> Disk was successfully formatted...")

    def service_data_controller(self, data):
        __tmp_data = "----------------"
        __tmp_stack = []
        __tmp = data
        for index in self.__data:
            if not index.data_use:
                if len(__tmp) <= 16:
                    index.data_data = __tmp + __tmp_data[len(__tmp):]
                    index.data_use = True
                    __tmp_stack.append(index.data_order)
                    break
                else:
                    index.data_data = __tmp[0:16]
                    index.data_use = True
                    __tmp = __tmp[16:]
                    __tmp_stack.append(index.data_order)
        return __tmp_stack

    def service_write_file(self, name, data):
        __tmp = "--------"
        for index in self.__nodes:
            if not index.node_use:
                index.node_name = name + __tmp[len(name):]
                index.node_use = True
                index.node_register = self.service_data_controller(data)
                break

    def service_check_capacity(self, x):
        __free = 0
        for index in self.__data:
            if not index.data_use:
                __free += 16
        if __free - len(x) > 0:
            return
        else:
            return -1

    def service_check_nodes(self):
        __free_nodes = 5
        for index in self.__nodes:
            if index.node_use:
                __free_nodes -= 1
        return __free_nodes

    def service_show_disc(self):
        for index in self.__nodes:
            if index.node_bin:
                print("> Node: " + str(index.node_order) + "     Bin")
            else:
                print("> Node: " + str(index.node_order))
            print("> Node name: " + index.node_name)
            print("> Assigned blocks: " + str(index.node_register) + "\n")
        for index in self.__data:
            print("> Data block: " + str(index.data_order))
            print("> Data in block: " + index.data_data)
            if index.data_use:
                print("> In use\n")
            else:
                print("> Free\n")

    def service_search_file(self, x):
        tmp = ""
        for index in self.__nodes:
            if index.node_name[0:len(x)] == x and not index.node_bin:
                print("> " + index.node_name.translate(str.maketrans('', '', '-')))
                for obj in self.__data:
                    if obj.data_order in index.node_register:
                        tmp += obj.data_data
                print("> " + tmp.translate(str.maketrans('', '', '-')))
                return tmp
        return -1

    def service_average_capacity(self):
        __free_bytes = 0
        __free_blocks = 0
        for index in self.__data:
            if not index.data_use:
                __free_blocks += 1
            for character in index.data_data:
                if character == "-":
                    __free_bytes += 1
        print("> Free bytes: " + str(__free_bytes) + "/160")
        print("> Free blocks: " + str(__free_blocks) + "/10")

    def service_bin_search(self, x):
        for index in self.__nodes:
            if index.node_name[0:len(x)] == x:
                return 0
        return -1

    def service_show_bin(self):
        for index in self.__nodes:
            if index.node_bin:
                print(">->" + index.node_name.translate(str.maketrans('', '', '-')))
        print(">->")

    def service_add_to_bin(self, x):
        for index in self.__nodes:
            if index.node_name[0:len(x)] == x:
                index.node_bin = True
                print(">-> File was successfully moved to bin")
                break

    def service_remove_forever(self, x):
        for index in self.__nodes:
            if index.node_name[0:len(x)] == x:
                index.node_bin = False
                index.node_name = "--------"
                index.node_use = False
                for num in index.node_register:
                    for block in self.__data:
                        if block.data_order == num:
                            block.data_data = "----------------"
                            block.data_use = False
                index.node_register.clear()
                print(">-> File was successfully removed")
                break
            else:
                print("Error Bin")

    def __str__(self):
        return "I am the Service layer"


class AppLayer:
    __interface = Services(5, 10)

    def __init__(self):
        pass

    def format_disc(self):
        self.__interface.service_format_disc()

    def write_file(self):
        print("> Write file <")
        __file_name = input("> Enter a file name:\n<")
        if len(__file_name) > 8:
            print("> Allowed are a names less than 8 characters")
        else:
            __file_data = input("> Enter a file data:\n<")
            if self.__interface.service_check_capacity(__file_data) != -1:
                if self.__interface.service_search_file(__file_name) == -1:
                    if self.__interface.service_check_nodes() != 0:
                        self.__interface.service_write_file(__file_name, __file_data)
                    else:
                        print("> No empty Nodes")
                else:
                    print("> File is already exist.")
            else:
                print("> Entered data are bigger than disk free capacity")

    def remove_file(self):
        print("> Remove file <")
        __file_name = input("> Enter a file name:\n<")
        if self.__interface.service_search_file(__file_name) != -1:
            __file_remove = input("Do you want to continue? (y/n) \n<")
            if __file_remove == "Y" or __file_remove == "y":
                self.__interface.service_remove_forever(__file_name)
        else:
            print("> File not found")

    def copy_file(self):
        print("> Copy file <")
        __file_name = input("> Enter a file name:\n<")
        if self.__interface.service_search_file(__file_name) == -1:
            print("> File not found")
        else:
            __newfile_name = input("> This data will be copied...\n> Enter new file name: \n<")
            if self.__interface.service_search_file(__newfile_name) != -1 or self.__interface.service_check_nodes() == 0:
                print("Error during copying...")
            else:
                tmp = self.__interface.service_search_file(__file_name)
                if self.__interface.service_check_capacity(tmp) != -1:
                    print(">>> Will be copied to " + __newfile_name)
                    self.__interface.service_write_file(__newfile_name, tmp)
                else:
                    print("> Entered data are bigger than disk free capacity")

    def print_file(self):
        print("> Print file <")
        __file_name = input("> Enter a file name:\n<")
        if self.__interface.service_search_file(__file_name) == -1:
            print("> File not found")

    def show_disc(self):
        self.__interface.service_show_disc()

    def average_capacity(self):
        self.__interface.service_average_capacity()

    def bin_options(self):
        print(">-> r - Remove file from bin")
        print(">-> s - Show files in bin")
        print(">-> a - Add file to bin")
        __bin_choice = input("<-<")
        if __bin_choice == "r" or __bin_choice == "R":
            __file_namer = input(">-> Enter a file name:\n<-<")
            if self.__interface.service_bin_search(__file_namer) != -1:
                self.__interface.service_remove_forever(__file_namer)
            else:
                print(">-> File not found")
        elif __bin_choice == "s" or __bin_choice == "S":
            self.__interface.service_show_bin()
        elif __bin_choice == "a" or __bin_choice == "A":
            __file_name = input(">-> Enter a file name:\n<-<")
            if self.__interface.service_search_file(__file_name) != -1:
                self.__interface.service_add_to_bin(__file_name)
            else:
                print(">-> File not found")
        else:
            print(">-> Bad input")

    def __str__(self):
        return "I am the Application layer"
