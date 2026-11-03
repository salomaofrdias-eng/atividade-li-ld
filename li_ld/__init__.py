"""Sistema para julgar dependência linear (LI ou LD) de vetores em R³."""

from .operacoes import determinante, formatar, produto_vetorial
from .dois_vetores import julgar_dois_vetores
from .tres_vetores import julgar_tres_vetores

__all__ = [
    "determinante",
    "formatar",
    "produto_vetorial",
    "julgar_dois_vetores",
    "julgar_tres_vetores",
]
