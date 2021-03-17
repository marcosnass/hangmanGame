from random import randint
import funcaoEscreva

file = ['casa', 'girafa', 'noite', 'escurecer', 'programar', 'anoitecer', 'amanhecer', 'encontrar', 'viver', 'morrer', 'escutar']
size = len(file)
sort = randint(0, size) - 1
word = file[sort]
jogada = []
escrita = []
sizeWord = len(word)#tamanho da palavra sorteada
funcaoEscreva.escreva('JOGO DA FORCA')
for c in range(0, len(word)):
    escrita.append('_')
print(f'A palavra tem {len(escrita)}, letras. Boa Sorte!')
print('Você podera errar 6 vezes')
print(escrita)
acert = c = erro = 0
while erro != 6:
    letter = str(input('Letra:'))
    if letter in word:
        for i, k in enumerate(word):
            if letter == k:
                escrita[i] = letter
                jogada.append(letter)
        acert += 1
    else:
        erro += 1
        print(f'Não tem a letra "{letter.upper()}" na palavra [{erro}ª erro]')
    if len(jogada) == len(word):
        print(f'PARABÉNS, você venceu em {c+1} tentativas')
        break
    print('A palavra é: ', end='')
    for i in escrita:
        print(i, end=' ')
    print()
    print(f'{c+1}ª tentativa')
    c += 1
if c == 6:
    print('-*'*15)
    print('Você excedeu o número de tentativas, PERDEU!')
    print('-*'*15)
print(f'A palavra era "- {word} -"')
print()
print('FIM DA EXECUÇÃO')
