import unittest
from tests.fizzBuzz import fizzBuzz

def fizzBuzz(value):
    if (value % 3) == 0:
        return "Fizz"
    if (value % 5) == 0:
        return "Buzz"
    if (value % 15) == 0:
        return "FizzBuzz"
    return str(value)