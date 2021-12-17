#UTF- 8
# My first game - Hangman - Matheus Marcondes.
# Meu primeiro game - Jogo da Forca
# Programação Orientada a Objetos- Data Science Academy

# Importaremos o módulo random para que durante o jogo sejam selecionadas as palavras de maneira aleatória.
import random
#Agora "desenharemos" o tabuleiro.
tabuleiro = ['''
>>> Jogo da Forca <<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Definiremos a classe do jogo.
class jogoDaFoca:
    #Agora definiremos os métodos, sendo o primeiro o médoto construtor.
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []  #Lista de letras incorretas.
        self.letras_ok = []

    #Método para advinharmos as letras.
    def adv(self, letra):
        if letra in self.palavra and letra not in self.letras_ok:
            self.letras_ok.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    # Agora precisamos definir um método para verificarmos se o jogo terminou.
    def fim(self):  # Não será acrescentado nem um atributo ao método.
        return self.vitoria() or (len(self.letras_erradas) == 6)
        # Utilizaremos a função len como forma de medição das letras erradas.

    #Definiremos o método para verificarmos se o jogador venceu.
    def vitoria(self):
        if '*' not in self.ocultar_letra():
            return True
        return False



        # Método para ocultar a palavra no quadro(board)
    def ocultar_letra(self):
        oculte = ''
        for letra in self.palavra:  # Para cada letra em "palavra
            if letra not in self.letras_ok:  # Se 'letra' não em 'advinha letra'.
                oculte += '*'
            else:
                oculte += letra
        return oculte

    #Agora precisamos definir um método para checarmos o 'status'e imprimirmos o tabuleiro na tela.
    def mostrar_tabuleiro(self):
        print(tabuleiro[len(self.letras_erradas)]) #Utilizaremos novamento a função len como forma de medição do status do tabuleiro.
        print('Palavra: ' + self.ocultar_letra()) #Aqui faremos com que a palavra retorne de forma que suas letras estejam ocultas.
        #Iremos definir um loop for para que possamos saber quais as letras que erramos.
        #Lembrando que só teremos 6 chances sendo, cabeça = 1, braços = 2, tronco = 1, pernas = 2
        print('Letras incorretas: ')
        for letra in self.letras_erradas:
            print(letra,)
        print()

#Agora precisamos definir um método para que retornarmos uma palavra de forma aleatória do banco de palavras(word.txt)
def palavra_aleatoria():
    with open("palavras.txt", "rt") as w:
        banco_de_palavras = w.readlines() #leremos o arquivo linha por linha.
    return banco_de_palavras[random.randint(0,len(banco_de_palavras))].strip() #Utilizaremos o strip para excluir os espaços em branco antes e depois da palavra.

#Agora precisamos definir o método de execução do programa.
def exe():
    #Definiremos o objeto de execução.
    game = jogoDaFoca(palavra_aleatoria())

    #loop while para retorno do status e solicitar uma letra.
    while not game.fim():
        game.mostrar_tabuleiro()
        add_letra = input('\nDigite uma letra: ')
        game.adv(add_letra)

    #Verificando o status do jogo.
    game.mostrar_tabuleiro()

    #Irá retornar a mensagem de acordo com o status do jogo.
    if game.vitoria():
        vitoria = int(input('Parabéns, você ganhou! \nDeseja jogar novamente? \nTecle 1 para SIM - 2 para Não.'))
        if vitoria == 1:
            exe()
        else:
            print('Muito obrigado por ter jogado comigo!')
            print('Matheus Marcondes, 1º semestre - Data Science - UNESA')
            print('Data Science Academy')

    else:
        print('Esta é a palavra correta: ' + game.palavra)
        derrota = int(input('Infelizente você errou, \nDeseja jogar novamente? \nTecle 1 para SIM - Tecle 2 para Não.'))
        if derrota == 1:
            exe()
        else:
            print('Muito obrigado por ter jogado comigo!')
            print('Matheus Marcondes, 1º semestre - Data Science - UNESA')
            print('Data Science Academy')

#Função para executarmos o programa.
if __name__ == "__main__":
    exe()