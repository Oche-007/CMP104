#  Write a program with two classes Math & physics that have 5 operations in each class
# Ask the user if they were to calculate math or physics
# Ask what operations they wish to perform and return the appropriate answer

class Math:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def power(self, a, b):
        return a ** b


class Physics:
    def __init__(self):
        pass

    def velocity(self, distance, time):
        return distance / time

    def acceleration(self, velocity, time):
        return velocity / time

    def force(self, mass, acceleration):
        return mass * acceleration

    def work(self, force, distance):
        return force * distance

    def energy(self, mass, velocity):
        return 0.5 * mass * velocity ** 2

# Ask the user if they were to calculate math or physics

choice = input("Enter 'math' or 'physics' to perform calculations: ")

if choice == 'math':
    math = Math()
    print(math.add(4, 7))
    print(math.subtract(10, 5))
    print(math.multiply(10, 10))
    print(math.divide(100, 10))
    print(math.power(2, 6))

elif choice == 'physics':
    physics = Physics()
    print(physics.velocity(100, 10))
    print(physics.acceleration(64, 4))
    print(physics.force(45, 5))
    print(physics.work(20, 5))
    print(physics.energy(5, 10))

else:
    print("Wrong choice. Please enter 'math' or 'physics'.")
