def myfun():
    x=int(input("enter value of x"))
    y=int(input("enter  tvalue of y"))
    print(f"Addition ofwo numbers is {x + y}")
    print(f"Subtraction of two numbers is {x - y}")
    print(f"Division of two numbers is {x / y}")
    print(f"Multiplication of two numbers is {x * y}")
myfun()

def covid(name,temp = 98):
    print(f"Name={name}\ntemperature={temp}")

covid("Murphy",96)
covid("Raven")