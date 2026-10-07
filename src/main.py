def display_menu() -> None:
    """Display the available password manager actions."""
    print("\nPassword Manager")
    print("1. Add credential")
    print("2. List credentials")
    print("3. Search credentials")
    print("4. Generate password")
    print("0. Exit")


def add_credential(credentials: list[dict[str, str]]) -> None:
    """Add a new credential to the password manager."""
    service = input("Enter the service name: ").strip()
    username = input("Enter the username: ").strip()
    password = input("Enter the password: ").strip()
    credentials.append({"service": service, "username": username, "password": password})
    print(f"Credential for {service} added successfully.")


def list_credentials(credentials: list[dict[str, str]]) -> None:
    """List all stored credentials."""
    if not credentials:
        print("No credentials stored.")
    else:
        for number, credential in enumerate(credentials, start=1):
            print(f"{number}. Service: {credential['service']}, Username: {credential['username']}, Password: ********")


def main() -> None:
    """Run the menu until the user exits."""
    credentials = []
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_credential(credentials)
        elif choice == "2":
            list_credentials(credentials)
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
