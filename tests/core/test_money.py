import pytest
from perfinpy.core.money import Currency, Money

##### Currency ################################################################

def test_valid_currency():
    valid_acronym = 'EUR'
    currency = Currency(valid_acronym)
    assert currency.acronym == valid_acronym

def test_invalid_currency():
    invalid_acronym = 'EURO'
    with pytest.raises(ValueError):
        Currency(invalid_acronym)