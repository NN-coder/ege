# Выражение из условия
x = 64**10 + 2**90 - 16
# Выражение из условия в нужной системе счисления
x8 = ''

# Переводим число в нужную систему счисления, при необходимости можно вынести в отдельную функцию
while x:
  x8 = str(x % 8) + x8
  x //= 8

# Подсчёт количества искомых цифр
count7 = x8.count('7')
print(count7)
