import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount


@pytest.fixture
def zero_bank_account():
    print("Creating empty bank account")
    return BankAccount()

@pytest.fixture
def bank_account():
    print("Creating bank account with initial balance")
    return BankAccount(50)

@pytest.mark.parametrize("num1,num2,expected", [
    (3, 2, 5),
    (7, 1, 8),
    (12,4,16),
])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected

def test_subtract():
    assert subtract(3, 2) == 1

def test_multiply():
    assert multiply(3, 2) == 6

def test_divide():
    assert divide(6, 2) == 3


def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_withdraw(zero_bank_account):
    print("testing my bank account")
    assert zero_bank_account.balance == 00

def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70

def test_collect_interest(bank_account):
    bank_account.collect_interest(0.1)
    assert round(bank_account.balance, 6) == 55

@pytest.mark.parametrize("deposited,withdrew,expected", [
    (200, 100, 100),
    (300, 200, 100),
    (1400, 300, 1100),

])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
        with pytest.raises(Exception):
            bank_account.withdraw(200)