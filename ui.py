from logger import input_data, print_data

def interface():
    print('Добрый день, вы попали на специальный бот справочник / n 1 - запись данных / n 2 - вывод данных')
    command = int(input("введите число"))

    while command != 1 and command != 2:
        print ('неправильный ввод')
        command = int(input("введите число"))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()