import os
import calculator

DESCRIPTION = """
===============================
📐 Geometry Area Calculator 📐
Calculate area & perimeter of:
- Rectangle
- Square
- Triangle
- Circle
- Regular Hexagon
===============================
"""

def print_menu():
    print("1. Rectangle")
    print("2. Square")
    print("3. Triangle")
    print("4. Circle")
    print("5. Hexagon")
    print("0. Exit")

def run():
    while True:
        print(DESCRIPTION)
        print_menu()

        choice = input("\nChoose an option (0-5): ")

        print(DESCRIPTION)

        if choice == "1":
            print("📏 Rectangle selected.")
            calculator.get_rectangle()

        elif choice == "2":
            print("⬛ Square selected.")
            calculator.get_square()

        elif choice == "3":
            print("🔺 Triangle selected.")
            calculator.get_right_triangle()

        elif choice == "4":
            print("⚪ Circle selected.")
            calculator.get_circle()

        elif choice == "5":
            print("⬡ Hexagon selected.")
            calculator.get_hexagon()

        elif choice == "0":
            print("Exiting... 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

        input("\nPress Enter to return to the menu...")

run()
