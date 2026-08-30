"""Create a Dog class with __init__ setting name and breed. Make two objects; print each one's
details."""

class Dog :
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def details(self) :
        print(f"Name : {self.name}\nBreed : {self.breed}")

dog1 = Dog("Charlie ", "Golden Retriever")
dog2 = Dog("Max" , "German Shepherd")
print("----dog1----")
dog1.details()
print("----dog2----")
dog2.details()