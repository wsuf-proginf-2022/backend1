a = []
b = a


print(id(a))
print(id(b))

a.append(1)
c = a.copy()
print(id(c))

print(a)
print(b)


a = []
b = []

print(id(a))
print(id(b))

a = 23
b = a

print(id(a))
print(id(b))

b = 24
print(id(a))
print(id(b))
print(a, b)

a = 'hello'
b = a

print('id of a:', id(a))
print(id(b))

a += ' world'

print('new a: ', id(a))
print(id(b))

players = [{'name': 'Rolf', 'score': 10}, {'name': 'John', 'score': 20}]
for player in players:
  player['score'] *= 2
  player['name'] = player['name'].upper()

print(players)

# mutable: list, dict, set
# immutable: int, float, bool, str, tuple, frozenset 
