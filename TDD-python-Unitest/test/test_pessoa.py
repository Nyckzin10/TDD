"""
class Pessoa 
    __init__
        nome str 
        sobrenome str 
        dados_obetidos boll -> iniciar os dados como "False" 

    API:
        obter_todos_dados -> method !----- dados obtidos da api da 'url'
            OK
            404

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

import unittest
from pessoa import Pessoa
from unittest.mock import patch



class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Hedris' , 'Rocha')

    def test_pessoa_attr_nome_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Hedris')

    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)


    def test_pessoa_attr_sobrenome_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Rocha')

    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)


    def test_pessoa_attr_dados_obetidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obetidos)



    def test_obeter_todos_os_dados_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True 
            
            self.assertEqual(self.p1.obter_todos_os_dados(), "CONECTADO")


    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False 
            
            self.assertEqual(self.p1.obter_todos_os_dados(), "ERRO 404")




if __name__ == '__main__':
    unittest.main(verbosity=2)
