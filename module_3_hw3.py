def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(a=2)
print_params(a=3, b="Письма")
print_params(a=1, b='письмо', c='отправлено')

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [12, 'Писем', False]
print_params(*values_list)

values_dict = {'a': 'Друг', 'b': 12, 'c': 'messages'}
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)