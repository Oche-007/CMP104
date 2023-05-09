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

def perform_operation(category):
    operation = input(f"Enter the {category} operation: ")
    values = input("Enter the values (comma-separated): ").split(",")
    values = [float(value.strip()) for value in values]

# Ask what operations they wish to perform and return the appropriate answer

    if category == "math":
        math = Math()
        if operation == 'add':
            return math.add(*values)
        elif operation == 'subtract':
            return math.subtract(*values)
        elif operation == 'multiply':
            return math.multiply(*values)
        elif operation == 'divide':
            return math.divide(*values)
        elif operation == 'power':
            return math.power(*values)

    elif category == "physics":
        physics = Physics()
        if operation == 'velocity':
            return physics.velocity(*values)
        elif operation == 'acceleration':
            return physics.acceleration(*values)
        elif operation == 'force':
            return physics.force(*values)
        elif operation == 'work':
            return physics.work(*values)
        elif operation == 'energy':
            return physics.energy(*values)

    return None


category = input("Enter 'math' or 'physics' to select the category: ")

result = perform_operation(category)
if result is not None:
    print("Result:", result)
else:
    print("Invalid category or operation.")
