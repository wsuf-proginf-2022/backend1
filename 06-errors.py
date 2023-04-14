

def divide(a, b):
  if b == 0:
    raise ZeroDivisionError('b cannot be 0.')
  return a / b

# print(divide(10, 0))
grades = []
# grades = [23, 45, 67, 89, 90, 100]
print("welcome to the average grade program.")
try:
  average = divide(sum(grades), len(grades))
  print(f"the average grade is {average}")
except ZeroDivisionError as e:
  print(e)
  print("there are no grades yet in your list.")
finally:
  print("thank you!")


print("code executed.")
