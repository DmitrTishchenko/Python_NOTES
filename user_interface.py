import keyboard
import classNote
import checks


def createNote():
    note = editNote()   
    return classNote.Note(title = note[0], body = note[1])


def editNote():
    title = ''
    body = ''
    while len(title)<1:
        
        title = input('Введите ЗАГОЛОВОК заметки: ')
    while len(body)<1:
        
        body = input('\rВведите ОПИСАНИЕ заметки: ')
    return (title, body)


def menu():
    print("\033[H\033[J")
    print('Добро пожаловать в программу "Заметки"\n')
    print("\n1 - для добавления заметки\n2 - для вывода всех заметок\n3 - для удаления заметки\n4 - для редактирования заметки\n5 - для выборки по дате\n6 - показать элемент по id\n7 - для выхода\n")


def continueWork():
    print('Нажмите пробел для продолжения...')
    keyboard.wait('space')

   