import random

def jogar():
    print("*******************")
    print("Jogo da adivinhação")
    print("*******************")

    numero_secreto= random.randrange(1,101)
    total_de_tentativas= 0
    print(numero_secreto)
    pontos=1000

    print("Escolha o nível do jogo:")
    nivel= int(input(("(1)Fácil, (2)Médio e (3)Difícil:\n")))

    if(nivel == 1):
        total_de_tentativas=20
    elif(nivel== 2):
        total_de_tentativas= 10
    else:
        total_de_tentativas= 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentaiva {} de {}". format(rodada, total_de_tentativas))
        chute_str= input("Adivinhe o número secreto entre 1 e 100:\n")
        chute= int(chute_str)
        print("Você digitou:",chute)

        if (chute <1 or chute >100):
            print("Digite um valor entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Parabéns você acertou e fez {} pontos". format(pontos))
            break

        else:
            if(maior):
                print("Digite um valor menor")
                if (rodada == total_de_tentativas):
                    print("Você perdeu, o número secreto era {} e você fez {} pontos". format(numero_secreto, pontos))

            elif(menor):
                print("Digite um valor maior")
                if (rodada == total_de_tentativas):
                    print("Você perdeu, o número secreto era {} e você fez {} pontos". format(numero_secreto, pontos))

            pontos_perdidos= abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo!")      

if(__name__=="__main__"):
    jogar()          