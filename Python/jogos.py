import adivinhacao
import forca

def jogos():

    print('*'*32)
    print('      Escolha o seu jogo!')
    print('*'*32)

    print('(1) Adivinhação\n(2) Forca')
    jogo = int(input('Qual jogo você quer jogar? '))

    if jogo == 1:
        print('Jogando Adivinhacao...')
        adivinhacao.jogar_adivinhacao()
    if jogo == 2:
        print(('Jogando Forca...'))
        forca.jogar_forca()

if __name__ == "__main__":
    jogos()