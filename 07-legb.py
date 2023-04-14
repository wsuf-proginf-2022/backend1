# LEGB rule

# Local
# Enclosing
# Global
# Built-in

# Local
x = 'this is global x'

def report():
  x = 'local'
  print(x)

report()

# Enclosing
def outer():
  x = 'outer x'

  def inner():
    # x = 'inner x'
    print(x)

  inner()
  print(x)

outer()

def outer():
  def inner():
    print(x)
  inner()

outer()

# Built-in
print(__file__)
print(__name__)


def report():
  global x
  x = 'inside'
  print(x)


report()
print(x)
