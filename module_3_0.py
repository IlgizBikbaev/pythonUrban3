def calculate_structure_sum(data_structure):
    s = 0
    s = float(s)
    if isinstance(data_structure, (list, set, tuple)):
        for element in data_structure:
           s+= calculate_structure_sum(element)
    elif isinstance(data_structure, (int, float)):
        s += data_structure
    elif isinstance(data_structure, str):
        s += len(data_structure)
    # elif isinstance(data_structure, dict): # мой старый вариант, но он не учитывает тип данных в ключах и значениях, cумма та же
    #     s += sum(map(len,list(data_structure.keys())))+ sum(list(data_structure.values()))
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            s += calculate_structure_sum(key)
            s += calculate_structure_sum(value)
    return s


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)