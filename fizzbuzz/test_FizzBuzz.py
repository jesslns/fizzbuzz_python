from fizzbuzz import FizzBuzz


def test_divisibleByThree():
    assert FizzBuzz.divisibleByThree(6) == "Fizz"
    assert FizzBuzz.divisibleByThree(21) == "Fizz"


def test_notDivisibleByThree():
    assert FizzBuzz.divisibleByThree(8) == 8
    assert FizzBuzz.divisibleByThree(14) == 14

def test_divideByFive():
    assert FizzBuzz.divisibleByFive(20) == "Buzz"
    assert FizzBuzz.divisibleByFive(25) == "Buzz"

def test_notDivideByFive():
    assert FizzBuzz.divisibleByFive(13) == 13
    assert FizzBuzz.divisibleByFive(11) == 11

    
