lst = [1, 2, 3, 4, 5]
unique = True
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            unique = False
            break
print(unique)
