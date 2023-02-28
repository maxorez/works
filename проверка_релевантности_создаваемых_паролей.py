# -*- coding: utf-8 -*-
"""
@author:Max Mikhailichenko
"""
# =============================================================================
# 4.Компания просит вас разработать код для проверки релевантности создаваемых пользователями паролями.
# Пароль может быть задан пользователем, однако к нему есть требования:
# Не может содержать менее 10 символов
# Обязательно содержит одну заглавную букву;
# Все буквы должны быть латинскими;
# В пароле должны содержаться символы @,~,*,(,),’
# Создайте файл csv с учетными данными пользователей (логин, пароль).
# Учетные данные вводите из консоли, проверяйте пароль,
# записывайте в файл нового пользователя в том случае,
# если его пароль соответствует политики компании.
# В противном случае предложите изменить пароль.
# =============================================================================


import os
import csv

# Проверяем наличие файла csv с учетными данными пользователей (логин, пароль)
# Если файла нет, создаем его
def check_userbase():
    check_file = False   # статус проверки наличия файла False - нет, True - есть

    if os.path.isfile('userbase.csv'):
        check_file = True
    else:                # создаем userbase.csv
        with open('userbase.csv', 'w', newline='') as userbase_csv:
            head_file_userbase = ['login', 'password']
            userbase_writer = csv.DictWriter(userbase_csv, fieldnames = head_file_userbase,  delimiter=';')
            userbase_writer.writeheader()
            check_file = True

    return check_file


# Проверка пароля на соответсвтвие политики безопасности компанни
def check_password(login, password):
    success_message = '\nЛогин и пароль успешно созданы'
    user_base = {}
    all_errors = {}
    check_capital_letter = []
    check_symbol = False
    latin = 'absdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbol = "@~*,'"


# проверка длины пароля
    if len(password) < 10:
        all_errors['error_len'] = "Пароль должен содеражть не менее 10 символов"


# проверка заглавных букв
    for f in password:
        if f.isupper():
            check_capital_letter.append(f)

    if len(check_capital_letter) == 0:
            all_errors['error_capital_letter'] = "Обязательно содержит одну заглавную букву"


# проверка латинских букв
    for f in password:
        if f.isalpha() and f not in latin:
            all_errors['error_latin'] = "буквы должны быть латинскими"


#проверяем есть ли символы  @~*,' в пароле
    for f in password:
        if f in symbol:
            check_symbol = True
            break

#если check_symbol false, сообщаем ошибку
    if not check_symbol:
        all_errors['error_symbol'] = "В пароле должны содержаться символы: @ ~ * ,'"


# проверяем, если нет ошибок в словаре all_errors, то заносим данные в словарь user_base
    if len(all_errors) == 0:
        user_base["login"] = login
        user_base["password"] = password
        check_file = check_userbase()   # проверяем наличие файла csv, берем данные из функции check_userbase()
        if check_file == True:          # если есть, то добавляем данные в csv из словаря user_base
            with open('userbase.csv', 'a+', newline='') as userbase_csv:
                userbase_writer = csv.DictWriter(userbase_csv, fieldnames = ['login', 'password'], delimiter=';')
                userbase_writer.writerow(user_base)
        else:
            success_message = 'Ошибка БД, зови админа!'

        return success_message

# если есть ошибки, формируем сообщение и показываем список ошибок
    else:
        list_error = list(all_errors.values())
        print("\nПароль не надежен!!!\n")
        i = 0
        for f in list_error:
            i += 1
            print(f'{i}. {f}')

        return '\nСоздайте новый надежный пароль!!!'


login = input("Придумайте логин: ")
password = input("Придумайте пароль: ")

print(check_password(login, password))

# login = 'max'
# password = 'vb{fDkbxtyrj@'

# print(check_userbase());



