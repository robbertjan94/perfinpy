import pytest
from perfinpy.core.money import Currency, Money

##### Currency ################################################################

def test_currency_valid():
    currency = Currency('EUR')
    assert currency.acronym == 'EUR'

def test_currency_invalid():
    with pytest.raises(ValueError):
        Currency('EURO')

def test_currency_equality():
    eur = Currency('EUR')
    assert eur == eur
    usd = Currency('USD')
    assert eur != usd

##### Money ###################################################################

def test_money_initialize():
    money_1 = Money(1)
    assert money_1.value == 1
    usd = Currency('USD')
    usd_1 = Money(1, usd)
    assert usd_1.currency == usd

def test_money_equality():
    eur_1 = Money(1, Currency('EUR'))
    assert eur_1 == eur_1
    eur_5 = Money(5, Currency('EUR'))
    assert eur_1 != eur_5
    usd_1 = Money(1, Currency('USD'))
    assert eur_1 != usd_1

def test_money_compatible():
    eur_1 = Money(1, Currency('EUR'))
    assert eur_1.compatible(eur_1)
    usd_1 = Money(1, Currency('USD'))
    assert not eur_1.compatible(usd_1)
