fibonacci = [0, 1]


def fib(n: list) -> list:
    '''Calcula o n-ésimo termo da série de Fibonacci.'''
    if n >= len(fibonacci):
        for i in range(len(fibonacci), n + 1):
            fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])

    return fibonacci[n]


for i in range(100):
    print('fib ' + str(i) + ': ' + str(fib(i)))
