def calculate_weather(t, h, w):
    return 0.5 * t**2 - 0.2 * h + 0.1 * w - 15

def predict_weather(weather):
    if weather <= 100:
        return "Stormy"
    elif 100 < weather < 200:
        return "Mild"
    elif 200 <= weather < 250:
        return "Rainy"
    elif 250 <= weather < 300:
        return "Cloudy"
    else:
        return "Sunny"

#hardcoded values
def process_hardcoded_values():
    print("\nProcessing hardcoded values:")
    t = 30  
    h = 50  
    w = 10  
    weather = calculate_weather(t, h, w)
    weather_type = predict_weather(weather)
    print(f"With hardcoded values (t={t}, h={h}, w={w}), Weather = {weather:.2f}, Prediction: {weather_type}")

#values from keyboard input
def process_keyboard_input():
    print("\nProcessing values from keyboard input:")
    t = float(input("Enter the temperature (t): "))
    h = float(input("Enter the humidity (h): "))
    w = float(input("Enter the wind speed (w): "))
    weather = calculate_weather(t, h, w)
    weather_type = predict_weather(weather)
    print(f"With input values (t={t}, h={h}, w={w}), Weather = {weather:.2f}, Prediction: {weather_type}")
#inputs from a file
def process_single_input_from_file(file_name):
    print("\nProcessing a single set of inputs from file:")
    try:
        with open(file_name, "r") as file:
            line = file.readline().strip()
            t, h, w = map(float, line.split())
        weather = calculate_weather(t, h, w)
        weather_type = predict_weather(weather)
        print(f"With input values (t={t}, h={h}, w={w}), Weather = {weather:.2f}, Prediction: {weather_type}")
    except FileNotFoundError:
        print("Error: File not found. Please ensure the file exists.")
    except ValueError:
        print("Error: Invalid input format in the file.")

#multiple sets of inputs from a file
def process_multiple_inputs_from_file(file_name):
    print("\nProcessing multiple sets of inputs from file:")
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            try:
                t, h, w = map(float, line.strip().split())
                weather = calculate_weather(t, h, w)
                weather_type = predict_weather(weather)
                print(f"With input values (t={t}, h={h}, w={w}), Weather = {weather:.2f}, Prediction: {weather_type}")
            except ValueError:
                print(f"Set {i + 1}: Invalid input format. Skipping this set.")
    except FileNotFoundError:
        print("Error: File not found. Please ensure the file exists.")

def main():
    print("Weather Modeling using the formula: w = 0.5t^2 - 0.2h + 0.1w - 15")
    print("Choose an option:")
    print("1. Process hardcoded values.")
    print("2. Process values from keyboard input.")
    print("3. Process a single set of inputs from a file.")
    print("4. Process multiple sets of inputs from a file.")
    choice = input("Enter your choice (1, 2, 3, or 4): ")
    if choice == "1":
        process_hardcoded_values()
    elif choice == "2":
        process_keyboard_input()
    elif choice == "3":
        file_name = input("Enter the file name (e.g., 'values.txt'): ")
        process_single_input_from_file(file_name)
    elif choice == "4":
        file_name = input("Enter the file name (e.g., 'values.txt'): ")
        process_multiple_inputs_from_file(file_name)
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
if __name__ == "__main__":
    main()
