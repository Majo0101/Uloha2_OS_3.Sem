from app import AppLayer


class Terminal:
    __app = AppLayer()

    def __init__(self):
        self.__menu()
        self.__prog_loop()

    def __menu(self):
        print("> m - self.manual")
        print("| f - Format disc")
        print("| w - Write file")
        print("| r - Remove file")
        print("| c - Copy file")
        print("| p - Print file")
        print("| s - Show disc")
        print("| a - Average capacity")
        print("> e - Exit")

    def __switch(self, user_input):
        if user_input == "m":
            self.__menu()
        elif user_input == "f":
            self.__app.format_disc()
        elif user_input == "w":
            self.__app.write_file()
        elif user_input == "r":
            self.__app.remove_file()
        elif user_input == "c":
            self.__app.copy_file()
        elif user_input == "p":
            self.__app.print_file()
        elif user_input == "s":
            self.__app.show_disc()
        elif user_input == "a":
            self.__app.average_capacity()

    def __prog_loop(self):
        user_input = "m"
        def_input = {"m", "f", "w", "r", "c", "p", "s", "a", "e"}

        while user_input != "e":
            user_input = input("<")
            if len(user_input) > 1 or user_input not in def_input:
                print("> Bad choice, you can try read the menu...\n")
                continue
            else:
                self.__switch(user_input)

        print("> Thank you, bye...")

    def __str__(self):
        return "I am the Terminal"
