# Урок 8. Работа с файлами
#
# Задача 38: Дополнить телефонный справочник возможностью
# изменения и удаления данных. Пользователь также может
# ввести имя или фамилию, и Вы должны реализовать
# функционал для изменения и удаления данных
#
def print_records(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split(';'), end='')


def insert_records(file_name: str):
    with open(file_name, 'r+', encoding='utf-8') as data:
        record_id = 0
        for line in data:
            if line != '':
                record_id = line.split(';', 1)[0]
        print('Введите фамилию, имя, отчество, номер телефона через пробел')
        line = f'{int(record_id) + 1};' + ';'.join(input().split()[:4]) + ';\n'
        data.write(line)


def find_char():
    print('Выберите характеристику:')
    print('1 - Фамилия, 2 - Имя, 3 - Отчество, q - Выход')
    char = input()
    while char not in ('1', '2', '3', 'q'):
        print('Введены неверные данные')
        print('Выберите характеристику:')
        print('1 - фамилия, 2 - имя, 3 - отчество, q - выйти')
        char = input()
    if char != 'q':
        inp = input('Введите значение\n')
        return char, inp
    else:
        return 'q', 'q'


def find_records(file_name: str, char, condition):
    if condition != 'q':
        printed = False
        with open(file_name, 'r', encoding='utf-8') as data:
            for line in data:
                if condition == line.split(';')[int(char)]:
                    print(*line.split(';'))
                    printed = True
        if not printed:
            print("Не найдено")
        return printed

path = 'phone.txt'

file = open(path, 'r')

#
# Урок 9. Работа с табличными данными
#
# доработать телефонный справочник в модульном варианте
#
#
# Урок 10. Построение графиков
#
# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца. Ваша задача перевести
# его в one hot вид. Сможете ли вы это сделать без get_dummies?
#
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |
#
