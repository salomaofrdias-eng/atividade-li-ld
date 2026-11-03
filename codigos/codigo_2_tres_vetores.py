# Código 2: dados três vetores de R³, julga se o conjunto é LI ou LD.
#
# Critério: montamos a matriz 3x3 com os vetores nas linhas.
# Se det = 0, o conjunto é LD. Se det ≠ 0, o conjunto é LI.

from fractions import Fraction


def ler_vetor(nome):
    """Lê um vetor de R³. Aceita inteiros, decimais e frações. Ex.: 1 0,5 2/3"""
    while True:
        texto = input(f"Digite as 3 coordenadas de {nome}, separadas por espaço: ")
        try:
            vetor = [Fraction(x.replace(",", ".")) for x in texto.split()]
        except (ValueError, ZeroDivisionError):
            print("Entrada inválida. Use números separados por espaço. Ex.: 1 0,5 2/3")
            continue
        if len(vetor) == 3:
            return vetor
        print("Entrada inválida. O vetor precisa ter exatamente 3 coordenadas.")


def determinante(u, v, w):
    """Determinante 3x3 por cofatores, expandindo pela primeira linha."""
    return (
        u[0] * (v[1] * w[2] - v[2] * w[1])
        - u[1] * (v[0] * w[2] - v[2] * w[0])
        + u[2] * (v[0] * w[1] - v[1] * w[0])
    )


def julgar_tres_vetores(u, v, w):
    det = determinante(u, v, w)
    return ("LD" if det == 0 else "LI"), det


if __name__ == "__main__":
    u = ler_vetor("u")
    v = ler_vetor("v")
    w = ler_vetor("w")
    resultado, det = julgar_tres_vetores(u, v, w)

    print(f"\ndet = {det}")
    print(f"Resultado: o conjunto de vetores é {resultado}.")
