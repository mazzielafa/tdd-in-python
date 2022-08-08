from multiprocessing.sharedctypes import Value
import unittest

def fizzBuzz(value):
    if (value % 3) == 0:
        return "Fizz"
    if (value % 5) == 0:
        return "Buzz"
    # if (value % 15) == 0:
    #     return "FizzBuzz"
    return str(value)

# defining what outcome I want the values to do.
def checkReturnVal(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal
    

def test_return1():
    checkReturnVal(1, "1")
    
def test_return2():
    checkReturnVal(2, "2")

def test_return3():
    checkReturnVal(3, "Fizz")

def test_return5():
    checkReturnVal(5, "Buzz")

def test_return6():
    checkReturnVal(6, "Fizz")

def test_return10():
    checkReturnVal(10, "Buzz")

def test_return15():
    checkReturnVal(15, "FizzBuzz")