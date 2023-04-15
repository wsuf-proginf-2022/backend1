my_list = []

with open('test.txt', 'r') as f:
  for line in f:
    my_list.append(line.strip('\n'))

print(my_list)

# without with block:
f = open('test.txt', 'r')
for line in f:
  my_list.append(line.strip('\n'))
f.close()

print(my_list)
