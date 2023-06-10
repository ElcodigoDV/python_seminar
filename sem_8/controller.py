import view
import model


actions = {'1': 'список',
        '2': 'запись',
        '3': 'поиск',
        '4': 'изменение',
        '5': 'удаление',
        'q': 'выход'}


while actions != 'q':
    print('Какое действие хотите совершить?',
          *[f'{i} - {actions[i]}' for i in actions])
    action = input()
    while action not in actions:
        print('Какое действие хотите совершить?',
              *[f'{i} - {actions[i]}' for i in actions])
        action = input()
        if action not in actions:
            print('Введены неверные данные')
    if action != 'q':
        if action == '1':
            view.print_records(model.path)
        elif action == '2':
            model.insert_records(model.path)
        elif action == '3':
            model.find_records(model.path, *model.find_char())
        elif action == '4':
            model.change_records(model.path)
        elif action == '5':
            model.delete_records(model.path)