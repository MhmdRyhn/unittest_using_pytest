# -------- This script uses pytest Fixtures -------------
# In test_simple.py script, we need to create Account 
# object in each test function. To avoid this, pytest
# fixture is here to help us.

import pytest

from bank.account import Account, InsufficientBalance


@pytest.fixture
def empty_account():
    """
    Returns an Account instance with a zero balance
    """
    return Account()


@pytest.fixture
def account():
    """
    Returns an Account instance with a balance of 10
    """
    return Account(10)


def test_default_initial_amount(empty_account):
    assert empty_account.balance == 0


def test_setting_the_initial_amount(account):
    assert account.balance == 10


def test_account_add_cash(account):
    account.add_cash(5)
    assert account.balance == 15


def test_account_withdraw_cash(account):
    account.withdraw_cash(5)
    assert account.balance == 5


def test_withdraw_insufficient_amount(empty_account):
    # When a function raises some Exception, use this way
    with pytest.raises(InsufficientBalance):
        empty_account.withdraw_cash(5)
