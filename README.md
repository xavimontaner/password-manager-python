# password-manager-python
A beginner-friendly Python password manager built incrementally to explore CLI development, clean architecture, secure storage, cryptography, testing, and software engineering best practices.

## Requirements

- Python 3.13 or later
- pytest (only needed to run the tests)



# Password Manager (Python)

A beginner-friendly command-line password manager built in Python. This project is developed incrementally to practice Python, clean architecture, secure storage, cryptography, testing, and software engineering best practices.

## Current features

- Add credentials
- List credentials
- Search credentials by service
- View a credential
- Edit credentials
- Delete credentials
- Generate secure random passwords
- Save and load credentials from a JSON file

## Requirements

- Python 3.13 or later
- pytest (only needed to run the tests)

## Run the program

From the `password-manager-python` directory:

```powershell
py src/main.py
```

## Run the tests

```powershell
py -m pytest
```

## Important security note

This is an educational project. Credentials are currently stored in `credentials.json` as plain text and are **not encrypted**.

Use only fictional or test credentials. Do not store real passwords until encryption is added in a later version.