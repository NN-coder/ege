# ----------------------------------------------------------------------------------------------------
# Все 4-буквенные слова, составленные из букв М, А, Р, Т, записаны в алфавитном порядке. Вот начало списка:
# 1. АААА
# 2. АААМ
# 3. АААР
# 4. АААТ
# Запишите слово, которое стоит на 250-м месте от начала списка.
# ----------------------------------------------------------------------------------------------------

# Букв 4, из чего делаем вывод, что система счисления - четверичная.
# Исходя из начала списка, сопоставим буквы и цифры: А = 0, М = 1, Р = 2, Т = 3
# Нумерация списка начинается с 1, поэтому в четверичную систему счисления переведём число 250 - 1 = 249
x = 249
x4 = ''
while x:
  x4 = str(x % 4) + x4
  x //= 4
# Выводим полученное число и сопоставляем в нём цифры и буквы, получая искомое слово
print(x4)

# ----------------------------------------------------------------------------------------------------
# Сколько существует различных символьных последовательностей длины 6 в четырёхбуквенном алфавите {М, А, Р, T},
# которые содержат ровно две буквы Р?
# ----------------------------------------------------------------------------------------------------

# Создаём массив из всех букв алфавита
letters = ['М', 'А', 'Р', 'T']

# Функция, проверяющая строку на соответствие критериям из условия задачи
def isValid(s: str):
  if s.count(letters[2]) != 2:
    return False

  return True

count = 0

# n вложенных циклов, где n - длина слов из условия
for l1 in letters:
  for l2 in letters:
    for l3 in letters:
      for l4 in letters:
        for l5 in letters:
          for l6 in letters:
            s = l1 + l2 + l3 + l4 + l5 + l6
            if isValid(s):
              count += 1

print(count)

# ----------------------------------------------------------------------------------------------------
# Тимофей составляет 5-буквенные коды из букв Т, И, М, О, Ф, Е, Й. Буква Й может использоваться в коде
# не более одного раза, при этом она не может стоять на первом месте, на последнем месте и рядом с
# буквой И. Все остальные буквы могут встречаться произвольное количество раз или не встречаться совсем.
# Сколько различных кодов может составить Тимофей?
# ----------------------------------------------------------------------------------------------------

letters = ['Т', 'И', 'М', 'О', 'Ф', 'Е', 'Й']

def isValid(s: str):
  if s.count(letters[-1]) > 1:
    return False

  if s[0] == letters[-1] or s[-1] == letters[-1]:
    return False

  if 'ИЙ' in s or 'ЙИ' in s:
    return False

  return True

count = 0

for l1 in letters:
  for l2 in letters:
    for l3 in letters:
      for l4 in letters:
        for l5 in letters:
          s = l1 + l2 + l3 + l4 + l5
          if isValid(s):
            count += 1

print(count)

# ----------------------------------------------------------------------------------------------------
# Петя составляет 7-буквенные слова из букв А, Б, Р, И, К, О, С. Каждую букву нужно использовать ровно 1
# раз, при этом нельзя ставить подряд две гласные или две согласные. Сколько различных кодов может
# составить Петя?
# ----------------------------------------------------------------------------------------------------

letters = ['А', 'Б', 'Р', 'И', 'К', 'О', 'С']

def isValid(s: str):
  for l in letters:
    if s.count(l) != 1:
      return False

  if 'АИ' in s or 'АО' in s or 'ИА' in s or 'ИО' in s or 'ОА' in s or 'ОИ' in s:
    return False

  if ('БР' in s or 'БК' in s or 'БС' in s or
      'РБ' in s or 'РК' in s or 'РС' in s or
      'КБ' in s or 'КР' in s or 'КС' in s or
      'СБ' in s or 'СР' in s or 'СК' in s):
    return False

  return True

count = 0

for l1 in letters:
  for l2 in letters:
    for l3 in letters:
      for l4 in letters:
        for l5 in letters:
          for l6 in letters:
            for l7 in letters:
              s = l1 + l2 + l3 + l4 + l5 + l6 + l7
              if isValid(s):
                count += 1

print(count)
