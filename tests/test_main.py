import string
from src.main import generate_password, add_credential
from src.models import Credential


def test_generate_password_has_requested_length_and_character_types(
    monkeypatch,
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "12")

    password = generate_password()

    assert len(password) == 12
    assert any(character.islower() for character in password)
    assert any(character.isupper() for character in password)
    assert any(character.isdigit() for character in password)
    assert any(character in string.punctuation for character in password)


def test_generate_password_retries_when_length_is_too_short(
    monkeypatch,
) -> None:
    inputs = iter(["5", "8"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    password = generate_password()

    assert len(password) == 8


def test_add_credential(monkeypatch) -> None:
    inputs = iter(
        [
            "TestService",
            "TestUser",
            "TestPassword",
            "https://testservice.com",
            "Test notes",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    credentials = []
    
    add_credential(credentials)

    assert len(credentials) == 1
    credential = credentials[0]
    assert isinstance(credential, Credential)
    assert credential.service == "TestService"
    assert credential.username == "TestUser"
    assert credential.password == "TestPassword"
    assert credential.url == "https://testservice.com"
    assert credential.notes == "Test notes"