from fizzbuzz import FizzBuzz


def test_divisibleByThree():
    assert FizzBuzz.divisibleByThree(6) == "Fizz"
    assert FizzBuzz.divisibleByThree(21) == "Fizz"


def test_notDivisibleByThree():
    assert FizzBuzz.divisibleByThree(8) == 8
    assert FizzBuzz.divisibleByThree(14) == 14

def test_divisibleByFive():
    assert FizzBuzz.divisibleByFive(20) == "Buzz"
    assert FizzBuzz.divisibleByFive(25) == "Buzz"

def test_notDivisibleByFive():
    assert FizzBuzz.divisibleByFive(13) == 13
    assert FizzBuzz.divisibleByFive(11) == 11

def test_divisibleByThreeAndFive():
    assert FizzBuzz.divisibleByThreeAndFive(15) == "FizzBuzz"
    assert FizzBuzz.divisibleByThreeAndFive(30) == "FizzBuzz"

def test_notDivisibleByThreeAndFive():
    assert FizzBuzz.divisibleByThreeAndFive(19) == 19
    assert FizzBuzz.divisibleByThreeAndFive(7) == 7
