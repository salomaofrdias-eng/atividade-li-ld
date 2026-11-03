# Atividade: dependência linear (LI/LD) em R³

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1MtnTAuxW-dR9oEXj7ojE2VY0UhK6vztv?usp=sharing)

Trabalho de **Álgebra Linear**, Prof. Dr. Flausino Spindola.

**Alunos:** Cauã Barros (matrícula 20240045292) · Salomão Ferreira Dias (matrícula 2023030256)
**Link do Colab:** <https://colab.research.google.com/drive/1MtnTAuxW-dR9oEXj7ojE2VY0UhK6vztv?usp=sharing>
**Repositório:** <https://github.com/salomaofrdias-eng/atividade-li-ld>

Programa em Python que julga se vetores de R³ são **linearmente independentes (LI)** ou
**linearmente dependentes (LD)**:

1. **Código 1:** dados dois vetores de R³, diz se são LI ou LD.
2. **Código 2:** dados três vetores de R³, diz se o conjunto é LI ou LD.
3. **Extra (fora do enunciado):** a mesma verificação por escalonamento, para 2 ou 3 vetores.

Usa só a biblioteca padrão do Python 3 (nenhuma instalação necessária). Os cálculos usam
`fractions.Fraction`, então são **exatos**: `0,1 0,2 0,3` e `1 2 3` são reconhecidos como LD sem erro de ponto flutuante.

## Como funciona

| Caso | Critério | Resultado |
|---|---|---|
| 2 vetores `u`, `v` | produto vetorial `u × v` | `u × v = (0,0,0)` → **LD**; caso contrário → **LI** |
| 3 vetores `u`, `v`, `w` | determinante da matriz 3×3 com os vetores nas linhas | `det = 0` → **LD**; `det ≠ 0` → **LI** |
| 2 ou 3 vetores (extra) | escalonamento da matriz com os vetores nas linhas | posto = nº de vetores → **LI**; posto menor → **LD** |

O vetor nulo é tratado automaticamente: com ele, o produto vetorial, o determinante e o posto indicam dependência, e o conjunto é LD.
Os testes comparam o escalonamento com os Códigos 1 e 2 em 500 casos aleatórios, e os resultados sempre coincidem.

## Estrutura do repositório

```
atividade-li-ld/
├── main.py                  # sistema com menu (opções 1, 2, 3 e 0)
├── li_ld/                   # pacote do sistema
│   ├── entrada.py           #   leitura e validação dos vetores
│   ├── operacoes.py         #   produto vetorial, determinante, formatação
│   ├── dois_vetores.py      #   Código 1 (lógica + execução)
│   ├── tres_vetores.py      #   Código 2 (lógica + execução)
│   └── escalonamento.py     #   extra: LI/LD por escalonamento
├── codigos/                 # versões autocontidas (as mesmas do PDF e do Colab)
│   ├── codigo_1_dois_vetores.py
│   ├── codigo_2_tres_vetores.py
│   └── extra_escalonamento.py
├── notebooks/
│   └── atividade_LI_LD.ipynb  # notebook para abrir no Google Colab
├── tests/                   # testes automatizados (unittest)
├── docs/
│   ├── enunciado.pdf
│   └── atividade_LI_LD.pdf  # PDF de entrega com os códigos
└── README.md
```

## Como executar

**Sistema com menu:**

```bash
python main.py
```

**Cada código separado:**

```bash
python codigos/codigo_1_dois_vetores.py
python codigos/codigo_2_tres_vetores.py
python codigos/extra_escalonamento.py
```

**Testes:**

```bash
python -m unittest -v
```

**Google Colab:** o notebook está em
<https://colab.research.google.com/drive/1MtnTAuxW-dR9oEXj7ojE2VY0UhK6vztv?usp=sharing>.
Também dá para abrir direto do GitHub, sem upload:

<https://colab.research.google.com/github/salomaofrdias-eng/atividade-li-ld/blob/main/notebooks/atividade_LI_LD.ipynb>

## Exemplos

```
Digite as 3 coordenadas de u, separadas por espaço: 1 2 3
Digite as 3 coordenadas de v, separadas por espaço: 2 4 6

u x v = (0, 0, 0)
Resultado: os vetores são LD.
```

```
Digite as 3 coordenadas de u, separadas por espaço: 1 2 3
Digite as 3 coordenadas de v, separadas por espaço: 4 5 6
Digite as 3 coordenadas de w, separadas por espaço: 7 8 10

det = -3
Resultado: o conjunto de vetores é LI.
```

Extra, por escalonamento, com `(1,2,3)`, `(4,5,6)`, `(7,8,9)`:

```
Operações:
  L2 = L2 - (4)*L1
  L3 = L3 - (7)*L1
  L3 = L3 - (2)*L2
Matriz escalonada:
  [1, 2, 3]
  [0, -3, -6]
  [0, 0, 0]
Posto = 2 (de 3 vetores)
Resultado: o conjunto de vetores é LD.
```

| Entrada | Resultado |
|---|---|
| `u=(1,2,3)`, `v=(2,4,6)` | `u×v=(0,0,0)` → LD |
| `u=(1,0,2)`, `v=(0,1,1)` | `u×v=(-2,-1,1)` → LI |
| `u=(0,0,0)`, `v=(1,2,3)` | `u×v=(0,0,0)` → LD |
| `(1,0,0)`, `(0,1,0)`, `(0,0,1)` | `det=1` → LI |
| `(1,2,3)`, `(4,5,6)`, `(7,8,9)` | `det=0` → LD |
| `(1,2,3)`, `(4,5,6)`, `(7,8,10)` | `det=-3` → LI |

## Atualizar o repositório

```bash
git clone https://github.com/salomaofrdias-eng/atividade-li-ld.git
cd atividade-li-ld
# (copie os arquivos novos para esta pasta)
git add .
git commit -m "Atualiza atividade LI/LD"
git push
```
