"""
TDD - test driven development (Desevolvimentos dirigidos em tests)


Red -----
parte 1 -> Cria um test e vê falhar ! 

Win -----
parte 2 -> Cria o codico e vê o test passar! 

Refractory --=---
parte 3 -> Melhora o meu codico....
"""




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

from cadastro import logins_user_cadastrados
import unittest



class TestCadastro(unittest.TestCase):
    def test_cadastro_login_deve_receber_assertion_erro_se_nao_recebe_int(self):
        with self.assertRaises(AssertionError):
            logins_user_cadastrados('4')
            


    def test_cadastro_login_deve_retornar_aprovados_se_entrada_for_multiplo_de_5_e_3(self):
        entradas = (15, 30, 45, 60)
        saida =  'Aprovados'
            
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(logins_user_cadastrados
                (entrada), 
                saida,
                msg=f"{entrada} nao retornou á {saida}")

    def test_cadastro_login_deve_retornar_reprovados_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7)
        saida =  'Reprovados'
            
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(logins_user_cadastrados
                (entrada), 
                saida,
                msg=f"{entrada} nao retornou á {saida}")



    def test_cadastro_login_deve_retornar_aceito_se_entrada_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21)
        saida =  'Aceitos'
            
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(logins_user_cadastrados
                (entrada), 
                saida,
                msg=f"{entrada} nao retornou á {saida}")



    def test_cadastro_login_deve_retornar_aceito_se_entrada_for_multiplo_de_5(self):
        entradas = (5, 10, 20, 25, 35)
        saida =  'Cadastrados'
            
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(logins_user_cadastrados
                (entrada), 
                saida,
                msg=f"{entrada} nao retornou á {saida}")








unittest.main(verbosity=2)
