import forca
import advinhacao

def escolhe_jogo():
    print("************************************************")
    print("****************ESCOLHA SEU JOGO****************")
    print("************************************************")

    print("(1) FORCA   (2) ADVINHAÇÃO")
    jogo = int(input("Qual Jogo?"))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Advinhação")
        advinhacao.jogar()
if(__name__ == "__main__"):
    escolhe_jogo()