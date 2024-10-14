lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = []
for num in lst:
    if num not in unique_lst:
        unique_lst.append(num)
print(unique_lst)
