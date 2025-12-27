FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    try:
        return (float(fahrenheit) - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    except ValueError:
        return "Invalid input. Please enter a numeric value."

def convert_to_fahrenheit(celsius):
    try:
        return (float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    except ValueError:
        return "Invalid input. Please enter a numeric value."

    ## Usage
temp = input("Enter temperature to convert: ")
unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "F":
    print(f"{temp}°F is ", convert_to_celsius(temp),"°C")
elif unit == "C":
    print(f"{temp}°C is ", convert_to_fahrenheit(temp),"°F")
else:
    print("Invalid unit. Please enter C or F.")
