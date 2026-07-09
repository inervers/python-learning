class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def __str__(self):
        status = "已借出" if self.borrowed else "可借"
        return f"《{self.title}》{self.author} [{status}]"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        self.books[title] = Book(title, author)
        print(f"添加成功：{self.books[title]}")

    def borrow_book(self, title):
        if title not in self.books:
            print("查无此书")
            return
        book = self.books[title]
        if book.borrowed:
            print(f"《{title}》已被借出")
        else:
            book.borrowed = True
            print(f"借出成功：{book}")

    def return_book(self, title):
        if title not in self.books:
            print("查无此书")
            return
        book = self.books[title]
        if not book.borrowed:
            print(f"《{title}》未被借出，无需归还")
        else:
            book.borrowed = False
            print(f"还书成功：{book}")

    def search(self, keyword):
        results = [book for book in self.books.values()
                   if keyword in book.title or keyword in book.author]
        if not results:
            print(f"未找到包含「{keyword}」的书")
        else:
            for book in results:
                print(book)

    def show_all(self):
        if not self.books:
            print("图书馆为空")
        else:
            for book in self.books.values():
                print(book)


if __name__ == "__main__":
    lib = Library()
    lib.add_book("三体", "刘慈欣")
    lib.add_book("百年孤独", "马尔克斯")
    lib.add_book("1984", "乔治·奥威尔")
    lib.show_all()
    print("---")
    lib.borrow_book("三体")
    lib.borrow_book("三体")
    lib.return_book("三体")
    print("---")
    lib.search("体")
