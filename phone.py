def choose_action(phone_book):
    while True:
        print('Телефонный справочник открыт. Выберите пункт меню:')
        user_choice = input('1 - Добавить контакт\n2 - Найти контакт\n3 - Изменить контакт\n4 - Удалить контакт\n5 - Просмотреть все контакты\n0 - Выйти из справочника\n')
        print()
        if user_choice == '1':
            add_phone_number(phone_book)
        elif user_choice == '2':
            contact_list = read_file_to_dict(phone_book)
            find_number(contact_list)
        elif user_choice == '3':
            change_phone_number(phone_book)
        elif user_choice == '4':
            delete_contact(phone_book)
        elif user_choice == '5':
            show_phone_book(phone_book)
        elif user_choice == '0':
            print('Справочник закрыт')
            
            break
        else:
            print('Введено некорректно число! \n')
            print()
            continue

def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Имя', 'Фамилия', 'Номер телефона', 'Адрес']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list

def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list

def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - По имени\n2 - По фамилии\n3 - По номеру телефона\n4 - По адресу\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите номер телефона для поиска: ')
        print()
    elif search_field == '4':
        search_value = input('Введите адрес для поиска: ')
        print()    
    return search_field, search_value

def find_number(contact_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Имя', '2': 'Фамилия', '3': 'Номер телефона', '4': 'Адрес'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()

def get_new_number():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone_data = input('Введите номер телефона: ')
    address_data = input('Введите адрес: ')
    return name, surname, phone_data, address_data

def add_phone_number(file_name):
    info = ' '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')
    print('Контакт добавлен в справочник! \n')

def show_phone_book(file_name):
    list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Имя'])
    print_contacts(list_of_contacts)
    # print()
    print('Контакты справочника \n')
    return list_of_contacts

def search_to_modify(contact_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден \n')
        
    print()

def change_phone_number(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Имя\n2 - Фамилия\n3 - Номер телефона\n4 - Адрес\n')
    if field == '1':
        number_to_change[0] = input('Введите имя: ')
    elif field == '2':
        number_to_change[1] = input('Введите фамилию: ')
    elif field == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    elif field == '4':
        number_to_change[3] = input('Введите адрес: ')
    contact_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)
    print('Контакт изменен! \n')

def delete_contact(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)
    print('Контакт удален! \n')

def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()

if __name__ == '__main__':
    file = 'data_phone.csv'
    choose_action(file)

