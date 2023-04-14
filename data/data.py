from dataclasses import dataclass


@dataclass
class Person:
    """Хранить необходимые для тестов данные.
    """
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
