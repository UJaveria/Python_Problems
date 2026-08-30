# Add a bark() method to Dog that prints "{name} says Woof!"
class Dog :
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def details(self) :
        print(f"Name : {self.name}\nBreed : {self.breed}")

    def bark(self) :
        print(f"{self.name} says woof!")

dog1 = Dog("Charlie ", "Golden Retriever")
dog2 = Dog("Max" , "German Shepherd")
print("----dog1----")
dog1.details()
print("----dog2----")
dog2.details()
dog2.bark()