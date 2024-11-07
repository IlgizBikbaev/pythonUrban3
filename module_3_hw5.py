def get_multiplied_digits(number):
    number = int(number)
    str_number = str(number)
    first = int(str_number[0])
    str_number = str_number.replace('0', "")

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

number_enter = input('Введите целое положительное число: ')
result = get_multiplied_digits(number_enter)
print('Результат умножения ваших чисел', result)