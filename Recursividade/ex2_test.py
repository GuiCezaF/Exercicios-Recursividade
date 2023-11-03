import unittest
from ex2 import palindromo


def test_palindromo1():
    assert palindromo('ovo') == True
    print('OK - 1')


def test_palindromo2():
    assert palindromo('ola') == False
    print('OK - 2')


def test_palindromo3():
    assert palindromo('') == True
    print('OK - 3')


if __name__ == '__main__':
    test_palindromo1()
    test_palindromo2()
    test_palindromo3()
