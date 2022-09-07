import pytest
import main

def test_fib_1():
    assert main.fib(5) == [0, 1, 1, 2, 3, 5]


def test_fib_2():
    assert main.fib(1) == [0, 1, 1]
