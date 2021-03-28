import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        #초기 화면설정
        self.ai_game = ai_game
        self.screen = ai_game.screen
        #화면의 크기를 변수화 한다
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #폰트의 셋업 값을 설정
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 스코어 보드에 값들을 업로드
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    #스코어를 이미지화 해주는 함수
    def prep_score(self):
        """Turn the score into a rendered image."""
        #일의 자리에서 반올림하는 숫자로 계산
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        #pygame의 font내부의 렌더모듈을 이용하여 렌더한다.
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        #위치를잡는다.
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    #최고점을 이미지화 해주는 함수
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    #레벨을 이미지화 해주는 함수
    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                                            self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    #배의 목숨을 이미지화 해주는 함수
    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    #현재 최고점을 확인하는 함수
    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    #스코어를 업데이트하는함수
    def show_score(self):
        """Draw scores, level, and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
