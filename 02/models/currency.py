from dataclasses import dataclass

from enum import Enum

@dataclass
class Currency:
    _name = "currency"

    def __init__(self, name: str, symbol: str, code: str):
        self.name = name
        self.code = code
        self.symbol = symbol

    name: str = ""
    code: str = ""

    symbol: str = ""

    def __eq__(self, record) -> bool:
        if isinstance(record, Currency):
            return self.code == record.code and self.symbol == record.symbol and self.name == record.name
        
        return self.code == record



class CurrencyOptions(Enum):
    CLP = Currency(
        name="Chilean peso",
        symbol="CLP$",
        code="CLP"
    )

    ARS = Currency(
        name="Argentinan Peso",
        symbol="$",
        code="ARS"
    )

    USD = Currency(
        name="U.S Dollar",
        symbol="$",
        code="USD"
    )

    EUR = Currency(
        name="Euro",
        symbol="€",
        code="EUR"
    )

    TRY = Currency(
        name="Turkish Lira",
        symbol="₺",
        code="TRY"
    )

    GBP = Currency(
        name="British Pound",
        symbol="£sd",
        code="GBP"
    )
