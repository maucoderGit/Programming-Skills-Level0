from dataclasses import dataclass

from .currency import Currency, CurrencyOptions


@dataclass
class CurrencyRate:
    """Rate conversiont to main exchange system currency"""
    _name = "currency_rate"

    currency: Currency

    rate: float
    inverse_rate: float

    min_amount: float
    max_amount: float

    def __init__(
        self,
        currency: Currency,
        rate: float = 0,
        inverse_rate: float = 0,
        min_amount: float = 0,
        max_amount: float = 0
    ):
        self.currency = currency

        if not rate:
            raise ValueError("Rate or inverse rate must be set.")

        if inverse_rate:
            rate = 1 / inverse_rate
        elif rate:
            inverse_rate = 1 / rate

        self.rate = rate
        self.inverse_rate = inverse_rate

    def convert_from_currency(self, amount) -> float:
        return round(amount * self.inverse_rate, 4)
    
    def convert_to_currency(self, amount) -> float:
        return round(amount * self.rate, 4)