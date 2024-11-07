def calculate_structure_sum(data_structure):
     for i in data_structure:
         if isinstance(i, str):
             a = len(i)
         if isinstance(i, list):
             for j in i:
                 if isinstance(j, str):
                     b = len(j)
                 if isinstance(j, int):
                     b = sum(i) + len(i)
     return(a + b)


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)