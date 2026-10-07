import secrets
import string


def display_menu() -> None:
    """Display the available password manager actions."""
    print("\nPassword Manager")
    print("1. Add credential")
    print("2. List credentials")
    print("3. Search credentials")
    print("4. Generate password")
    print("5. Edit credential")
    print("6. View credential")
    print("7. Delete credential")
    print("0. Exit")


def add_credential(credentials: list[dict[str, str]]) -> None:
    """Add a new credential to the password manager and manage empty input."""
    service = input("Enter the service name: ").strip()
    username = input("Enter the username: ").strip()
    password = input("Enter the password: ").strip()

    if not service or not username or not password:
        print("Error: All fields are required.")
        return

    credentials.append({"service": service, "username": username, "password": password})
    print(f"Credential for {service} added successfully.")


def list_credentials(credentials: list[dict[str, str]]) -> None:
    """List all stored credentials."""
    if not credentials:
        print("No credentials stored.")
    else:
        for number, credential in enumerate(credentials, start=1):
            print(f"{number}. Service: {credential['service']}, Username: {credential['username']}, Password: ********")


def search_credentials(credentials: list[dict[str, str]]) -> None:
    """Search for a credential by service name."""
    service = input("Enter the service name to search: ").strip()
    found_credentials = [cred for cred in credentials if cred["service"].lower() == service.lower()]

    if not found_credentials:
        print(f"No credentials found for service: {service}")
    else:
        for number, credential in enumerate(found_credentials, start=1):
            print(f"{number}. Service: {credential['service']}, Username: {credential['username']}, Password: ********")


def generate_password() -> str:
    """Generate a random password."""
    length = 12  # Default password length
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


def select_credential(credentials: list[dict[str, str]]) -> dict[str, str] | None:
    """Select an existing credential."""
    service = input("Enter the service name of the credential: ").strip()
    if not service:
        print("Error: Service name is required.")
        return None
    found_credentials = [cred for cred in credentials if cred["service"].lower() == service.lower()]
    if not found_credentials:
        print(f"No credentials found for service: {service}")
        return None
    elif len(found_credentials) == 1:
        credential = found_credentials[0]
    else:
        print("Multiple credentials found for this service:")
        for i, cred in enumerate(found_credentials, start=1):
            print(f"  {i}. Username: {cred['username']}")
        try:
            index = int(input("Enter the number of the credential: ")) - 1
            if index < 0 or index >= len(found_credentials):
                print("Not in the list.")
                return None
            credential = found_credentials[index]
        except ValueError:
            print("Invalid selection.")
            return None
    return credential


def update_credential(credentials: list[dict[str, str]]) -> None:
    """Update an existing credential."""
    credential = select_credential(credentials)
    if not credential:
        return
    print(f"Updating credential for service: {credential['service']}")
    new_username = input(f"Enter new username (leave blank to keep '{credential['username']}'): ").strip()
    new_password = input(f"Enter new password (leave blank to keep current password): ").strip()
    if new_username:
        credential['username'] = new_username
    if new_password:
        credential['password'] = new_password

    print("Credential updated successfully.")


def view_credential(credentials: list[dict[str, str]]) -> None:
    """View a credential by service name."""
    credential = select_credential(credentials)
    if credential:
        print(f"Service: {credential['service']}, Username: {credential['username']}, Password: {credential['password']}")


def delete_credential(credentials: list[dict[str, str]]) -> None:
    """Delete a credential by service name."""
    credential = select_credential(credentials)
    if credential:
        while True:
            confirmation = input(f"Are you sure you want to delete the credential for '{credential['service']}'? (y/n): ").strip().lower()
            if confirmation in ('y', 'yes'):
                break
            elif confirmation in ('n', 'no'):
                print("Deletion cancelled.")
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        credentials.remove(credential)
        print(f"Credential for service '{credential['service']}' deleted successfully.")


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
            search_credentials(credentials)
        elif choice == "4":
            password = generate_password()
            print(f"Generated password: {password}")
        elif choice == "5":
            update_credential(credentials)
        elif choice == "6":
            view_credential(credentials)
        elif choice == "7":
            delete_credential(credentials)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from the menu.")


if __name__ == "__main__":
    main()
