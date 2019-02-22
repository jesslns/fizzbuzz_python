from fizzbuzz import FizzBuzz


def test_divisibleByThree():
    assert FizzBuzz.divisibleByThree(6) == "Fizz"

def test_notDivisibleByThree():
    assert FizzBuzz.divisibleByThree(8) == 8
