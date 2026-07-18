def c_to_f(c):
    return round((c * 9 / 5) + 32, 2)


def f_to_c(f):
    return round((f - 32) * 5 / 9, 2)


def cm_to_m(cm):
    return round(cm / 100, 2)


def m_to_cm(m):
    return round(m * 100, 2)


def kg_to_g(kg):
    return round(kg * 1000, 2)


def g_to_kg(g):
    return round(g / 1000, 2)


def print_title():
    print("=" * 35)
    print("Biomedical Unit Converter")
    print("=" * 35)
    print()


def print_menu():
    print("""
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Centimeter to Meter
4. Meter to Centimeter
5. Kilogram to Gram
6. Gram to Kilogram
0. Exit
""")


def main():
    print_title()
    print("Welcome to the Biomedical Unit Converter!")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's get started.\n")
    while True:
        print_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")
            continue   


        if choice == 0:
                print("Exiting... Goodbye!")
                break

        if choice < 1 or choice > 6:
                print("Invalid choice. Please enter a number between 0 and 6.\n")
                continue

        if choice == 1:
                c = float(input("Enter Celsius: "))
                print(f"Result: {c}°C = {c_to_f(c)}°F\n")

        elif choice == 2:
                f = float(input("Enter Fahrenheit: "))
                print(f"Result: {f}°F = {f_to_c(f)}°C\n")

        elif choice == 3:
                cm = float(input("Enter Centimeter: "))
                print(f"Result: {cm} cm = {cm_to_m(cm)} m\n")

        elif choice == 4:
                m = float(input("Enter Meter: "))
                print(f"Result: {m} m = {m_to_cm(m)} cm\n")

        elif choice == 5:
                kg = float(input("Enter Kilogram: "))
                print(f"Result: {kg} kg = {kg_to_g(kg)} g\n")

        elif choice == 6:
                g = float(input("Enter Gram: "))
                print(f"Result: {g} g = {g_to_kg(g)} kg\n")



if __name__ == "__main__":
    main()
