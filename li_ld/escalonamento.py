"""Extra: LI ou LD por escalonamento (2 ou 3 vetores de R³).

Escalona a matriz com os vetores nas linhas. posto = nº de vetores -> LI; posto menor -> LD.
"""

from .entrada import ler_vetor


def escalonar(vetores):
    """Escalona a matriz com os vetores nas linhas. Retorna (matriz, passos)."""
    m = [list(v) for v in vetores]
    passos = []
    linha = 0
    for col in range(3):
        if linha == len(m):
            break
        pivo = next((i for i in range(linha, len(m)) if m[i][col] != 0), None)
        if pivo is None:
            continue
        if pivo != linha:
            m[linha], m[pivo] = m[pivo], m[linha]
            passos.append(f"L{linha + 1} <-> L{pivo + 1}")
        for i in range(linha + 1, len(m)):
            if m[i][col] != 0:
                fator = m[i][col] / m[linha][col]
                m[i] = [a - fator * b for a, b in zip(m[i], m[linha])]
                passos.append(f"L{i + 1} = L{i + 1} - ({fator})*L{linha + 1}")
        linha += 1
    return m, passos


def posto(matriz):
    """Número de linhas não nulas de uma matriz escalonada."""
    return sum(1 for linha in matriz if any(x != 0 for x in linha))


def julgar_por_escalonamento(vetores):
    """Retorna ("LI" ou "LD", posto, matriz escalonada, passos)."""
    m, passos = escalonar(vetores)
    r = posto(m)
    return ("LI" if r == len(vetores) else "LD"), r, m, passos


def _formatar(vetor):
    return "[" + ", ".join(str(x) for x in vetor) + "]"


def _ler_quantidade():
    while True:
        texto = input("Quantos vetores (2 ou 3)? ").strip()
        if texto in ("2", "3"):
            return int(texto)
        print("Entrada inválida. Digite 2 ou 3.")


def executar():
    print("\n--- Escalonamento (extra) ---")
    n = _ler_quantidade()
    vetores = [ler_vetor(nome) for nome in ["u", "v", "w"][:n]]
    resultado, r, m, passos = julgar_por_escalonamento(vetores)

    print("\nOperações:")
    for p in passos or ["(nenhuma, a matriz já está escalonada)"]:
        print("  " + p)
    print("Matriz escalonada:")
    for linha in m:
        print("  " + _formatar(linha))
    print(f"Posto = {r} (de {n} vetores)")
    print(f"Resultado: o conjunto de vetores é {resultado}.")
