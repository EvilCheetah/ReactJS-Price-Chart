from typing import TypedDict

from prices.types.amout import Amount
from prices.types.iso_date import ISODate
from prices.types.platform import Platform


class PriceEntry(TypedDict):
    id: str
    platform: Platform
    amount: Amount
    timestamp: ISODate