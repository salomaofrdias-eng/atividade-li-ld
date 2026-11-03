"""Código 1: dois vetores de R³ são LI ou LD?

Critério: u e v são LD se, e somente se, u x v = (0, 0, 0).
"""

from .entrada import ler_vetor
from .operacoes import formatar, produto_vetorial


def julgar_dois_vetores(u, v):
    """Retorna ("LI" ou "LD", u x v)."""
    w = produto_vetorial(u, v)
    return ("LD" if all(x == 0 for x in w) else "LI"), w


def executar():
    print("\n--- Dois vetores de R³ ---")
    u = ler_vetor("u")
    v = ler_vetor("v")
    resultado, w = julgar_dois_vetores(u, v)

    print(f"\nu x v = {formatar(w)}")
    print(f"Resultado: os vetores são {resultado}.")
