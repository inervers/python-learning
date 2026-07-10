from src.library.library import Library

lib = Library()
lib.add_book("三体", "刘慈欣")
lib.add_book("百年孤独", "马尔克斯")
lib.borrow_book("三体")
lib.show_all()
