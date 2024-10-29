calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    str_first = str(string)
    str_tuple = (len(str_first), str_first.upper(), str_first.lower())
    count_calls()
    return str_tuple

def is_contains(string, list_to_search):
    string = str(string).upper()
    new_list = [i.upper() for i in list_to_search]
    count_calls()
    if string in new_list:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)