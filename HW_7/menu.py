from os.path import exists
from functions import writing_stroka, writing_spiskom, get_info,  from_file


def view():
    # path1 = 
    print(from_file('C:\\Users\\fatim\\Desktop\\PY_HW\\HW_7\\Contacts_Form1.txt'))


def record_info():
    info = get_info()
    writing_stroka(info)
    writing_spiskom(info)


def choice():
    flag = input('Для продолжения работы нажмите \'да\', или любой символ для завершения работы... ')
    while (flag.lower() == 'да'):
        path = 'C:\\Users\\fatim\\Desktop\\PY_HW\\HW_7\\Contacts_Form2.txt'
        valid = exists(path)
        choice_action = input('Введите \'да\', если хотите записать новые данные, и любой другой символ, если хотите просмотреть справочник в консоли: ')
        if choice_action.lower() == 'да':
            record_info()
        else:
            view()
        flag = input('Для продолжения работы нажмите \'да\', или любой символ для завершения работы... ')
    print('Программа завершена.')