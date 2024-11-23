my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]    # вводим список
a = 0                                                     # вводим дополнительную переменную для работы с элементами списка
while True:                                               # записываем цикл
    if my_list[0] > a:                                    # проверяем элемент списка с помощью доп. переменной
        print(my_list[0])
    else:
        break                                             # остановка цикла, если условие ложное
    if my_list[1] > a:
        print(my_list[1])
    else:
        break
    if my_list[2] > a:
        print(my_list[2])
    else:
        break
    if my_list[3] > a:
        print(my_list[3])
    else:
        break
    if my_list[4] > a:
        print(my_list[4])                                   # ноль портит всю малину
        continue                                            # продолжаем цикл, чтобы не останавливать его на нуле
    if my_list[5] > a:
        print(my_list[5])
    else:
        break
    if my_list[6] > a:
        print(my_list[6])
    else:
        break                                               # остановка цикла на первом отрицательном числе из списка
    if my_list[7] > a:
        print(my_list[7])
    else:
        break
    if my_list[8] > a:
        print(my_list[8])
    else:
        break
    if my_list[9] > a:
        print(my_list[9])
    else:
        break
    if my_list[10] > a:
        print(my_list[10])
    else:
        break
    if my_list[11] > a:
        print(my_list[11])
        break
# print((len(my_list)) == my_list[0])