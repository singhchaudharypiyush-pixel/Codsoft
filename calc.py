# file: calculator.py
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0: raise ZeroDivisionError("Cannot divide by zero")
    return a / b
def power(a, b): return a ** b

ops = {
    "1": ("Addition", add),
    "2": ("Subtraction", sub),
    "3": ("Multiplication", mul),
    "4": ("Division", div),
    "5": ("Power", power),
    "6": ("Exit", None)
}

def get_number(prompt):
    while True:
        try: return float(input(prompt))
        except ValueError: print("Please enter a valid number.")

def main():
    while True:
        print("\n=== SIMPLE CALCULATOR ===")
        for k,(name,_) in ops.items(): print(f"{k}. {name}")
        choice = input("Choose operation: ").strip()
        if choice == "6": print("Goodbye!"); break
        if choice not in ops: print("Invalid choice."); continue
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        try:
            result = ops[choice][1](a, b)
            print(f"Result: {result}")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
