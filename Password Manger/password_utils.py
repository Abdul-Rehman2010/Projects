password = []

class Passwords:
    def add(self):
        password_for = input("\n \nThe Password Is For: ")
        new_password = input("\n \nEnter New Password: ")
        password.append("Password for " + password_for + " is " + new_password)


    def veiw(self):
        for i in password:
            print(i, "\n")
   

