from codigo.bytebank import Funcionario
import pytest
from pytest import mark
class TestClass:
    def test_idade_recebe_13_03_2000_retornar_26(self):
        #given-contexto
        entrada = '13/03/2000'
        esperado = 26

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        #when-ação
        resultado = funcionario_teste.idade()

        #Then-desfecho
        assert resultado == esperado
    
    def test_quando_sobrenome_rescebe_Lucas_carvalho_deve_retornar_apenas_carvalho(self):
        entrada = 'Lucas Carvalho' #given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() #when

        assert resultado == esperado #then

    def test_decrecimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome,'11/11/2000', entrada_salario)
        
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste','11/11/2000', entrada_salario)
               
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_10000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 10000000
            

            funcionario_teste = Funcionario('Teste','11/11/2000', entrada_salario)
                
            resultado = funcionario_teste.calcular_bonus()

            assert resultado
    
    