

class Credential:
    def __init__(self, service: str, username: str, password: str, url: str, notes: str, created_at: str, modified_at: str) -> None:
        self.service = service
        self.username = username
        self.password = password
        self.url = url
        self.notes = notes
        self.created_at = created_at
        self.modified_at = modified_at

    def to_dict(self) -> dict[str, str]:
        return {
            "service": self.service,
            "username": self.username,
            "password": self.password,
            "url": self.url,
            "notes": self.notes,
            "created_at": self.created_at,
            "modified_at": self.modified_at,
        }