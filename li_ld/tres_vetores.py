"""Código 2: três vetores de R³ formam um conjunto LI ou LD?

Critério: com os vetores nas linhas de uma matriz 3x3, det = 0 <=> LD.
"""

from .entrada import ler_vetor
from .operacoes import determinante


def julgar_tres_vetores(u, v, w):
    """Retorna ("LI" ou "LD", determinante)."""
    det = determinante(u, v, w)
    return ("LD" if det == 0 else "LI"), det


def executar():
    print("\n--- Três vetores de R³ ---")
    u = ler_vetor("u")
    v = ler_vetor("v")
    w = ler_vetor("w")
    resultado, det = julgar_tres_vetores(u, v, w)

    print(f"\ndet = {det}")
    print(f"Resultado: o conjunto de vetores é {resultado}.")
