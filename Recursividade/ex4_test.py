import unittest
from ex4 import calcular_fatorial


def test_fatorial1():
    assert calcular_fatorial(4) == 24
    print('OK - 1')


def test_fatorial2():
    assert calcular_fatorial(0) == 1
    print('OK - 2')


if __name__ == '__main__':
    test_fatorial1()
    test_fatorial2()
