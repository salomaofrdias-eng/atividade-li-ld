import unittest
from fractions import Fraction as F

from li_ld import determinante, julgar_dois_vetores, julgar_tres_vetores, produto_vetorial
from li_ld.entrada import parse_vetor


def vet(*xs):
    return [F(x) for x in xs]


class TestDoisVetores(unittest.TestCase):
    def test_multiplos_sao_ld(self):
        self.assertEqual(julgar_dois_vetores(vet(1, 2, 3), vet(2, 4, 6))[0], "LD")

    def test_nao_multiplos_sao_li(self):
        resultado, w = julgar_dois_vetores(vet(1, 0, 2), vet(0, 1, 1))
        self.assertEqual(resultado, "LI")
        self.assertEqual(w, vet(-2, -1, 1))

    def test_vetor_nulo_e_ld(self):
        self.assertEqual(julgar_dois_vetores(vet(0, 0, 0), vet(1, 2, 3))[0], "LD")
        self.assertEqual(julgar_dois_vetores(vet(0, 0, 0), vet(0, 0, 0))[0], "LD")

    def test_multiplo_negativo_e_fracionario(self):
        self.assertEqual(julgar_dois_vetores(vet(1, 2, 3), vet(-1, -2, -3))[0], "LD")
        self.assertEqual(julgar_dois_vetores(vet(2, 4, 6), vet("1/3", "2/3", 1))[0], "LD")

    def test_decimais_sao_exatos(self):
        # 0,1 + 0,2 != 0,3 em float; com Fraction o resultado é exato
        u = parse_vetor("0,1 0,2 0,3")
        v = parse_vetor("1 2 3")
        self.assertEqual(julgar_dois_vetores(u, v)[0], "LD")

    def test_vetores_canonicos_sao_li(self):
        self.assertEqual(julgar_dois_vetores(vet(1, 0, 0), vet(0, 1, 0))[0], "LI")

    def test_produto_vetorial_anticomutativo(self):
        u, v = vet(1, 2, 3), vet(4, 5, 6)
        self.assertEqual(produto_vetorial(u, v), [-x for x in produto_vetorial(v, u)])


class TestTresVetores(unittest.TestCase):
    def test_base_canonica_e_li(self):
        resultado, det = julgar_tres_vetores(vet(1, 0, 0), vet(0, 1, 0), vet(0, 0, 1))
        self.assertEqual((resultado, det), ("LI", 1))

    def test_coplanares_sao_ld(self):
        resultado, det = julgar_tres_vetores(vet(1, 2, 3), vet(4, 5, 6), vet(7, 8, 9))
        self.assertEqual((resultado, det), ("LD", 0))

    def test_exemplo_li(self):
        resultado, det = julgar_tres_vetores(vet(1, 2, 3), vet(4, 5, 6), vet(7, 8, 10))
        self.assertEqual((resultado, det), ("LI", -3))

    def test_vetor_nulo_no_conjunto_e_ld(self):
        self.assertEqual(julgar_tres_vetores(vet(0, 0, 0), vet(1, 2, 3), vet(4, 5, 7))[0], "LD")

    def test_vetores_repetidos_sao_ld(self):
        self.assertEqual(julgar_tres_vetores(vet(1, 2, 3), vet(1, 2, 3), vet(0, 1, 0))[0], "LD")

    def test_determinante_troca_de_linhas_inverte_sinal(self):
        u, v, w = vet(1, 2, 3), vet(4, 5, 6), vet(7, 8, 10)
        self.assertEqual(determinante(u, v, w), -determinante(v, u, w))


class TestEntrada(unittest.TestCase):
    def test_inteiros_decimais_e_fracoes(self):
        self.assertEqual(parse_vetor("1 0,5 2/3"), [F(1), F(1, 2), F(2, 3)])
        self.assertEqual(parse_vetor("1.5 -2 0"), [F(3, 2), F(-2), F(0)])

    def test_quantidade_errada_de_coordenadas(self):
        for texto in ("", "1 2", "1 2 3 4"):
            with self.assertRaises(ValueError):
                parse_vetor(texto)

    def test_valores_invalidos(self):
        for texto in ("a b c", "1 2 x", "1 2 1/0", "nan 1 2", "inf 1 2"):
            with self.assertRaises(ValueError):
                parse_vetor(texto)


if __name__ == "__main__":
    unittest.main()
