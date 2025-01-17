class BookStore:
    NoofBooks = 0
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoofBooks += 1
    def Display(self):
        print(f"book name is : {self.Name}, Author is : {self.Author},No of Books : {BookStore.NoofBooks}")
A=BookStore("My Book","joel")
A.Display()