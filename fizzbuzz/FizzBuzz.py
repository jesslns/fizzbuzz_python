import pytest

def divisibleByThree(number):
    if number % 3 == 0:
        return "Fizz"
    else:
        return number

def divisibleByFive(number):
    if number % 5 == 0:
        return "Buzz"
    else:
        return number
