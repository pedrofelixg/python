import webbrowser
import html

print('**************************************************')
print('*********BEM VINDOS À CALCULADORA DE IMC**********')
print('**************************************************')

nome = input('Qual o seu nome? ')
altura = float(input('Informe sua altura: '))
peso = int(input('Informe seu peso: '))
print('\n')

imc = peso / (altura * altura)
imc_round = round(imc, 2)

# site = webbrowser.open('https://bvsms.saude.gov.br/bvs/dicas/215_obesidade.html')
# Preciso dar um jeito de fazer esse link ser "ciclável". O programa tá dando True ao final, e já abrindo.

print('Olá {} o seu IMC é'.format(nome), imc_round, '\n')
if(imc_round <= 18):
    print('Seu IMC está abaixo Ideal Recomendado')
elif(imc_round > 18 and imc_round <= 24):
    print('Seu IMC está no Ideal Recomendado')
else:
    print('Você está acima do Ideal Recomendado')

print('Obrigado pela preferência')