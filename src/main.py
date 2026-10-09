import json
import secrets
import string
from datetime import datetime


def current_timestamp() -> str:
    """Return the current local date and time in a readable format."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


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


def load_credentials() -> list[dict[str, str]]:
    """Load credentials from a file"""
    try:
        with open("credentials.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Credentials file is corrupted. Starting with an empty list.")
        return []


def save_credentials(credentials: list[dict[str, str]]) -> None:
    """Save credentials to a file"""
    with open("credentials.json", "w") as file:
        json.dump(credentials, file, indent=4)


def add_credential(credentials: list[dict[str, str]]) -> None:
    """Add a new credential to the password manager and manage empty input."""
    service = input("Enter the service name: ").strip()
    username = input("Enter the username: ").strip()
    password = input("Enter the password: ").strip()
    url = input("Enter the URL (optional): ").strip()
    notes = input("Enter any notes (optional): ").strip()

    if not service or not username or not password:
        print("Error: Service, username, and password are required.")
        return

    timestamp = current_timestamp()
    credentials.append(
        {
            "service": service,
            "username": username,
            "password": password,
            "url": url,
            "notes": notes,
            "created_at": timestamp,
            "modified_at": timestamp,
        }
    )
    print(f"Credential for {service} added successfully.")


def display_credential(
    credential: dict[str, str],
    number: int | None,
    show_password: bool,
) -> None:
    """Display the details of a single credential."""
    if number is not None:
        print(f"{number}.")
    print(f"Service: {credential['service']}")
    print(f"Username: {credential['username']}")
    if show_password:
        print(f"Password: {credential['password']}")
    else:
        print(f"Password: ********")
    print(f"URL: {credential.get('url') or 'N/A'}")
    print(f"Notes: {credential.get('notes') or 'N/A'}")
    print(f"Created At: {credential.get('created_at', 'N/A')}")
    print(f"Modified At: {credential.get('modified_at', 'N/A')}")


def list_credentials(credentials: list[dict[str, str]]) -> None:
    """List all stored credentials."""
    if not credentials:
        print("No credentials stored.")
    else:
        for number, credential in enumerate(credentials, start=1):
            display_credential(credential, number, False)


def search_credentials(credentials: list[dict[str, str]]) -> None:
    """Search for a credential by service name."""
    service = input("Enter the service name to search: ").strip()
    found_credentials = [cred for cred in credentials if cred["service"].lower() == service.lower()]

    if not found_credentials:
        print(f"No credentials found for service: {service}")
    else:
        for number, credential in enumerate(found_credentials, start=1):
            display_credential(credential, number, False)


def generate_password() -> str:
    """Generate a random password."""
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    lowercase = secrets.choice(string.ascii_lowercase)
    uppercase = secrets.choice(string.ascii_uppercase)
    digit = secrets.choice(string.digits)
    punctuation = secrets.choice(string.punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    password_list = [lowercase, uppercase, digit, punctuation]
    for _ in range(length - 4):
        password_list.append(secrets.choice(characters))
    secrets.SystemRandom().shuffle(password_list)
    password = "".join(password_list)
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
    was_updated = False
    new_username = input(f"Enter new username (leave blank to keep '{credential['username']}'): ").strip()
    new_password = input(f"Enter new password (leave blank to keep current password): ").strip()
    new_url = input(f"Enter new URL (leave blank to keep '{credential.get('url') or 'N/A'}'): ").strip()
    new_notes = input(f"Enter new notes (leave blank to keep '{credential.get('notes') or 'N/A'}'): ").strip()
    if new_username:
        credential['username'] = new_username
        was_updated = True
    if new_password:
        credential['password'] = new_password
        was_updated = True
    if new_url:
        credential['url'] = new_url
        was_updated = True
    if new_notes:
        credential['notes'] = new_notes
        was_updated = True
    if was_updated:
        credential['modified_at'] = current_timestamp()
        print("Credential updated successfully.")
    else:
        print("No changes made.")


def view_credential(credentials: list[dict[str, str]]) -> None:
    """View a credential by service name."""
    credential = select_credential(credentials)
    if credential:
        display_credential(credential, None, True)


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
    credentials = load_credentials()
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_credential(credentials)
            save_credentials(credentials)
        elif choice == "2":
            list_credentials(credentials)
        elif choice == "3":
            search_credentials(credentials)
        elif choice == "4":
            password = generate_password()
            print(f"Generated password: {password}")
        elif choice == "5":
            update_credential(credentials)
            save_credentials(credentials)
        elif choice == "6":
            view_credential(credentials)
        elif choice == "7":
            delete_credential(credentials)
            save_credentials(credentials)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from the menu.")


if __name__ == "__main__":
    main()
