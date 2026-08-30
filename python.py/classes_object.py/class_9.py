# Create Library holding a list of titles. Add add_book, remove_book, find_book(keyword).
class Library :
    def __init__(self,titles):
        self.titles  = titles

    def add_book(self,name) :
        self.titles.append(name)
        return (self.titles)

    def remove_book(self) :
        name = input("Enter book name you want to remove : ").lower()
        if name not in self.titles :
            return "not found"
        else : 
            for book in self.titles :
                if book == name :
                    self.titles.remove(name)
                    print("Remove Successfully!")
                    return self.titles

    def find_book(self ,keyword) :
        keyword = input("Enter book name you want to search : ").lower()
        if keyword not in self.titles :
            return "not found"
        else : 
            return "found"

        

books = [
    "Python Crash Course",
    "Think Python",
    "Effective Python",
    "Python for Data Analysis",
    "Hands-On Machine Learning",
    "Clean Code"
]
my_books = []
for book in books :
    my_books.append(book.lower())

l1 = Library(my_books)
print(l1.add_book("Geophysics".lower()))
print(l1.titles)
print(my_books)
print(l1.remove_book())
print(l1.find_book("clea code"))