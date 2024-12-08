class User():
    username: str
    password: str

    first_name: str
    last_name: str

    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.password = password

        self.first_name = first_name
        self.last_name = last_name

# Our users haven't the best security practices.

USERS = [
    User("maucoder", "password123"),
    User("BanderaAntonio", "ilovecats"),
    User("CoolStudent", "12345678"),
    User("HackerMan", "h4ck3r", "Hacker", "Man"),
    User("SecretAgent007", "007", "James", "Bond"),
    User("QueenOfTheInternet", "princess"),
    User("TheProcrastinator", "deadline?"),
    User("CoffeeLover", "coffeetime"),
    User("NightOwl", "latenightcode"),
    User("EarlyBird", "morningroutine")
]
