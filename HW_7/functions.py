# Вывод из файла в консоль
def from_file(file):
    with open(file, 'r', encoding='utf-8') as data:
        dictionary = data.read()
    return dictionary

# Запись в файл
def get_info():
    info = []
    sur_name = input('Введите фамилию: ')
    info.append(sur_name)
    name = input('Введите имя: ')
    info.append(name)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info

def writing_spiskom(info):
    file = 'C:\\Users\\fatim\\Desktop\\PY_HW\\HW_7\\Contacts_Form1.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')
        
def writing_stroka(info):
    file = 'C:\\Users\\fatim\\Desktop\\PY_HW\\HW_7\\Contacts_Form2.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')        
