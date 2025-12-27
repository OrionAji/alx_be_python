FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Conversion functions for ALX checker
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program
def main():
    while True:
        print("\nTemperature Conversion Tool")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            try:
                temp_c = float(input("Enter temperature in Celsius: "))
                temp_f = convert_to_fahrenheit(temp_c)
                print(f"{temp_c:.1f}°C is {temp_f:.1f}°F")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == "2":
            try:
                temp_f = float(input("Enter temperature in Fahrenheit: "))
                temp_c = convert_to_celsius(temp_f)
                print(f"{temp_f:.1f}°F is {temp_c:.1f}°C")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
