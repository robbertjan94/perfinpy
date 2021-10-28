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

    def __eq__(self, other: Currency):
        return self.acronym == other.acronym

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

    def __eq__(self, other: Money) -> bool:
        same_value = self.value == other.value
        return same_value and self.compatible(other)

    def __add__(self, other: Money | int | float) -> Money:
        if isinstance(other, (int, float)):
            return Money(self.value+other, self.currency)
        if isinstance(other, Money):
            if self.compatible(other):
                return Money(self.value+other.value, self.currency)
        raise TypeError

    def __radd__(self, other: Money | int | float) -> Money:
        return self + other

    def __sub__(self, other: Money | int | float) -> Money:
        if isinstance(other, (int, float)):
            return Money(self.value-other, self.currency)
        if isinstance(other, Money):
            if self.compatible(other):
                return Money(self.value-other.value, self.currency)
        raise TypeError

    def __rsub__(self, other: Money | int | float) -> Money:
        return other - self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.value*other, self.currency)
        if isinstance(other, Money):
            if self.compatible(other):
                return Money(self.value*other.value, self.currency)
        raise TypeError

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.value/other, self.currency)
        if isinstance(other, Money):
            if self.compatible(other):
                return Money(self.value/other.value, self.currency)
        raise TypeError

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return Money(other/self.value, self.currency)
        if isinstance(other, Money):
            if self.compatible(other):
                return Money(other.value/self.value, self.currency)
        raise TypeError

    def compatible(self, other: Money) -> bool:
        """Checks equality of denominations."""
        return self.currency == other.currency
