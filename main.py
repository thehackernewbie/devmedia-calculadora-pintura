from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()

comodo = Comodo(
    input('Qual é a largura do cômodo? '),
    input('Qual é a profundidade do cômodo? ')
)

print('A área das paredes é: ',
    calc.calcular_area_paredes(
    comodo.largura, comodo.profundidade, comodo.altura)
)

print('A área do teto é: ',
    calc.calcular_area_teto(
    comodo.largura, comodo.profundidade)
)

print('A litragram necessaria é: ',
    calc.calcular_litragem()
)
