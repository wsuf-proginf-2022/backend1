class Animal:
  alive = True

  def __init__(self, age, max_age):
    self.age = age
    self.max_age = max_age

  def eat(self):
    print("Eating")

  def die(self):
    print("Dying")
    Animal.alive = False

  def __str__(self):
    return f"Animal: age={self.age}, max_age={self.max_age}"



my_animal = Animal(10, 100)
my_animal2 = Animal(20, 200)
my_animal.eat()

my_animal.die()
print(my_animal.alive)
print(my_animal2.alive)

class Dog(Animal):
  # overload override: the base class has a method with the same name
  def __init__(self, age, max_age, name):
    super().__init__(age, max_age)
    self.name = name

  def bark(self):
    print("Barking")

  def __str__(self):
    animal_str = super().__str__()
    return f"Dog: {self.name} ({self.age}/{self.max_age}) {animal_str}"

  def __repr__(self):
    return f"Dog"


my_dog = Dog(10, 100, "Rex")
my_dog.eat()
my_dog.bark()

print(my_dog)
print(repr(my_dog))

print(Dog.__bases__)
print(Dog.__subclasses__())
print(Dog.__mro__)


# multiple inheritance
class A:
  def __init__(self):
    print("A")

  def a(self):
    print("a")

class B:
  def __init__(self):
    print("B")

  def b(self):
    print("b")


class C(A, B):
  def __init__(self):
    super().__init__()
    print("C")

  def c(self):
    print("c")

my_c = C()
my_c.a()
my_c.b()
my_c.c()


# object composition

class BookShelf:
  def __init__(self, *books):
    self.books = books

  def __str__(self):
    return f"BookShelf with {len(self.books)} books."


class Book:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"Book {self.name}"

book1 = Book("Harry Potter")
book2 = Book("Lord of the Rings")
my_bookshelf = BookShelf(book1, book2)


class Date:
  def __init__(self, date):
    self.date = date

  def get_date(self):
    return self.date

  @staticmethod
  def to_dash_date(date):
    return date.replace("/", "-")

  @classmethod
  def extra_year(cls, date):
    date_parts = date.get_date().split("-")
    year = date_parts[0]
    month = date_parts[1]
    day = date_parts[2]
    new_date = f"{int(year)+1}-{month}-{day}"
    return cls(new_date)



date = Date("2020-01-01")
print(date.get_date())
print(Date.get_date(date))

extra_year_date = Date.extra_year(date)
print(extra_year_date.get_date())

date_str = "2022/01/01"
my_date2 = Date(Date.to_dash_date(date_str))
print(my_date2.get_date())
