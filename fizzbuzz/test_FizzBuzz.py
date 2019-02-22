from fizzbuzz import FizzBuzz


def test_divisibleByThree():
    assert FizzBuzz.divisibleByThree(6) == "Fizz"

def test_notDivisibleByThree():
    assert FizzBuzz.divisibleByThree(8) == 8

def test_divideByFive():
    assert FizzBuzz.divisibleByThree(20) == "Buzz"

def test_notDivideByFive():
    assert FizzBuzz.divisibleByThree(13) == 13
