import unittest
from ex1 import string_inversa


def teste_inversa():
    assert string_inversa('alo') == 'ola'
    print('OK - 1')


def teste_string_vazia():
    assert string_inversa('') == ''
    print('OK - 2')


if __name__ == '__main__':
    teste_inversa()
    teste_string_vazia()
