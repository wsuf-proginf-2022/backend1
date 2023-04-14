import time
import functools

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

def my_function():
  num_list = []
  for num in range(1, 100000):
    num_list.append(num)
  print("the sum of all numbers is: {}".format(sum(num_list)))

def timing_function(callback):
  @functools.wraps(callback)
  def wrapper():
    t1 = time.time()
    callback()
    t2 = time.time()
    result = "Time it took to run the function: " + str((t2 - t1)) + " seconds"
    print(result)
  return wrapper

wrapped_function = timing_function(my_function)
wrapped_function()

@timing_function
def my_sum():
  num_list = []
  for num in range(1, 100000):
    num_list.append(num)
  print("the sum of all numbers is: {}".format(sum(num_list)))

my_sum()
print(my_sum.__name__)


x = [1, 2, 3, 4, 5]
out = []
for item in x:
  out.append(item**2)
print(out)

# list comprehension
out = [item**2 for item in x]

users = [('Bob', 42, 'Mechanic'), ('James', 24, 'Artist'), ('Harry', 32, 'Lecturer')]

# dictionary comprehension
user_mapping = { user[0]: user for user in users }

print(user_mapping)

user_mapping2 = {}
for user in users:
  user_mapping2[user[0]] = user

