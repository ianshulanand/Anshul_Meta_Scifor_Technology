lst = [1, 4, 9, 16]
max_diff = 0
for i in range(1, len(lst)):
    diff = abs(lst[i] - lst[i-1])
    if diff > max_diff:
        max_diff = diff
print(max_diff)
