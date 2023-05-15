# 1 Python program to find the largest number in a list

#  list of numbers
list_of_numbers = []

number_of_elements = int(input("Enter number of elements in list: "))

for i in range(1, number_of_elements + 1):
    element = int(input("Enter elements: "))
    list_of_numbers.append(element)

print("largest element is:", max(list_of_numbers))


