
info = ""

key = """
    Name : Your Name
    Age : Your Age 
    Location : Your Location
"""

class Person:

    def __init__(self , name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def Name(self):
        User_Name = input("Your Name: ")
        return User_Name

    def Age(self):
        User_Age = input("Your Age: ")
        return User_Age
    
    def Location(self):
        User_Location = input("Your Location: ")
        return User_Location

name = Person.Name("")
age = Person.Age("")
location = Person.Location("")


user = Person(name, age, location)

print("To Find Your Info Type" + key)
print("To Finish Type 'exit' ")

while True:
    if info == "name":
        print(f"Name is" , user.name)
        
    elif info == "age":
        print(f"Age is" , user.age)

    elif info == "location":
        print(f"Location is" , user.location)

    elif info == "exit":
        break

    info = input(">")
    info = info.lower()


