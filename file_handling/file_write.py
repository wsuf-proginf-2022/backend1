my_list = ['test', 'line']

with open('test.txt', 'w') as f:
  for item in my_list:
    f.write(f"{item}\n")

# without with block:
f = open('test.txt', 'w')
for item in my_list:
  f.write(f"1{item}\n")
f.close()

