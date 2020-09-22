# Операция следования
def sequence1(a, b):
  return not(a > b)
# Или
def sequence2(a, b):
  return not(a) or b

# Вывод имён переменных для того, чтобы не запутаться
print('x y z w')
# Вложенные циклы с переменными
for x in range(2):
  for y in range(2):
    for z in range(2):
      for w in range(2):
        # Условие из задачи
        if (((x and not(y)) or sequence1(w, z)) == (z == x)) == 1:
          print(x, y, z, w)
