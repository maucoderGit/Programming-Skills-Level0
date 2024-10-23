import db as db
from models.users import User
from models.transaction import Transaction, TransactionType

# All functions must receive the account parameter

def get_balance(user_info) -> float:
    transactions = _get_transactions_by_account(user_info["account_ids"][0])

    balance: float = 0

    for transaction in transactions:
        balance += transaction["amount"] if transaction["transaction_type"] == "DEPOSIT" else -transaction["amount"]
    
    print(f"Your balance is: {balance}")
    
    return balance

def create_transaction(user_info):
    balance = get_balance(user_info)

    print("Select a transaction type to do:")

    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transference")

    transaction_type = int(input("Introduce the transaction type: "))

    if transaction_type not in range(1, 4):
        print("You selected a wrong option, please try again.")
        return
    
    amount: float = float(input("Please insert the amount of transaction (i.e.: 300.00): "))

    if transaction_type == 1:
        transaction_type = TransactionType.deposit
    elif transaction_type == 2:
        transaction_type = TransactionType.withdraw
    else:
        transaction_type = TransactionType.transference

    if transaction_type != 1 and amount > balance:
        print("Amount inserted is too high.")
        return

    if transaction_type == "TRANSFERENCE":
        account_to: str = input("Insert account number for transference: ")
    
    description: str = input("Insert any description (OPTIONAL - ENTER To continue): ")

    values: dict = {
        "id": 1213, # random for the moment, fix
        "name": description,
        "user_id": user_info["id"],
        "account_id": user_info["account_ids"][0],
        "amount": amount,
        "transaction_type": transaction_type.value
    }

    trx = Transaction(**values)

    table: str = Transaction._table_name.default
    all_transactions: list = db.get_records_from_json_file(table)

    all_transactions.append(values)

    db.update_json_file(table, all_transactions)

    print("DONE~!\n")

    return trx

MENU_OPTIONS = {
    0: ("Exit.", lambda: print("Bye!")),
    1: ("Get Balance", get_balance),
    2: ("Create movement", create_transaction)
}

def login(username: str, password: str) -> tuple[bool, int]:
    table: str = User._table_name.default
    users: list = db.get_records_from_json_file(table)

    for user in users:
        username_exists: bool = user.get("username") == username

        if username_exists and password == user.get("password"):
            user["login_attempts"] = 0

            user_info = user

            db.update_json_file(table, users)
            return user_info, user["login_attempts"]
        elif username_exists:
            user["login_attempts"] += 1

            db.update_json_file(table, users)

            return False, user["login_attempts"]

    return False, 0

def _get_transactions_by_account(account_id: int) -> list[dict]:
    table: str = Transaction._table_name.default
    all_transactions: list = db.get_records_from_json_file(table)

    transactions: list[dict] = []

    for transaction in all_transactions:
        account_related: bool = transaction.get("account_id") == account_id

        if account_related:
            transactions.append(transaction)

    return transactions

def select_menu_option(option: int, user_info) -> bool:
    if option == 0:
        return True

    try:
        _option_title, option_action = MENU_OPTIONS[option]
    except KeyError(e):
        print(f"Option: {option} is not a valid option!\n")

    option_action(user_info)

    return False

def display_menu_option() -> None:
    print("- Please select any of the following options: \n")
    for option_index, values in MENU_OPTIONS.items():
        print(f"  -> {option_index}: {values[0]}")

def run() -> None:
    print("Hi, welcome to your bank!\n")
    user_info: bool = False
    remaining_attempts: int = 0

    while remaining_attempts < 3 and not user_info:
        username: str = input("- Username: ")
        password: str = input("- Password: ")

        user_info, remaining_attempts = login(username, password)

        if user_info:
            break
        
        print("Wrong creedentials, please try again.")
        remaining_attempts += 1
    else:
        print("You reached the max attemps of login, try again later or contact an administrator.")
        return
    
    menu_processed = False

    while not menu_processed:
        display_menu_option()

        selection: int = int(input("INTRODUCE YOUR SELECTION: "))

        menu_processed = select_menu_option(selection, user_info)
    
    print("Bye~")