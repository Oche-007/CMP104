#  5. Generate a python list of all even numbers between 4 to 30
even_numbers = []

for num in range(4, 31):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

