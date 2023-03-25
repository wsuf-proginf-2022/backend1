
def my_first_function():
  pass

# add_user()

# pass by reference
def add_user(users, new_user):
  users.append(new_user)

users: list = []

add_user(users, "user1")
print(users)

# pass by value
def set_name(name, new_name):
  name = new_name

name: str = "Peter"
set_name(name, "John")
print(name)

vehicle: str = "car"

def drive():
  global vehicle
  vehicle = vehicle.upper()
  print(vehicle)

drive()


def divide(dividend, divisor=2):
  if divisor == 0:
    return None
  return dividend / divisor

result = divide(10, 5)
print(result)
result = divide(10)


seq = [1, 2, 3, 4, 5]

# anonymous function: lambda
times2 = map(lambda x: x * 2, seq)
print(list(times2))

filtered_list = filter(lambda x: x % 2 == 0, seq)
print(list(filtered_list))

# rest parameter *args
def multiply(*args):
  result = 1
  print(type(args))
  for arg in args:
    result *= arg
  return result

print(multiply(1, 2, 3, 4, 5))

my_nums = [1, 2, 3, 4, 5]

# unpacking (spread operator)
print(multiply(*my_nums))

# keyword arguments
def print_user(person, **kwargs):
  print(person)
  print(type(kwargs))
  for key, value in kwargs.items():
    print(f"{key}: {value}")

print_user('the person', name="Peter", age=30, city="Berlin")
