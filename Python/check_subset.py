lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4, 5]
is_subset = True
for num in lst1:
    if num not in lst2:
        is_subset = False
        break
print(is_subset)
