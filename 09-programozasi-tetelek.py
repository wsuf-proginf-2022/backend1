# összegzés

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

osszeg = 0
for i in t:
  osszeg += i 

print(osszeg)

# megszámlálás

t = [ 3, 5, 6, 9 ]
count = 0
for i in t:
  if i > 5:
    count += 1

print(count)

# eldöntés
n = len(t)
keresett = 5
i = 0
while i < n and t[i] != keresett:
  i += 1

if i < n:
  print('Van benne')
else:
  print('Nincs benne')


# kiválasztás
n = len(t)
i = 0
while i < n and t[i] != keresett:
  i += 1

if i < n:
  print(f'A keresett elem indexe: {i}')
else:
  print('Nincs benne')


# lineáris keresés
n = len(t)
i = 0
while i < n and t[i] != keresett:
  i += 1

if i < n:
  print(f'A keresett elem indexe: {i}')
  print(f'Értéke: {t[i]}')
else:
  print('Nincs benne')

# maximum kiválasztás
n = len(t)
max = t[0]
for i in range(1, n):
  if t[i] > max:
    max = t[i]

max_index = 0
max = t[0]
for i, elem in enumerate(t):
  if elem > max:
    max = elem
    max_index = i

print(max_index)
print(max)

t = [ 9, 6, 5, 3 ]
print(t)
# buborék rendezés
n = len(t)
for i in range(n - 1):
  for j in range(n - i - 1):
    if t[j] > t[j + 1]:
      t[j], t[j + 1] = t[j + 1], t[j]

print(t)

t = [ 9, 6, 5, 3 ]
print(t)
# minimum kiválasztásos rendezés
n = len(t)
for i in range(n - 1):
  min_index = i
  for j in range(i + 1, n):
    if t[j] < t[min_index]:
      min_index = j
  t[i], t[min_index] = t[min_index], t[i]

print(t)

# bináris keresés
t = [ 3, 5, 6, 9 ]
keresett = 5
n = len(t)
i = 0
j = n - 1
while i <= j:
  kozep = (i + j) // 2
  if keresett == t[kozep]:
    print(f'A keresett elem indexe: {kozep}')
    break
  elif keresett < t[kozep]:
    j = kozep - 1

# quicksort
t = [ 3, 5, 6, 9 ]
print(t)
def quicksort(t):
  if len(t) <= 1:
    return t
  else:
    pivot = t[0]
    smaller = [x for x in t[1:] if x <= pivot]
    bigger = [x for x in t[1:] if x > pivot]
    return quicksort(smaller) + [pivot] + quicksort(bigger)


print(quicksort(t))
