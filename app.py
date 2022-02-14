numbers = [1, 0, 15, 12, 3, 4]

biggest_number = numbers[0]

for number in numbers:
    if biggest_number < number:
        biggest_number = number

print(biggest_number)
