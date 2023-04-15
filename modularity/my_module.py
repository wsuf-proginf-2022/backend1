

def say_hello():
  print("Hello from my_module.py")

def multiply(a, b):
  return a * b

# print(__name__)


if __name__ == "__main__":
  print('this is the main file')

  say_hello()
  print(multiply(2, 3))
