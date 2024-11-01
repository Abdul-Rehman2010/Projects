# ____
# |  O
# | /|\
# | / \


class hang_man:
    def __init__(self):
        self.shared_var = "_____ \n" 

    def man1(self):
        self.shared_var = f"{self.shared_var}|   O"
        print(self.shared_var, "\n")
        return self.shared_var

    def man2(self):
        self.shared_var = f"{self.shared_var} \n|  /"
        print(self.shared_var, "\n")
        print()
        return self.shared_var

    def man3(self):
        self.shared_var = f"{self.shared_var}|"
        print(self.shared_var, "\n")
        print()
        return self.shared_var

    def man4(self):
        self.shared_var = f"{self.shared_var}\ \n"
        print(self.shared_var, "\n")
        return self.shared_var

    def man5(self):
        self.shared_var = f"{self.shared_var}|  / "
        print(self.shared_var, "\n")
        return self.shared_var

    def man6(self):
        self.shared_var = f"{self.shared_var}\ "
        print(self.shared_var, "\n")
        return self.shared_var
