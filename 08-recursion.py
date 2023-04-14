
def my_func():
  my_func()

# my_func()

def fakt(n):
  if n == 1:
    return 1
  return n * fakt(n - 1)
  # return 5 * fakt(4)
  # return 5 * 4 * fakt(3)
  # return 5 * 4 * 3 * fakt(2)
  # return 5 * 4 * 3 * 2 * fakt(1)
  # return 5 * 4 * 3 * 2 * 1


print(fakt(5))
