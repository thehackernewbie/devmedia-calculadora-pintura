from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()

comodo = Comodo(
    input('Qual é a largura do cômodo? '),
    input('Qual é a profundidade do cômodo? ')
)

print('A área das paredes é: ',
    calc.calcular_area_paredes(comodo))

print('A área do teto é: ',
    calc.calcular_area_teto(comodo))

print('A litragram necessaria é: ',
    calc.calcular_litragem()
)
