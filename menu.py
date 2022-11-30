class Terminal:
    def __init__(self):
        self.__menu()
        self.__prog_loop()

    def __menu(self):
        print("m - manual")
        print("f - Format disc")
        print("w - Write file")
        print("r - Remove file")
        print("c - Copy file")
        print("s - Show disc")
        print("a - Average capacity")
        print("e - Exit\n")

    def __switch(self, user_input):
        if user_input == "m":
            print("m")
        elif user_input == "f":
            print("f")
        elif user_input == "w":
            print("w")
        elif user_input == "r":
            print("r")
        elif user_input == "c":
            print("c")
        elif user_input == "s":
            print("s")
        elif user_input == "a":
            print("a")

    def __prog_loop(self):
        user_input = "m"
        def_input = {"m", "f", "w", "r", "c", "s", "a", "e"}

        while user_input != "e":
            user_input = input("> ")
            if len(user_input) > 1 or user_input not in def_input:
                print("> Bad choice, you can try read the menu...\n")
                continue
            else:
                self.__switch(user_input)

        print("Thank you, bye...")
