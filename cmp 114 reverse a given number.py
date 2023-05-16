#Write a program to reverse a given number
#buh/22/04/09/0097
#Name: Ani chukwuebuka Emmanuel
#dept: cyber security 100L

number = int(input("Enter a number: "))
reversed_number = 0

while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
print("Reversed Number: " + str(reversed_number))
