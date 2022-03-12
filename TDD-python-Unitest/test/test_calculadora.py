try:
    import sys
    import os 

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise






from calculadora import soma, subtrai
import unittest


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_20_e_20_deve_retornar_40(self):
        self.assertEqual(soma(20, 20 ), 40)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)




    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (-5, 5, 0),
            (100, 100, 200),
        )
        
        for x_y_saidas in x_y_saidas:
            x, y, saida = x_y_saidas
            self.assertEqual(soma(x, y), saida)


    def test_soma_x_e_nao_e_int_ou_float_deve_retornar_assertionerro(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)
    
    
    def test_soma_y_e_nao_e_int_ou_float_deve_retornar_assertionerro(self):
        with self.assertRaises(AssertionError):
            soma(11, '0')


## sisitema de subtração da calculadora ....


    def test_subtrai_10_e_5_deve_retornar_5(self):
        self.assertEqual(subtrai(10, 5 ), 5)


    def test_subtrai_20_e_15_deve_retornar_5(self):
        self.assertEqual(subtrai(20, 15), 5)



    def test_subtrai_varias_entradas(self):
        x_y_saidas = (
            (10, 5, 5),
            (20, 5, 15),
            (100, 50, 50),
            (500, 250, 250),
        )

        for x_y_saidas in x_y_saidas:
            x, y, saida = x_y_saidas 
            self.assertEqual(subtrai(x, y), saida)

    def test_subtrai_x_e_nao_e_int_ou_float_deve_retornar_assertionerro(self):
        with self.assertRaises(AssertionError):
            subtrai('11', 4)
    
    def test_subtrai_y_e_nao_e_int_ou_float_deve_retornar_assertionerro(self):
        with self.assertRaises(AssertionError):
            subtrai(10, '11')
    



unittest.main(verbosity=2)
