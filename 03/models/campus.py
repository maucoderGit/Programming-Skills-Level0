class Campus():
    name: str

    program_spots_limit: int
    registered_users: list = []

    def __init__(self, name, program_spots_limit):
        self.name = name
        self.program_spots_limit = program_spots_limit

CAMPUS_RECORDS = [
    Campus("Manchester", 3),
    Campus("Liverpool", 1),
    Campus("London", 1)
]
