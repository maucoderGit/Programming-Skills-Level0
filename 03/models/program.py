from .user import USERS

class Program():
    name: str
    available_spots: int

    registered_users: list = []

    def __init__(self, name, available_spots):
        self.name = name
        self.available_spots = available_spots

PROGRAMS = [
    Program("Computer Science", 5),
    Program("Medicine", 5),
    Program("Marketing", 5),
    Program("Arts", 5),
]
