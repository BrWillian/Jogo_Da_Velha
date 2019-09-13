import numpy as np
from os import system

co = "\033[31m"
cx = "\033[1m"

class JogoDaVelha:
    def __init__(self):
        self.__player_1 = None
        self.__player_2 = None
        self.array = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], dtype=np.str)

    def jogar(self):
        self.__player_1 = input('Digite nome do jogador 1: ')
        self.__player_2 = input('Digite nome do jogador 2: ')
        system('clear')
        self.printa()
        p = 9
        while(p):
            if p % 2 != 0:
                x, y = input('Digite a posicao: ').split(' ')
                x = int(x)
                y = int(y)
                self.player_1(x,y)
            else:
                x, y = input('Digite a posicao: ').split(' ')
                x = int(x)
                y = int(y)
                self.player_2(x, y)
            p -= 1
            self.printa()


    def printa(self):

        print("\n" * 40 + f'''
                                   |     |      
                                {self.array[0,0]}  |  {self.array[0,1]}  |  {self.array[0,2]}  
                              _____|_____|_____
                                   |     |      
                                {self.array[1,0]}  |  {self.array[1,1]}  |  {self.array[1,2]}  
                              _____|_____|_____
                                   |     |      
                                {self.array[2,0]}  |  {self.array[2,1]}  |  {self.array[2,2]}  
                                   |     |    

        
        ''')
        print('\n' * 3)

    def player_1(self, x, y):
        self.x, self.y = x,y
        self.array[self.x, self.y] = 'X'

    def player_2(self, x, y):
        self.x, self.y = x,y
        self.array[self.x, self.y] = 'O'
