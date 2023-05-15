#  No.2 Write a program to find the largest number in a list
lower_number = int(input("Input the Lowest Number: "))
upper_number = int(input("Input the Highest Number: "))

print("The Prime Numbers in the given range are: ")
for number in range(lower_number, upper_number + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)
