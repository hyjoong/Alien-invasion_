import pygame
import random
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        #kwon_ 여러색의 에일리언 추가
        a = pygame.image.load('assets/alien.bmp')
        b = pygame.image.load('assets/redalien.png')
        c = pygame.image.load('assets/blue.png')
        d = pygame.image.load('assets/black.png')

        #kwon_ 랜덤을 사용하여 특수 색의 에일리언을  생성
        self.y = random.randint(0,99)
        
        if  self.y  < 80 :
            self.image = a

        #kwon_ 각각 10%,10%,1%의 확률로
        if  80 <= self.y and self.y < 90 :   
            self.image = b
        if  90 <= self.y and self.y < 99   :
            self.image = c
        if  99 == self.y  :
            self.image = d
        self.rect = self.image.get_rect()    
        

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x


    #kwon_ 격추당한 에일리언의 색상
    def pointk(self):
        if  self.y  < 80 :
            print("격추당한 색깔은 초록")
            return 1
            
        if  80 <= self.y and self.y < 90 :   
            print("격추당한 색깔은 빨강")
            return 2
              
        if  90<= self.y and self.y < 99   :
            print("격추당한 색깔은 파랑")
            return 3
                
        if  99 == self.y  :
            print("격추당한 색깔은 검정")
            return 10
