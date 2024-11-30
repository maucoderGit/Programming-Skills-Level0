from enum import Enum
from typing import Union

from models.currency import CurrencyOptions, Currency
from models.currency_rate import CurrencyRate

main_currency = CurrencyOptions.USD

CurrentConversions: dict[CurrencyOptions, CurrencyRate] = {
    (CurrencyOptions.USD).value.code: CurrencyRate(CurrencyOptions.USD.value, 1),
    (CurrencyOptions.EUR).value.code: CurrencyRate(CurrencyOptions.EUR.value, 0.95),
    (CurrencyOptions.CLP).value.code: CurrencyRate(CurrencyOptions.CLP.value, 970.87),
    (CurrencyOptions.ARS).value.code: CurrencyRate(CurrencyOptions.ARS.value, 1010.14),
    (CurrencyOptions.TRY).value.code: CurrencyRate(CurrencyOptions.TRY.value, 34.66),
    (CurrencyOptions.GBP).value.code: CurrencyRate(CurrencyOptions.GBP.value, 0.79),
}

def user_selection_true_or_false(msg: str) -> bool:
    selection = False

    while selection not in ("Y", "N"):
        selection = input(f"{msg}").upper()

    return selection == "Y"

def select_currency(msg: str) -> str:
    currency = False

    while isinstance(currency, bool) or not CurrencyOptions[currency]:
        currency = input(f"\n{msg}").upper()

        try:
            currency = CurrencyOptions[currency].value.code
        except KeyError as e:
            print("Select a valid option")
            currency = False

    return currency

def convert_amount_and_withdraw(currency_from, currency_to):
    withdraw = False

    amount_to_withdraw = 0

    convert_to_base = CurrentConversions[currency_from]
    conversion_to = CurrentConversions[currency_to]

    while not withdraw:
        success: bool = False

        while not success:
            base_amount = float(input("Insert the amount to convert: "))

            if main_currency != currency_from:
                base_amount = convert_to_base.convert_from_currency(base_amount)
            
            result = conversion_to.convert_to_currency(base_amount)

            success = user_selection_true_or_false(f"The result of current conversion is: {result} {conversion_to.currency.symbol}, you want to complete the conversion? [Y/N]: ")

            if success:
                amount_to_withdraw += result

        withdraw = user_selection_true_or_false(f"Do you want to withdraw {amount_to_withdraw} {conversion_to.currency.symbol}? [Y/N (No option will start another conversion)]: ")

    return amount_to_withdraw


def run():
    print("Welcome to YUI currency exchange, the exchange system you can rely on.\n")
    currency_option_names: list = [f"[{currency.value.code}] - {currency.value.name}" for currency in CurrencyOptions]

    complete = False

    while not complete:
        print("\n".join(currency_option_names))

        currency_from = select_currency("Please, select your main currency by code from the above options (i.e; USD): ")
        currency_to = select_currency("Now, select the currency to convert (i.e; EUR): ")

        amount_withdrawed = convert_amount_and_withdraw(currency_from, currency_to)

        complete = not user_selection_true_or_false("Do you want to perform another operation? [Y/N]: ")

if __name__ == "__main__":
    run()
