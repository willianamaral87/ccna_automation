from calculator import Calculator

def main():
    calc = Calculator()

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", calc.add(a, b))
    print("Subtraction:", calc.subtract(a, b))

if __name__ == "__main__":
    main()