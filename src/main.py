def display_menu() -> None:
    """Display the available password manager actions."""
    print("\nPassword Manager")
    print("1. Add credential")
    print("2. List credentials")
    print("3. Search credentials")
    print("4. Generate password")
    print("0. Exit")


def main() -> None:
    """Run the menu until the user exits."""
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("Add credential is not implemented yet.")
        elif choice == "2":
            print("List credentials is not implemented yet.")
        elif choice == "3":
            print("Search credentials is not implemented yet.")
        elif choice == "4":
            print("Password generation is not implemented yet.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from the menu.")


if __name__ == "__main__":
    main()
