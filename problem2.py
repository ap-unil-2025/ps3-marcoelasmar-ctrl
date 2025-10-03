

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit"""
    return round((celsius * 9/5) + 32, 2)


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius"""
    return round((fahrenheit - 32) * 5/9, 2)


def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    print("Temperature Converter")
    print("-" * 30)

    try:
        value = float(input("Enter the temperature value: ").strip())
        unit = input("Is this in Celsius (C) or Fahrenheit (F)? ").strip().upper()

        if unit == "C":
            result = celsius_to_fahrenheit(value)
            print(f"{value}°C is equal to {result}°F")
        elif unit == "F":
            result = fahrenheit_to_celsius(value)
            print(f"{value}°F is equal to {result}°C")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("❌ Please enter a valid number for temperature.")

# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"
    
    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()