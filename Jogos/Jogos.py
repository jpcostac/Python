import Forca
import Adivinhacao

print("******************")
print("Escolha o seu jogo")
print("******************")

print("(1)Forca ou (2)Adivinhação:")

jogo= int(input("Qual o jogo"))

if (jogo == 1):
    print("Jogando Forca")
    Forca.jogar()

elif (jogo == 2):
    print("Jogando Adivinhação")
    Adivinhacao.jogar()