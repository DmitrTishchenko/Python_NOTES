from colorama import Fore, Style
import logic
import user_interface
import checks



def start():
    userInput ='0'
    while userInput != '7':
        user_interface.menu() 
        userInput =input('Введите номер задачи: ').strip()
        print("\n")
        if userInput == '2':
           logic.show()
           user_interface.continueWork()
        if userInput == '1':
            note =user_interface.createNote()
            logic.add(note)
            user_interface.continueWork()
        if userInput == '3':
            logic.show()
            print("\n")
            logic.delete(input("Введите id заметки: "))
            user_interface.continueWork()
        if userInput == '4':
            logic.show()
            print("\n")
            userInput = input("Введите id заметки: ")
            if checks.checkInList(userInput):
                editNote = user_interface.editNote()
                logic.edit(userInput, editNote[0], editNote[1])
            else:
                print(Fore.RED + 'Такой заметки нет. Возможно вы ввели неверный id')
                print(Style.RESET_ALL)  
            user_interface.continueWork()        
        if userInput == '5':
            logic.showByDate(input('Введите дату в формате dd.mm.yyyy: '))
            print('\n')
            user_interface.continueWork()
        if userInput == '6':
            logic.show()
            print("\n")
            logic.showById(input("Введите id заметки: "))
            user_interface.continueWork()
        if userInput == '7':
            print("Спасибо что выбрали наше приложение, до новых встреч!")
            break