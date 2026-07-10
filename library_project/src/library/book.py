class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def __str__(self):
        status = "已借出" if self.borrowed else "可借"
        return f"《{self.title}》{self.author} [{status}]"
