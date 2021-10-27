from __future__ import annotations
import datetime as dt
import os
from typing import List
from perfinpy.utils import read_file

##### Currency ################################################################

_currency_acronyms_path = os.path.join('data', 'currency_acronyms.txt')

def _get_currency_acronyms(path=_currency_acronyms_path) -> List[str]:
    """Read valid currency acronyms from file."""
    s = read_file(path)
    return s.split('\n')

_currencies_list = _get_currency_acronyms()

class Currency:
    """Base currency object."""

    def __init__(self, acronym: str):
        if acronym not in _currencies_list:
            raise ValueError
        self.acronym = acronym            

    def __repr__(self):
        return f'Currency({self.acronym})'

    def __str__(self):
        return self.acronym

    def _fx_rate(self, other: Currency, datetime: dt.datetime = None):
        raise NotImplementedError

_default_currency = Currency('EUR')

##### Money ###################################################################

class Money:
    """Base money object."""

    def __init__(self, value: float, currency: Currency = _default_currency):

        self.value = value
        self.currency = currency
    
    def __repr__(self):
        return f'Money({self.value}, {self.currency})'

    def __str__(self):
        return f'{self.currency} {self.value}'

    def __add__(self, other: Money) -> Money:
        if not self.compatible(other):
            raise TypeError
        return Money(self.value+other.value, self.currency)

    def compatible(self, other: Money) -> bool:
        """Checks if `self` and `other` are denominated in the same currency."""
        return self.currency == other.currency
