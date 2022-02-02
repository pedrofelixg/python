import random
def jogar():

    print("************************************************")
    print( "Olá bem vindo ao jogo de advinhação do Pedro!")
    print("************************************************")

    numero_secreto = random.randrange(1,51)
    total_de_tentativas = 0
    rodada = 1
    pontos = 100


    print("Qual o nível de Dificuldade?")
    print("(1) Fácil \n" "(2) Médio \n" "(3) Díficil \n")
    nivel = int(input(" Defina o Nível: "))

    if(nivel == 1):
        total_de_tentativas = 15
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite o seu número: ")
        numero = int(chute)
        print("Você digitou " , chute)

        if(numero < 1 or numero > 50):
            print("Você deve digitar um número entre 1 e 50")
            continue

        acerto = numero_secreto == numero
        maior = numero > numero_secreto
        menor = numero < numero_secreto

        if(acerto):
            print("Você Acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu número foi maior que o número secreto.")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            if(menor):
                print("Você errou! O seu número foi menor que o número secreto.")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - numero)
            pontos = pontos - pontos_perdidos
            print("Você Errou" '\n')
    print("FIM DE JOGO")
if(__name__ == "__main__"):
    jogar()