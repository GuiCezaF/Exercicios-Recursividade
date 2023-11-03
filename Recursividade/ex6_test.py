import unittest
from ex6 import soma_n_primeiros_numeros


def test_soma1():
    assert soma_n_primeiros_numeros(4) == 10
    print('OK - 1')


def test_soma2():
    assert soma_n_primeiros_numeros(1) == 1
    print('OK - 2')


def test_soma3():
    assert soma_n_primeiros_numeros(0) == 'Apenas numeros maiores que 0'
    print('OK - 3')


if __name__ == '__main__':
    test_soma1()
    test_soma2()
    test_soma3()
