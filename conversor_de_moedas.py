print('BEM VINDO AO CONVERSOR DE MOEDAS DO PEDRO')
print('*****************************************', '\n')

dolar = 5.46
euro = 6.19
remimbi = 0.86
libra = 7.40

valor_entrada = float(input('Qual o valor em R$? '))

print("Qual o tipo de moeda que você vai converter?")
print(' (1) Dólar', '\n', '(2) Euro', '\n', '(3) Remimbi', '\n', '(4) Libra')

tipo_moeda = int(input('Escolha: '))

if(tipo_moeda == 1):
    conversao_dolar = round(valor_entrada / dolar, 2)
    print('R$ {} está valendo hoje U$$ {}'.format(valor_entrada, conversao_dolar))
if(tipo_moeda == 2):
    conversao_euro = round(valor_entrada / euro, 2)
    print('R${} está valendo hoje €{}'.format(valor_entrada, conversao_euro))
if(tipo_moeda == 3):
    conversao_remi = round(valor_entrada / remimbi, 2)
    print('R${} está valendo hoje RI${}'.format(valor_entrada, conversao_remi))
if(tipo_moeda == 4):
    conversao_libra = round(valor_entrada / libra, 2)
    print('R${} está valendo hoje L${}'.format(valor_entrada, conversao_libra))
elif(tipo_moeda != 1,2,3,4):
    print('INFORME UM NÚMERO VÁLIDO')
