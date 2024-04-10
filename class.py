class Person: #create class person
    def __init__ (self):
        #ask the user to enter name and age
        self.name = input("Eter your name here:")
        self.age = int(input("Enter youtr age here:"))

    def introduce (self):
        print("Name is:", self.name)
        print("Age is:", self.age)
    #create instace person1 and call th method introduce 
person1 = Person ()
person1.introduce()
