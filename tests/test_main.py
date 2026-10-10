import string
from src.main import generate_password


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