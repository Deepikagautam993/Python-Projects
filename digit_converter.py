def convert_number(number, base_from, base_to):
    try:
        # Convert input to decimal first
        decimal = int(number, base_from)
        # Convert decimal to target base
        if base_to == 2:
            return bin(decimal)
        elif base_to == 8:
            return oct(decimal)
        elif base_to == 10:
            return str(decimal)
        elif base_to == 16:
            return hex(decimal)
    except ValueError:
        return "Invalid Input"

def main():
    print("Digit Converter Tool")
    number = input("Enter number: ")
    base_from = int(input("Enter base of input (2/8/10/16): "))
    base_to = int(input("Enter base to convert to (2/8/10/16): "))
    
    result = convert_number(number, base_from, base_to)
    print("Converted Value:", result)

if __name__ == "__main__":
    main()