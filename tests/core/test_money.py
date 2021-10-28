import pytest
from perfinpy.core.money import Currency, Money

##### Currency ################################################################

def test_currency_init():
    currency = Currency('EUR')
    assert currency.acronym == 'EUR'
    with pytest.raises(ValueError):
        Currency('EURO')

def test_currency_equality():
    eur = Currency('EUR')
    assert eur == eur
    usd = Currency('USD')
    assert eur != usd

##### Money ###################################################################

def test_money_init():
    money_1 = Money(1)
    assert money_1.value == 1
    eur = Currency('EUR')
    eur_1 = Money(1, eur)
    assert eur_1.currency == eur

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

def test_money_add():
    eur = Currency('EUR')
    eur_1 = Money(1, eur)
    eur_5 = Money(5, eur)
    assert eur_1 + eur_5 == Money(6, eur)
    assert eur_1 + 5 == Money(6, eur)
    assert 5 + eur_1 == Money(6, eur)
    usd = Currency('USD')
    usd_1 = Money(1, usd)
    with pytest.raises(TypeError):
        eur_1 + usd_1

def test_money_subtract():
    eur = Currency('EUR')
    eur_1 = Money(1, eur)
    eur_5 = Money(5, eur)
    assert eur_5 - eur_1 == Money(4, eur)
    assert eur_5 - 1 == Money(4, eur)
    assert 9 - eur_5 == Money(4, eur)
    assert eur_1 - eur_5 == Money(-4, eur)
    usd = Currency('USD')
    usd_1 = Money(1, usd)
    with pytest.raises(TypeError):
        eur_1 - usd_1

def test_money_multiply():
    eur = Currency('EUR')
    eur_2 = Money(2, eur)
    eur_5 = Money(5, eur)
    assert eur_2 * eur_5 == Money(10, Currency('EUR'))
    assert eur_2 * 5 == Money(10, Currency('EUR'))
    assert 2 * eur_5 == Money(10, Currency('EUR'))
    usd = Currency('USD')
    usd_1 = Money(1, usd)
    with pytest.raises(TypeError):
        eur_2 * usd_1

def test_money_divide():
    eur = Currency('EUR')
    eur_2 = Money(2, eur)
    eur_4 = Money(4, eur)
    assert eur_4 / eur_2 == Money(2, Currency('EUR'))
    assert eur_4 / 2 == Money(2, Currency('EUR'))
    assert 2 / eur_4 == Money(0.5, Currency('EUR'))
    usd = Currency('USD')
    usd_1 = Money(1, usd)
    with pytest.raises(TypeError):
        eur_2 / usd_1