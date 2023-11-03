
'''
Escreva uma função recursiva que some os n primeiros números.
'''


def soma_n_primeiros_numeros(n: int):
    if n < 1:
        return 'Apenas numeros maiores que 0'
    elif n == 1:
        return 1
    else:
        return n + soma_n_primeiros_numeros(n - 1)


n = 5
resultado = soma_n_primeiros_numeros(n)
print(f'A soma dos primeiros {n} números é {resultado}')
