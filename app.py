

user_logged_in = False

if user_logged_in == True:
  print('User is logged in')

print('Hello World')

szam = 10
while szam > 0:
  print(f' a szám értéke: {szam}')
  # print('a szám értéke: ' + str(szam))
  # print('a szám értéke: %s' % szam)
  # print('a szám értéke: {}, {}'.format(szam, szam))
  szam -= 1 # szam = szam - 1


def say_hello(name):
  print(f'Hello {name}')

say_hello('John')

for i in range(1, 11):
  print(i)



my_names = ['John', 'Jane', 'Jack', 'Jill']
print(type(my_names))

my_names.append('Joe')
my_names.remove('Jane')
my_names.insert(0, 'Jenny')
my_names.pop()

# error
# print(my_names[20])

print(my_names[-1])


# from time import sleep
# sleep(2)

for name in my_names:
  say_hello(name)

#                 inclusive, exclusive
numbers = list(range(1, 11))

# inclusive : exclusive
print(numbers[4:7])

print(numbers[:7])

print(numbers[4:])

# tuple nem változtatható: immutable
my_tuple = (True, [], 4, 5)


# set: nem lehet két azonos elem
my_set = { 1,3 }
my_set.add(2)
my_set.add(3)
print(my_set)


# dictionary
my_dict = { 'name': 'John', 'age': 30 }
print(my_dict['name'])

my_dict['data'] = [1,2,[3,4], (5, {'name': 'Jane'})]

print(my_dict['data'][2][1])

# type hinting
def add(a: int, b: int) -> int:
  return a + b

def add_2(a: str, b):
  return a.count('a')

print(add_2('aaa', 2))

def say_hello2(name: str, x,y) -> str:
  """
     This function says hello to a person
     @param name: the name of the person
     @returns the hello message
  """
  return f'Hello {name}'

print(say_hello2(name='John', x=2, y=3))
