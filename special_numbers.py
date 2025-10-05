numbers = [5, 12, 18, 21, 33, 42, 50, 77, 90]
special_numbers = []
for i in numbers:
    if int(i) > 20:
        if int(i) % 3 == 0:
            if int(i) % 5 != 0:
                special_numbers.append(i)
print("Special numbers are:", special_numbers)