import pygame

from pygame.sprite import Sprite


class Ship(Sprite):

    #sprite의 class를 생성했다
    def __init__(self, game):
        #부모의 초기값들을 가져오기위해 super()사용
        super().__init__()

        #초기 화면 세팅
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # 이미지를 불러온다.
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()

        #크기 변수를 초기화
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # 이동여부를 확인하는 flags
        self.moving_right = False
        self.moving_left = False

    #배의 업데이트
    def update(self):
        """Update the ship's position based on movement flags."""
        # 버튼에 따른 위치를 업데이트 한다.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update rect object from self.x.
        self.rect.x = self.x

    def draw(self):
        #업데이트된 객체를 그려준다
        self.screen.blit(self.image, self.rect)

    #위치를 좌표화 하여 업데이트를 진행
    def align_center(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
