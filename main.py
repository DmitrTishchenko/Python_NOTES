import csv
from turtle import update
import datetime

def add ():
    today = datetime.datetime.today()
    
    
    with open('list.csv', 'a', encoding='utf-8', newline='\n') as file:
        
        file_writer = csv.writer(file, delimiter = ";", lineterminator="\r")
        b = str(input("Нзвание заметки: "))
        c = str(input("Текст заметки: "))
        a = today.strftime("%H:%M:%S %d-%m-%Y")
        file_writer.writerow([a, b, c])
        print('Успешное добавление!')


def show():
    try:
        with open("list.csv", encoding='utf-8') as r_file:
            # Создаем объект reader, указываем символ-разделитель ","
            file_reader = csv.reader(r_file, delimiter = ";")
            # Счетчик для подсчета количества строк и вывода заголовков столбцов
            count = 0
            # Считывание данных из CSV файла
            for row in file_reader:
                if count == -1:
                    # Вывод строки, содержащей заголовки для столбцов
                    print(f'Файл содержит столбцы:\n {"; ".join(row)}')
                else:
                    # Вывод строк
                    print(f' Время создания: {row[0]} Назване: {row[1]} Текст: {row[2]} ')
                count += 1
            print(f'Всего в файле заметок: {count} .')
    except FileNotFoundError:
        print('Нет готового списка дел.')  

def delete():
    str_1 =''
    try: 
        open('list.csv')
        with open('list.csv', 'r', encoding='utf-8', newline='\n') as file:
            file_reader = csv.reader(file)
            text = str(input("Какую задачу удалить: "))
            for row in file_reader:
                if text in ''.join(row):
                    continue
                else:
                    row = ''.join(row)
                    str_1 += row
                    str_1 += '\n'
        with open('new.csv', 'w', encoding='utf-8') as file_new:
            file_new.write(str_1)
        with open('list.csv', 'w', encoding='utf-8', newline='\n') as file:
            file.write(str_1)
        print(f'Задачи содержащие "{text}" удалены.')
    except FileNotFoundError:
            print('Нет готового списка дел.')







def edit():
    today = datetime.datetime.today()
    text = str(input("Какую задачу редактируем: "))
    text_new = str(input("Введите новый текст: "))
    str_1 =''
    try: 
        open('list.csv')
        with open('list.csv', 'r', encoding='utf-8', newline='\n') as file:
            file_reader = csv.reader(file)
            
            for row in file_reader:
                if text in ''.join(row):
                    continue
                else:
                    row = ''.join(row)
                    str_1 += row
                    str_1 += ',\n'
        with open('new.csv', 'w', encoding='utf-8') as file_new:
            file_new.write(str_1)
        with open('list.csv', 'w', encoding='utf-8', newline='\n') as file:
            file.write(str_1)
            file.write(today.strftime("%H:%M:%S %d-%m-%Y") + ';')
            file.write(text +';')
            file.write(text_new)
        print(f'Задача "{text}" отредактированна.')
    except FileNotFoundError:
            print('Нет готового списка дел.')


# add()
# add()
# show()
delete()

# edit()