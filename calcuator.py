def add(P, Q):
    return P + Q


def subtract(P, Q):

    return P - Q


def multiply(P, Q):

    return P * Q


def divide(P, Q):

    return P / Q



print("select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input(" enter choice (a or b or c or d): ")

num_1 = int(input(" enter the first number: "))
num_2 = int(input(" enter the second number: "))

if choice == 'a':
    print(num_1, " + ", num_2, " = ", add(num_1, num_2))

elif choice == 'b':
    print(num_1, " - ", num_2, " = ", subtract(num_1, num_2))

elif choice == 'c':
    print(num1, " * ", num2, " = ", multiply(num1, num2))
elif choice == 'd':
    print(num_1, " / ", num_2, " = ", divide(num_1, num_2))
else:
    print("This is an invalid input")