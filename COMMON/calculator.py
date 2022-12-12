
# define the functions needed : add, sub, mul and div
# print options to the user 
# ask for the values
# call the functions
# while loop to continue the program until the user wants to exit

def add(a,b):
    result = a + b
    print(str(a) + " + " + str(b) + " = " + str(result))

def sub(a,b):
    result = a - b
    print(str(a) + " - " + str(b) + " = " + str(result))

def mul(a,b):
    result = a * b
    print(str(a) + " * " + str(b) + " = " + str(result))

def div(a,b):
    result = a/b
    print(str(a) + " / " + str(b) + " = " + str(result))
while True:
    print("A.   Addition")
    print("B.   Substraction")
    print("C.   Multiplication")
    print("D.   Division")
    print("E.   Exit")

    choice = input("Input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        add(a,b)
    elif choice == "b" or choice == "B":
        print("Substraction")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        sub(a,b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        mul(a,b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        div(a,b)
    elif choice == "e" or choice == "E":
        print("program ended")
        quit()





