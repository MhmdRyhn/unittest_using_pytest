import pytest

from bank.account import Account, InsufficientBalance


def test_default_initial_amount():
    account = Account()
    assert account.balance == 0


def test_withdraw_insufficient_amount():
    account = Account()
    # When a function raises some Exception, use this way
    with pytest.raises(InsufficientBalance):
        account.withdraw_cash(5)