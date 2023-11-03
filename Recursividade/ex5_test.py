import unittest
from ex5 import fib


def teste_sequencia_fibonacci():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(7) == 13
    assert fib(8) == 21


def teste_de_numeros_longos():
    assert fib(20) == 6765


if __name__ == '__main__':
    teste_sequencia_fibonacci()
    teste_de_numeros_longos()
    print("All tests passed!")
