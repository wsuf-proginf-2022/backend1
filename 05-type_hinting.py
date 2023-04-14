from typing import List

def list_avg(sequence: List) -> float:
  return sum(sequence) / len(sequence)

print(list_avg([1, 2, 3, 4, 5]))

class Book:
  pass

def avg_price(sequence: List[Book]):
  pass

class BookShelf:
  def __init__(self, books: List[Book]):
    self.books = books

myShelf = BookShelf(2)
