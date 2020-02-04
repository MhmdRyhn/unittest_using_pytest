# This script uses Parametrize Test Functions
# along with pytest fixture

import pytest

from bank.account import Account, InsufficientBalance


@pytest.fixture
def my_account():
    """
    Returns an Account instance with a balance of 20
    """
    return Account(20)


@pytest.mark.parametrize(
    "added,withdrawn,remaining", 
    [
        (10, 25, 5), 
        (3, 10, 13), 
        (8, 11, 17)
    ]
)
def test_transactions(my_account, added, withdrawn, remaining):
    my_account.add_cash(added)
    my_account.withdraw_cash(withdrawn)
    assert my_account.balance == remaining


@pytest.mark.parametrize(
    "added,withdrawn", 
    [
        (5, 26), 
        (3, 100), 
        (8, 31)
    ]
)
def test_invalid_transactions(my_account, added, withdrawn):
    my_account.add_cash(added)
    with pytest.raises(InsufficientBalance):
        my_account.withdraw_cash(withdrawn)
