"""Operações com vetores de R³. Usa Fraction, então os cálculos são exatos."""


def produto_vetorial(u, v):
    """Produto vetorial u x v."""
    return [
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0],
    ]


def determinante(u, v, w):
    """Determinante 3x3 (vetores nas linhas), por cofatores na primeira linha."""
    return (
        u[0] * (v[1] * w[2] - v[2] * w[1])
        - u[1] * (v[0] * w[2] - v[2] * w[0])
        + u[2] * (v[0] * w[1] - v[1] * w[0])
    )


def formatar(vetor):
    """Texto no formato (a, b, c)."""
    return "(" + ", ".join(str(x) for x in vetor) + ")"
