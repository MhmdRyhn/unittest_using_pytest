# ------ This script uses Parametrized Test Functions -------

import pytest

from bank.account import Account, InsufficientBalance


@pytest.mark.parametrize(
    "initial,added,withdrawn,remaining", 
    [
        (0, 10, 5, 5), 
        (12, 3, 5, 10), 
        (9, 8, 11, 6)
    ]
)
def test_transactions(initial, added, withdrawn, remaining):
    account = Account(initial)
    account.add_cash(added)
    account.withdraw_cash(withdrawn)
    assert account.balance == remaining
