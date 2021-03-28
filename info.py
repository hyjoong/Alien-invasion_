import pygame.font


class Info_Screen():
    def __init__(self, screen):
        #Hyun_ 화면의 크기, 위치, 색상, 폰트, 폰트 색상 등 설정
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 600, 600
        self.rect_color = (0, 255, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 30)
        self.title_font = pygame.font.SysFont(None, 100)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #Hyun_ 출력할 텍스트, 이미지 설정 및 렌더 메소드 실행
        self.title = 'Alien Invasion'
        self.msgs_page_1 = ['Defeat the Aliens and earn points by shooting them',
                   'Use" <-  -> " arrow keys to move horizontally',
                   'Press SPACEBAR to shoot aliens',
                    ' --------Alien Speed-------- ',
                    'EASY: 0.5, NORMAL = 1.0, HARD = 1.5'
        ]
        self.msgs_page_1_rect_y = [-50, 0, 50, 100, 150]
        self.aliens = [pygame.image.load('assets/redalien.png'),
                        pygame.image.load('assets/blue.png'),
                        pygame.image.load('assets/black.png')]
        self.msgs_page_2 = ['_______________Bonuses_______________',
                            'Alien Speed Up',
                            'Alien Speed Down',
                            'Ship Shooting Speed Up']
        self.msgs_page_2_rect_y = [-100, 20, 80, 140]

        self.prep_msgs(self.msgs_page_1, self.msgs_page_2)

        #Hyun_ 화면 출력중인지 저장
        self.status = False
        #Hyun_ 현재 페이지 저장
        self.currentPage = 1

    # Hyun_ 텍스트 렌더 및 배치 메소드
    def prep_msgs(self, msgs_page_1, msgs_page_2):
        #Hyun_ 타이틀
        self.title_image = self.title_font.render(self.title, True, self.text_color, self.rect_color)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.centerx = self.rect.centerx
        self.title_image_rect.top = self.rect.top + 20

        #Hyun_ 1페이지에서 쓰일 텍스트
        msg_page_1_images = [self.font.render(msg, True, self.text_color, self.rect_color) for msg in msgs_page_1]
        msg_page_1_image_rects = [img.get_rect() for img in msg_page_1_images]
        for rect, y in zip(msg_page_1_image_rects, self.msgs_page_1_rect_y):
            rect.centerx = self.rect.centerx
            rect.centery = self.rect.centery + y

        #Hyun_ 2페이지에서 쓰일 이미지 및 텍스트
        alien_image_rects = [img.get_rect() for img in self.aliens]
        msg_page_2_images = [self.font.render(msg, True, self.text_color, self.rect_color) for msg in msgs_page_2]
        msg_page_2_image_rects = [img.get_rect() for img in msg_page_2_images]
        for rect, y in zip(msg_page_2_image_rects, self.msgs_page_2_rect_y):
            if y < 0:
                rect.centerx = self.rect.centerx
            else:
                rect.left = self.rect.right - 300
            rect.centery = self.rect.centery + y
        for rect, y in zip(alien_image_rects, self.msgs_page_2_rect_y[1:]):
            rect.right = self.rect.left + 200
            rect.centery = self.rect.centery + y

        #Hyun_ self.page에 각 페이지별 출력할 텍스트들, 이미지들을 딕셔너리로 저장
        self.page = {1: [[msg_page_1_images, msg_page_1_image_rects]],
                    2: [[msg_page_2_images, msg_page_2_image_rects], [self.aliens, alien_image_rects]]}

    #Hyun_ 출력 메소드
    def draw_screen(self):
        self.screen.fill(self.rect_color, self.rect)
        self.screen.blit(self.title_image, self.title_image_rect)

        #Hyun_ 현재 페이지에 맞는 텍스트, 이미지를 출력함
        for items in self.page[self.currentPage]:
            for img, rect in zip(items[0], items[1]):
                self.screen.blit(img, rect)