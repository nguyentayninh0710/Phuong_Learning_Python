'''
Overview of OOP in Python

Comparing Java vs Python

Java: strongly typed, need to declare class, public/private, fixed constructor.

Python: dynamically typed, flexible class, no public/private keyword (use convention _), constructor with __init__.

4 OOP properties:

Encapsulation

Inheritance

Polymorphism

Abstraction
'''

# 1) Encapsulation demo (BankAccount)
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Optional, Iterable
from abc import ABC, abstractmethod
from math import pi
""" Encapsulation: protect the balance and access via methods. 
In Python, name-mangling using __balance helps discourage direct access. 
"""
class BankAccont:
    '''
    public BankAccont(String owner, float balance){
        this.owner = owner;
        this.balance = balance;
    }
    '''
    def __init__(self, owner: str, opening_balance: float = 0.0):
        self.owner = owner
        self.__balance = float(opening_balance)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("amount must be positive")
        else:
            self.__balance += amount
    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("amount must be positive")
        elif amount > self.__balance:
            raise ValueError("can not withdraw")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def __repr__(self): 
        return f"Bank acount owner = {self.owner}, balance = {self.__balance}"


print("\n=== 1) Encapsulation: BankAccount ===")
acc = BankAccont("Phuong", 100.0)
print("initial: ",  acc)

acc.deposit(50)

print("After diposit: ",  acc)

acc.withdraw(10)

print("After withdraw: ",  acc)



    