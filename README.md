# CMP104python
#write a program with two classes, maths and pthysics that have 5 operations in each class

class Math:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def power(self, x, y):
        return x ** y


class Physics:
    def velocity(self, distance, time):
        return distance / time

    def acceleration(self, initial_velocity, final_velocity, time):
        return (final_velocity - initial_velocity) / time

    def force(self, mass, acceleration):
        return mass * acceleration

    def work(self, force, distance):
        return force * distance

    def power(self, work, time):
        return work / time


def main():
    # Ask the user which subject they want to calculate
    subject = input("Do you want to calculate Math or Physics? ")

    # Create an instance of the appropriate class based on user input
    if subject.lower() == "math":
        calculator = Math()
    elif subject.lower() == "physics":
        calculator = Physics()
    else:
        print("Invalid subject")
        return

    # Ask the user which operation they want to perform
    operation = input("What operation do you want to perform? ")

    # Call the appropriate method based on user input
    if operation.lower() == "add":
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = calculator.add(x, y)
    elif operation.lower() == "subtract":
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = calculator.subtract(x, y)
    elif operation.lower() == "multiply":
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = calculator.multiply(x, y)
    elif operation.lower() == "divide":
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = calculator.divide(x, y)
    elif operation.lower() == "power":
        x = float(input("Enter the base number: "))
        y = float(input("Enter the exponent: "))
        result = calculator.power(x, y)
    elif operation.lower() == "velocity":
        distance = float(input("Enter the distance: "))
        time = float(input("Enter the time: "))
        result = calculator.velocity(distance, time)
    elif operation.lower() == "acceleration":
        initial_velocity = float(input("Enter the initial velocity: "))
        final_velocity = float(input("Enter the final velocity: "))
        time = float(input("Enter the time: "))
        result = calculator.acceleration(initial_velocity, final_velocity, time)
    elif operation.lower() == "force":
        mass = float(input("Enter the mass: "))
        acceleration = float(input("Enter the acceleration: "))
        result = calculator.force(mass, acceleration)
    elif operation.lower() == "work":
        force = float(input("Enter the force: "))
        distance = float(input("Enter the distance: "))
        result = calculator.work(force, distance)
    elif operation.lower() == "power":
        work = float(input("Enter the work: "))
        time = float(input("Enter the time: "))
        result = calculator.power(work, time)
    else:
        print("Invalid operation")
        return

    # Print the result
    print("Result:", result)


if __name__ == "__main__":
    main()
