from fizzbuzz import FizzBuzz


def test_divisibleByThree():
    assert FizzBuzz.divisibleByThree(6) == "Fizz"
    assert FizzBuzz.divisibleByThree(21) == "Fizz"

# 
# def test_notDivisibleByThree():
#     assert FizzBuzz.divisibleByThree(8) == 8
#     assert FizzBuzz.divisibleByThree(14) == 14
#
# def test_divisibleByFive():
#     assert FizzBuzz.divisibleByFive(20) == "Buzz"
#     assert FizzBuzz.divisibleByFive(25) == "Buzz"
#
# def test_notDivisibleByFive():
#     assert FizzBuzz.divisibleByFive(13) == 13
#     assert FizzBuzz.divisibleByFive(11) == 11
#
# def test_divisibleByThreeAndFive():
#     assert FizzBuzz.divisibleByThreeAndFive(15) == "FizzBuzz"
#     assert FizzBuzz.divisibleByThreeAndFive(30) == "FizzBuzz"
#
# def test_notDivisibleByThreeAndFive():
#     assert FizzBuzz.divisibleByThreeAndFive(19) == 19
#     assert FizzBuzz.divisibleByThreeAndFive(7) == 7
#     assert FizzBuzz.divisibleByThreeAndFive(10) == 10

def test_fizzbuzz():
    assert FizzBuzz.fizzbuzz(1) == 1
    assert FizzBuzz.fizzbuzz(3) == "Fizz"
    assert FizzBuzz.fizzbuzz(5) == "Buzz"
    assert FizzBuzz.fizzbuzz(15) == "FizzBuzz"
    assert FizzBuzz.fizzbuzz(19) == 19
    assert FizzBuzz.fizzbuzz(30) == "FizzBuzz"
    assert FizzBuzz.fizzbuzz(25) == "Buzz"
