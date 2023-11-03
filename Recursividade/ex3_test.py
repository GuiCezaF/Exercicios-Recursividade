import unittest
from ex3 import palindromo_frase


def test_palindromo1():
    assert palindromo_frase('olha que bacana') == False
    print('OK - 1')


def test_palindromo2():
    assert palindromo_frase('A mala nada na lama') == True
    print('OK - 2')


def test_palindromo3():
    assert palindromo_frase('') == True
    print('OK - 3')


if __name__ == '__main__':
    test_palindromo1()
    test_palindromo2()
    test_palindromo3()
