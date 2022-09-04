import random

def jogar_adivinhacao():

    print('*'*32)
    print('Bem vindo ao Jogo da Adivinhação')
    print('*'*32)

    numero_secreto = round(random.randrange(1, 101))
    tentativas = 0
    pontos = 1000
    pontos_perdidos = 0

    print('Nível de dificuldade:')
    print('(1) Fácil')
    print('(2) Médio\n(3) Difícil')
    dificuldade = int(input('Escolha a dificuldade: '))

    while dificuldade != 1 and dificuldade != 2 and dificuldade != 3:
        dificuldade = (int(input('Valor inválido! Escolha a dificuldade:')))
    else:
        if dificuldade == 1:
            tentativas = 20
        elif dificuldade == 2:
            tentativas = 10
        elif dificuldade == 3:
            tentativas = 5

    for rodada in range(1, tentativas + 1):
        print(f'Tentativa {rodada} de {tentativas}')
        chute = int(input('Digite um número entre 1 e 100: '))
        pontos_perdidos = chute - numero_secreto
        pontos = pontos - abs(pontos_perdidos)
        print(pontos)
        print('Voce digitou', chute)

        if (chute < 1) or (chute > 100):
            print('Voce deve digitar um numero entre 1 e 100')
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('Parabéns voce acertou o numero secreto!')
            break
        elif maior:
            print('Chute errado! Voce chutou muito alto')
        elif menor:
            print('Chute errado! Voce chutou muito baixo')

    print('Fim do jogo')
    print(f'A resposta era {numero_secreto}')
    print(f'A sua pontuação foi de: {pontos}')

if __name__ == "__main__":
    jogar_adivinhacao()