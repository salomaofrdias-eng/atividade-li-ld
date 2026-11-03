"""Sistema de dependência linear em R³ (LI ou LD).

Uso:
    python main.py
"""

from li_ld import dois_vetores, escalonamento, tres_vetores

MENU = """
=== Dependência linear em R³ ===
[1] Dois vetores   (LI ou LD)
[2] Três vetores   (LI ou LD)
[3] Escalonamento (extra: 2 ou 3 vetores)
[0] Sair
"""


def main():
    opcoes = {
        "1": dois_vetores.executar,
        "2": tres_vetores.executar,
        "3": escalonamento.executar,
    }
    while True:
        print(MENU)
        try:
            escolha = input("Escolha uma opção: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if escolha == "0":
            break
        acao = opcoes.get(escolha)
        if acao is None:
            print("Opção inválida. Digite 1, 2, 3 ou 0.")
            continue
        try:
            acao()
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada interrompida.")
            break
    print("Até logo!")


if __name__ == "__main__":
    main()
