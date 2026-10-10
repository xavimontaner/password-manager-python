from src.models import Credential


def test_credential_to_dict() -> None:
    credential = Credential(
        service="GitHub",
        username="student",
        password="example-password",
        url="https://github.com",
        notes="Test account",
        created_at="2026-10-10 10:00:00",
        modified_at="2026-10-10 10:00:00",
    )

    assert credential.to_dict() == {
        "service": "GitHub",
        "username": "student",
        "password": "example-password",
        "url": "https://github.com",
        "notes": "Test account",
        "created_at": "2026-10-10 10:00:00",
        "modified_at": "2026-10-10 10:00:00",
    }