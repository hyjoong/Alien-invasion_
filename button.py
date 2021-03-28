import pygame.font


class Button:

    def __init__(self, ai_game, msg, width=200, height=50, x=None, y=None, color=(0, 255, 0)):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 버튼의 너비와 색상, 텍스트색상, 폰트등을 셋업
        self.width, self.height = width, height
        self.button_color = color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 위치 설정
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        #hyun_ 버튼의 위치는 지정해주었을 때엔 해당 위치, 지정하지 않았을 때엔 중앙으로 배치
        self.rect.centerx = self.screen_rect.centerx if x is None else x
        self.rect.centery = self.screen_rect.centery if y is None else y

        # 메세지 출력함수를 실행
        #hyun_ 버튼 색상 변경을 위해 매개변수 msg 저장
        self.msg = msg
        self._prep_msg(self.msg)

    #파라미터로 들어온 msg를 랜더 함수 , 렌더해준다
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    #hyun_ 난이도 버튼 선택 시 버튼 색상을 변경하기 위한 메소드
    def change_color(self, color=(0, 255, 0)):
        self.button_color = color
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)

    #렌더한 이미지를 그려준다
    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)