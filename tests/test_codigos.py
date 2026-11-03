"""Garante que os scripts autocontidos de codigos/ (os mesmos do PDF e do Colab) funcionam."""

import importlib.util
import os
import subprocess
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / "codigos"


def carregar(arquivo):
    spec = importlib.util.spec_from_file_location(arquivo[:-3], PASTA / arquivo)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def rodar(arquivo, entrada):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    proc = subprocess.run(
        [sys.executable, str(PASTA / arquivo)],
        input=entrada, capture_output=True, text=True, encoding="utf-8", env=env,
    )
    return proc.stdout


class TestCodigo1(unittest.TestCase):
    def test_funcao(self):
        m = carregar("codigo_1_dois_vetores.py")
        self.assertEqual(m.julgar_dois_vetores([F(1), F(2), F(3)], [F(2), F(4), F(6)])[0], "LD")
        self.assertEqual(m.julgar_dois_vetores([F(1), F(0), F(2)], [F(0), F(1), F(1)])[0], "LI")

    def test_execucao_ld(self):
        saida = rodar("codigo_1_dois_vetores.py", "1 2 3\n2 4 6\n")
        self.assertIn("u x v = (0, 0, 0)", saida)
        self.assertIn("os vetores são LD.", saida)

    def test_execucao_li(self):
        saida = rodar("codigo_1_dois_vetores.py", "1 0 2\n0 1 1\n")
        self.assertIn("u x v = (-2, -1, 1)", saida)
        self.assertIn("os vetores são LI.", saida)

    def test_entrada_invalida_pede_de_novo(self):
        saida = rodar("codigo_1_dois_vetores.py", "1 2\nabc\n1 2 3\n2 4 6\n")
        self.assertEqual(saida.count("Entrada inválida"), 2)
        self.assertIn("os vetores são LD.", saida)


class TestCodigo2(unittest.TestCase):
    def test_funcao(self):
        m = carregar("codigo_2_tres_vetores.py")
        v = lambda *xs: [F(x) for x in xs]
        self.assertEqual(m.julgar_tres_vetores(v(1, 2, 3), v(4, 5, 6), v(7, 8, 9)), ("LD", 0))
        self.assertEqual(m.julgar_tres_vetores(v(1, 0, 0), v(0, 1, 0), v(0, 0, 1)), ("LI", 1))

    def test_execucao_li(self):
        saida = rodar("codigo_2_tres_vetores.py", "1 2 3\n4 5 6\n7 8 10\n")
        self.assertIn("det = -3", saida)
        self.assertIn("o conjunto de vetores é LI.", saida)

    def test_execucao_ld(self):
        saida = rodar("codigo_2_tres_vetores.py", "1 2 3\n4 5 6\n7 8 9\n")
        self.assertIn("det = 0", saida)
        self.assertIn("o conjunto de vetores é LD.", saida)


if __name__ == "__main__":
    unittest.main()
