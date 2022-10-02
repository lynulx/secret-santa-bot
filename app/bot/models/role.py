frmo dataclasses import dataclass


@dataclass
class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"
