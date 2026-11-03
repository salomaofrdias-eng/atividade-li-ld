# EXTRA (não faz parte do enunciado): julga LI ou LD por escalonamento.
#
# Critério: colocamos os vetores nas linhas de uma matriz e escalonamos.
# O posto é o número de linhas não nulas da matriz escalonada.
# Se posto = quantidade de vetores, o conjunto é LI. Se posto < quantidade, é LD.
# Funciona para 2 ou 3 vetores de R³ e confirma os resultados dos Códigos 1 e 2.

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


def ler_quantidade():
    while True:
        texto = input("Quantos vetores (2 ou 3)? ").strip()
        if texto in ("2", "3"):
            return int(texto)
        print("Entrada inválida. Digite 2 ou 3.")


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
    return sum(1 for linha in matriz if any(x != 0 for x in linha))


def julgar_por_escalonamento(vetores):
    m, passos = escalonar(vetores)
    r = posto(m)
    return ("LI" if r == len(vetores) else "LD"), r, m, passos


def formatar(vetor):
    return "[" + ", ".join(str(x) for x in vetor) + "]"


if __name__ == "__main__":
    n = ler_quantidade()
    nomes = ["u", "v", "w"][:n]
    vetores = [ler_vetor(nome) for nome in nomes]
    resultado, r, m, passos = julgar_por_escalonamento(vetores)

    print("\nOperações:")
    for p in passos or ["(nenhuma, a matriz já está escalonada)"]:
        print("  " + p)
    print("Matriz escalonada:")
    for linha in m:
        print("  " + formatar(linha))
    print(f"Posto = {r} (de {n} vetores)")
    print(f"Resultado: o conjunto de vetores é {resultado}.")
