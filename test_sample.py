import pytest
from main import BankAccount

def test_initial_balance():
    account = BankAccount(100)
    assert account.get_balance() == 100

def test_deposit():
    account = BankAccount(0)
    result = account.deposit(50)
    assert result == True
    assert account.get_balance() == 50

def test_withdraw():
    account = BankAccount(100)
    result = account.withdraw(40)
    assert result == True
    assert account.get_balance() == 60

def test_insufficient_funds():
    account = BankAccount(50)
    result = account.withdraw(100)
    assert result == False
    assert account.get_balance() == 50