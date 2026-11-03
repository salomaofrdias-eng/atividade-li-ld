"""Leitura e validação de vetores digitados pelo usuário."""

from fractions import Fraction


def parse_vetor(texto):
    """Converte um texto como '1 0,5 2/3' em uma lista de 3 Fractions.

    Aceita inteiros, decimais (com ponto ou vírgula) e frações.
    Levanta ValueError se algum valor for inválido ou se não houver 3 coordenadas.
    """
    try:
        vetor = [Fraction(x.replace(",", ".")) for x in texto.split()]
    except (ValueError, ZeroDivisionError):
        raise ValueError("Use números separados por espaço. Ex.: 1 0,5 2/3") from None
    if len(vetor) != 3:
        raise ValueError("O vetor precisa ter exatamente 3 coordenadas.")
    return vetor


def ler_vetor(nome):
    """Pede um vetor ao usuário até receber uma entrada válida."""
    while True:
        texto = input(f"Digite as 3 coordenadas de {nome}, separadas por espaço: ")
        try:
            return parse_vetor(texto)
        except ValueError as erro:
            print(f"Entrada inválida. {erro}")
