with open('example.txt', 'r') as file:
    content = file.read()
print(content)

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
k = 0 #демонстрация вхождения в цикл
with open('example.txt', 'r') as f:
    for line in f:
        k += 1
        print(k, line.strip()) #без strip() выводит пробелы

w = input('Введите текст: ')
with open('user_input.txt', 'w', encoding='UTF-8') as f:
    f.write(w)

a = input('Введите текст: ')
with open('user_input.txt', 'a', encoding='UTF-8') as f:
    f.write(a)

try:
    with open('examplо.txt', 'r') as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("Файл не найден.")