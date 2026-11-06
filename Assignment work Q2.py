class Book:
  def __init__(self, title, author, price, copies):
    self.title = title
    self.author = author
    self.price = price
    self.copies = copies
  def calculate_stock_value(self)
    return self.price * self.copies
  def check_stock(self):
    if self.copies > 0:
      return "in stock"
    else:
      return "out of stock"
if __name__ == "__main__":
  book1 = Book(title="python Basics", author="john simiyu", price=1200, copies=5)
  book2 = Book(title="Database Systems", author="Mary Mueni", price=2500, copies=0)
  print("---BOOK 1 DETAILS---")
  print(f"Title: {book1.title}")
  print(f"Author: {book1.author}")
  print(f"Stock Value: KSH {book1.calculate_stock_value():,}")
  print(f"Status: {book1.check_stock()})
  print("--- BOOK 2 DETAILS---")
  print(f"Title: {book1.title}")
  print(f"Author: {book2.author}")
  print(f"Stock Value: Ksh {book1.calculate_stock_value():,})
  print(f"Status: {book1.check_stock()}")

  print("---Book 2 Details---")
  print(f"Title: {book2.title}")
  print(f"Author: {book2.author}")
  print(f"Stock Value: Ksh {book2.calculate_stock_value():,})
  print(f"status: {book2.check_stock()}")
