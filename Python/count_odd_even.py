lst = [1, 2, 3, 4, 5, 6]
odd_count = 0
even_count = 0
for num in lst:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Odd: {odd_count}, Even: {even_count}")
