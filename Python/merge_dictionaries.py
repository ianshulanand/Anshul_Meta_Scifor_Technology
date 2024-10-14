dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5}
merged_dict = {}

for d in (dict1, dict2, dict3):
    for key in d:
        merged_dict[key] = d[key]
print(merged_dict)
