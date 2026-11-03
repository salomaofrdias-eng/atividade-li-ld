# Código 1: dados dois vetores de R³, julga se são LI ou LD.
#
# Critério: dois vetores são LD se, e somente se, um é múltiplo do outro.
# Em R³, isso equivale a u x v = (0, 0, 0). Se o produto vetorial não for nulo, são LI.
# O caso com vetor nulo já está incluído, pois nele o produto vetorial também dá zero.

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


def produto_vetorial(u, v):
    return [
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0],
    ]


def formatar(vetor):
    return "(" + ", ".join(str(x) for x in vetor) + ")"


def julgar_dois_vetores(u, v):
    w = produto_vetorial(u, v)
    return ("LD" if w == [0, 0, 0] else "LI"), w


if __name__ == "__main__":
    u = ler_vetor("u")
    v = ler_vetor("v")
    resultado, w = julgar_dois_vetores(u, v)

    print(f"\nu x v = {formatar(w)}")
    print(f"Resultado: os vetores são {resultado}.")
