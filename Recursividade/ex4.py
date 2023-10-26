def calcular_fatorial(num: int):
    if num == 0:
        return 1
    if num > 0:
        return num * calcular_fatorial(num - 1)

    return "Fatorial indefinido para números negativos"


numero = 5
resultado = calcular_fatorial(numero)
print(f'O fatorial de {numero} é {resultado}')
