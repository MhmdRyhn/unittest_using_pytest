import pytest

from bank.account import Account, InsufficientBalance


def test_default_initial_amount():
    account = Account()
    assert account.balance == 0


def test_setting_the_initial_amount():
    account = Account(10)
    assert account.balance == 10


def test_account_add_cash():
    account = Account(10)
    account.add_cash(5)
    assert account.balance == 15


def test_account_withdraw_cash():
    account = Account(10)
    account.withdraw_cash(5)
    assert account.balance == 5


def test_withdraw_insufficient_amount():
    account = Account()
    # When a function raises some Exception, use this way
    with pytest.raises(InsufficientBalance):
        account.withdraw_cash(5)