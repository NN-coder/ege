# Функция "следование", использовать при необходимости по условию
def sequence(A, b):
  return not(A) or b
# Основная функция, получающая дополнительные переменные и возвращающая результат выражения из условия
def F(x, y):
  return (y + 3*x < A) or (2*y + x > 50) or (4*y - x < 40)

# A - основная, искомая переменная
for A in range(1, 1000):
  # Переменная для проверки
  ok = True
  # Вложенные циклы с дополнительными переменными
  for x in range(1, 1000):
    for y in range(1, 1000):
      # Если основная функция возвращает False - присвоить переменной для проверки False и выйти из цикла
      if not(F(x, y)):
        ok = False
        break
  if ok:
    print(A)

# ----------------------------------------------------------------------------------------------------

# Функция "делимость", использовать при необходимости по условию
def Del(n, m):
  return n % m == 0
def sequence(a, b):
  return not(a) or b

def F(x):
  return sequence(not(Del(x, A)), sequence(Del(x, 6), not(Del(x, 9)))) == 1

for A in range(1, 1000):
  ok = True
  for x in range(1, 1000):
    if not(F(x)):
      ok = False
      break
  if ok:
    print(A)

# ----------------------------------------------------------------------------------------------------

def F(x, y):
  return (y - x != 5) or (A < x**3 * 2 + y) or (A < y**2 + 16) == 1

for A in range(1000):
  ok = True
  for x in range(1, 1000):
    for y in range(1, 1000):
      if not(F(x, y)):
        ok = False
        break
  if ok:
    print(A)

# ----------------------------------------------------------------------------------------------------

# Отрезки и функция из условия
A = [n for n in range(70, 90 + 1)]
B = [n for n in range(40, 60 + 1)]
def sequence(a, b):
  return not(a) or b
def F(x):
  return sequence(not(x in A), x in B) and sequence(not(x in C), x in A) == 1

# N - искомая переменная
for N in range(1, 1000):
  ok = False
  # C - отрезок из условия от 0 до N включительно
  C = [n for n in range(N + 1)]
  count = 0
  for x in range(1, 1000):
    if F(x):
      count+=1
    # Условие из задачи
    if count > 30:
      ok = True
      break
  if ok:
    print(N)
    break

# ----------------------------------------------------------------------------------------------------

def sequence(a, b):
  return not(a) or b
# & - побитовая конъюнкция
def F(x):
  return (x & 125 != 1) or sequence(x & 34 == 2, x & a == 0) == 1

for a in range(1, 1000):
  ok = True
  for x in range(1, 1000):
    if not(F(x)):
      ok = False
      break
  if ok:
    print(a)
    break

# ----------------------------------------------------------------------------------------------------

def sequence(a, b):
  return not(a) or b
def F(x):
  return sequence((x & a != 0) and (x & 12 == 0), (x & a == 0) and (x & 21 != 0)) or ((x & 21 == 0) and (x & 12 == 0)) == 1

for a in range(1, 1000):
  ok = True
  for x in range(1, 1000):
    if not(F(x)):
      ok = False
      break
  if ok:
    print(a)
