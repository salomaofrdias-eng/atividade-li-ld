"""Testes do extra por escalonamento, incluindo comparação com o produto vetorial e o determinante."""

import os
import random
import subprocess
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

from li_ld import julgar_dois_vetores, julgar_tres_vetores
from li_ld.escalonamento import escalonar, julgar_por_escalonamento, posto

RAIZ = Path(__file__).resolve().parent.parent


def vet(*xs):
    return [F(x) for x in xs]


class TestEscalonamento(unittest.TestCase):
    def test_dois_vetores(self):
        self.assertEqual(julgar_por_escalonamento([vet(1, 2, 3), vet(2, 4, 6)])[:2], ("LD", 1))
        self.assertEqual(julgar_por_escalonamento([vet(1, 0, 2), vet(0, 1, 1)])[:2], ("LI", 2))
        self.assertEqual(julgar_por_escalonamento([vet(0, 0, 0), vet(1, 2, 3)])[:2], ("LD", 1))

    def test_tres_vetores(self):
        self.assertEqual(julgar_por_escalonamento([vet(1, 0, 0), vet(0, 1, 0), vet(0, 0, 1)])[:2], ("LI", 3))
        self.assertEqual(julgar_por_escalonamento([vet(1, 2, 3), vet(4, 5, 6), vet(7, 8, 9)])[:2], ("LD", 2))
        self.assertEqual(julgar_por_escalonamento([vet(1, 2, 3), vet(4, 5, 6), vet(7, 8, 10)])[:2], ("LI", 3))

    def test_troca_de_linhas_quando_pivo_e_zero(self):
        m, passos = escalonar([vet(0, 1, 0), vet(1, 0, 0)])
        self.assertEqual(m, [vet(1, 0, 0), vet(0, 1, 0)])
        self.assertIn("L1 <-> L2", passos)

    def test_matriz_resultante_e_escalonada(self):
        m, _ = escalonar([vet(2, 1, 3), vet(4, 2, 7), vet(1, 5, 1)])
        pivos = [next((j for j, x in enumerate(l) if x != 0), 3) for l in m]
        self.assertEqual(pivos, sorted(pivos))  # pivôs avançam para a direita
        self.assertEqual(posto(m), 3)

    def test_concorda_com_produto_vetorial_e_determinante(self):
        rng = random.Random(2026)
        for _ in range(500):
            u, v, w = ([F(rng.randint(-2, 2)) for _ in range(3)] for _ in range(3))
            self.assertEqual(julgar_por_escalonamento([u, v])[0], julgar_dois_vetores(u, v)[0], (u, v))
            self.assertEqual(julgar_por_escalonamento([u, v, w])[0], julgar_tres_vetores(u, v, w)[0], (u, v, w))


class TestScriptExtra(unittest.TestCase):
    def rodar(self, entrada):
        env = dict(os.environ, PYTHONIOENCODING="utf-8")
        proc = subprocess.run(
            [sys.executable, str(RAIZ / "codigos" / "extra_escalonamento.py")],
            input=entrada, capture_output=True, text=True, encoding="utf-8", env=env,
        )
        return proc.stdout

    def test_tres_vetores_ld(self):
        saida = self.rodar("3\n1 2 3\n4 5 6\n7 8 9\n")
        self.assertIn("Posto = 2 (de 3 vetores)", saida)
        self.assertIn("é LD.", saida)

    def test_dois_vetores_li(self):
        saida = self.rodar("2\n1 0 2\n0 1 1\n")
        self.assertIn("Posto = 2 (de 2 vetores)", saida)
        self.assertIn("é LI.", saida)

    def test_quantidade_invalida_pede_de_novo(self):
        saida = self.rodar("5\n2\n1 2 3\n2 4 6\n")
        self.assertIn("Digite 2 ou 3", saida)
        self.assertIn("é LD.", saida)


if __name__ == "__main__":
    unittest.main()
