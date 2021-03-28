import sys
from time import sleep, time

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from utils import hide_mouse_cursor
from info import Info_Screen
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')
        self.stats = GameStats(self)
        self.score_board = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        #kwon_ 난이도 변수
        self.difficulty = 1
        self.create_fleet_of_aliens()
        play_button = Button(self, 'Play', y=335)
        easy_button = Button(self, 'EASY', width=160, x=430)
        normal_button = Button(self, 'NORMAL', width=160, color=(255, 0, 0))
        hard_button = Button(self, 'HARD', width=160, x=770)
        info_button = Button(self, 'Info', y=465)
        next_button = Button(self, '->', width=50, x=650, y=650)
        back_button = Button(self, '<-', width=50, x=550, y=650)
        self.return_to_main_button = Button(self, 'Main')
        #Hyun_ 버튼을 리스트에 저장
        self.buttons = [play_button, easy_button, normal_button, hard_button, info_button, next_button, back_button]
        #Hyun_ Info 화면 추가
        self.info = Info_Screen(self.screen)
        self.alien = Alien(self)
        pygame.mixer.music.load("music/game_music.ogg")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        #총알 발사상태 초기값 false로 설정 
        self.fire = False
        #Hyun_ 발사 속도 설정
        self.fire_speed = self.settings.fire_speed
        #Hyun_ 검은색을 맞췄을 때 발사 속도 증가 버프를 위해 bool형 변수 생성
        self.fire_speed_buffed = False
        #Hyun_ 버프 지속시간 확인을 위한 버프 시작 시간를 저장할 변수 생성
        self.buff_start_time = 0
        self.last_fire_time = time()
        

    def run_game(self):
        while True:
            #게임실행시 클래스 내부함수인 respond_to_event()를 반복문 속에서 실행하여
            #특정 이벤트가 발생했는지 모니터링한다
            self.respond_to_events()
            #이벤트 발생시 stats의 game_active함수를 통해 확인하고
            #각 객체들의 업데이트를 진행한다. ship aliens ,bullet, fire_bullet
            if self.stats.game_active:
                self.ship.update()
                self.update_bullet_positions()
                self._update_aliens()
                # fire_bullet 객체 추가
                self.fire_bullet()
            #class 내장함수인 _update_screen를 동작하여
            #화면의 목숨, score를 업데이트 한다
            self._update_screen()

    # 일시정지 기능 함수 정의
    def pause(self):
        x = True
        self.return_to_main_button.draw_button()
        pygame.display.flip()
        pygame.mouse.set_visible(True)
        while x>0:
            for event in pygame.event.get():
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        x = False
                        pygame.mouse.set_visible(False)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = self.return_to_main_button.rect.collidepoint(pygame.mouse.get_pos())
                    if clicked:
                        self.stats.game_active = False
                        x = False
                if event.type == pygame.QUIT:
                    sys.exit()
        pygame.display.flip()          
        clock = pygame.time.Clock()
        pygame.display.update()
        clock.tick(10)
        
    #실행중인 py-game 내부에서 발생하는 이벤트를 감지하는 함수
    def respond_to_events(self):
        #event.get 을 이용하여 발생한 이벤트 들을 확인한다
        for event in pygame.event.get():
            #종료 이벤트 일 경우 종료
            if event.type == pygame.QUIT:
                sys.exit()
            #키 버튼일 경우 class 내장함수인 check_keydown_events에
            #해당 이벤트를 파라미터로 전달
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
            #마우스 버튼일경우
            #pygame의 마우스 인식을 위한 mouse.get_pos()를 이용하여
            #내장함수인 start_game_if_player_clicks_play에 해당 파라미터를 전달
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.button_check(mouse_pos)
                # self.start_game_if_player_clicks_play(mouse_pos)


    #게임 시작을 위한 함수
    def start_game_if_player_clicks_play(self):
        #게임시작을 위한 조건 확인, 게임 활성화 x
        if not self.stats.game_active:
            #시작을 하게된다면 reset을 진행한다
            #클래스 내장 함수인 reset_game_statistics 와 remove_aliens_and_bullets 와 create_new_fleet
            #를 동작시킨다
            #마지막으로 파이썬 내장함수인 utils의 hide_mouse_cursor를 이용하여 화면상의 마우스를 가린다
            self.reset_game_statistics()
            self.reset_game_statistics()
            self.remove_aliens_and_bullets()
            self.create_new_fleet()
            hide_mouse_cursor()

    #게임초기화를 위해 settings의 initialize_dynamic_settings 함수를 사용 , 속도와 point 초기화 진행
    #class 내장함수인 reset_game_statistics를 사용하여 목숨, score, ship 위치등을 초기화
    def reset_game_settings(self):
        self.settings.initialize_dynamic_settings()
        self.reset_game_statistics()


    #에일리언과 총알을 비우는 함수
    def remove_aliens_and_bullets(self):
        self.aliens.empty()
        self.bullets.empty()


    #새로운 에일리언을 만들고
    #배의 위치를 가운대로 놓는 함수
    #초기 시작이나, 업데이트를 진행하때 사용
    def create_new_fleet(self):
        self.create_fleet_of_aliens()
        self.ship.align_center()

    #화면상의 통계값(스코어, 레벨, 목숨)을 초기화한다.
    def reset_game_statistics(self):
        self.stats.reset_stats()
        self.stats.game_active = True
        self.score_board.prep_score()
        self.score_board.prep_level()
        self.score_board.prep_ships()

    #pygame.event를 파라미터로 가지고
    #키보드를 누르고 땔때 ( KEYDOWN)의 경우 right과 left 움직임에 대해
    #값을 true값으로 바꾸어준다 이는 키를 땔경우 멈추고 키를 누르고 있을 경우
    #계속 움직일수 하기 위해서이다
    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            #self.fire_bullet()
            self.fire = True
            #Hyun_ 게임플레이 중일 떄 esc 키를 눌렀을 때 게임을 일시정지하고
            #Hyun_ info 상태에서 esc 키를 눌렀을때 info 창을 닫는다
        elif event.key == pygame.K_ESCAPE:
            if self.stats.game_active:
                self.pause()
            else:
                self.info.status = False

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        #Hyun_ Space 키를 눌렀다 뗐을 때 발사가 멈추게하는 경우 코드 추가
        elif event.key == pygame.K_SPACE:
            self.fire = False

    #새로운 총알을 만들고
    #이를 미리 선언했던 bullets 그룹에 넣는다
    def fire_bullet(self):
        if self.fire:
            # space 키를 누르고 있을때 0.3초마다 총알이 나가게 설정
            if len(self.bullets) < self.settings.bullets_allowed and time() - self.last_fire_time >= self.fire_speed:
                #Hyun 발사 속도 증가 버프중일 때
                if self.fire_speed_buffed:
                    #Hyun 버프 지속 시간이 다 끝났을 때 버프 끄고, 발사 속도 정상화
                    if time() - self.buff_start_time >= self.settings.buff_duration:
                        self.fire_speed_buffed = False
                        self.fire_speed = self.settings.fire_speed
                self.last_fire_time = time()
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)
                # 총알이 발사될때 효과음 play
                sound = pygame.mixer.Sound('music/bullet.wav')
                sound.play()

    #총알 그룹 객체를 업데이트하는 함수
    #화면에서 벗어난 총알을 제거하는 remove_bullets_that_have_disappeared와
    #에일리언과 충돌하여 사라지는 manage_bullet_alien_collision 과정을 거쳐서 업데이트한다.
    def update_bullet_positions(self):
        self.bullets.update()
        self.remove_bullets_that_have_disappeared()
        self.manage_bullet_alien_collision()

    def remove_bullets_that_have_disappeared(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    #총알과 에일리언이 충돌했을 때 발생하는 이벤트를 다루는 함수
    def manage_bullet_alien_collision(self):
        # Remove any bullets and aliens that have collided.
        #pygame 내부 모듈인 groupcollide로 bullets와 aliens의 충돌을 판단한다
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        
        #충돌이 발생했다면, 스코어 업데이트와
        #스코어 보드 업데이트, 최고점 업데이트 가 동시에 진행된다
        if collisions:
            for aliens in collisions.values():
                #kwon_ aliens[0].pointk() 함수를 사용하여 격추당한 에일리언의 색에 따른 점수 추가
                self.stats.score += self.settings.alien_points * len(aliens) * aliens[0].pointk()
                #kwon_ 격추한 색상에 따라 에일리언의 속도 조절
                self.settings.increase_speed_alien(aliens[0].pointk())
                #kwon_ 격추한 색상이 검정색일 경우 목숨을 추가한다.
                #Hyun_ 격추한 색상이 검정색일 경우 발사 속도 증가 버프를 부여해 버프 지속 시간 만큼 0.1초마다 발사
                if aliens[0].pointk() == 10:
                    # self.stats.ships_left += 1
                    # self.score_board.prep_ships()                    
                    self.fire_speed_buffed = True
                    self.fire_speed = 0.1
                    self.buff_start_time = time()
            self.score_board.prep_score()
            self.score_board.check_high_score()

        #에일리언이 없다면 -> 모든에일리언을 죽였다면
        #레벨이 증가한다
        if not self.aliens:
            self.increase_level()

    #모든 에일리언을 죽였을 경우 실행되는 함수
    def increase_level(self):
        # Destroy existing bullets and create new fleet.
        #기존의 bullets 그룹을 초기화한다.
        self.bullets.empty()
        #새로운 에일리언들을 세팅한다
        self.create_fleet_of_aliens()
        #속도를 증가시킨다
        self.settings.increase_speed()

        # Increase level.
        #레벨을 증가시키고
        #보드판을 업데이트한다
        self.stats.level += 1
        self.score_board.prep_level()



    #에일리언 업데이트 진행
    #에일리언의 fleet_direction 과 bottom position, ship hit을 결정한다
    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
          then update the positions of all aliens in the fleet.
        """
        #edges를 체크한다.
        #양 사이드의 벽을 만나면 방향을 바꿔주는 역할을 한다
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        #배와 에일리언이 충돌한 경우 해당 과정의 업데이트를 진행한다.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        #에일리언이 바닥에 닿을 경우 진행하는 함수
        self._check_aliens_bottom()

    #에일리언라인의 바닥을 확인하는 함수
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        #screen_rect의 크기를 초기에 설정하고 이를 에일리언의 라인과 비교할수 있도록 한다.
        screen_rect = self.screen.get_rect()
        #에일리언그룹의 모든 에일리언들을 반복문을 통해 screen_rect의 값들과 비교한다
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                #바닥에 닿았을 경우 _ship_hit 함수를 실행한다.
                self._ship_hit()
                break


    #배가 에일리언에 부딪혔을경우
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        #목숨을 확인하여 여분 목숨이 있을경우 전체적으로 초기화 진행
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.score_board.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self.create_fleet_of_aliens()
            self.ship.align_center()

            # Pause.
            sleep(0.5)
        #잔여 목숨이 없을경우 종료
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    #에일리언 생성
    def create_fleet_of_aliens(self):
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        #df = self.difficulty 
        alien = Alien(self)
        #에일리언 사이즈를 변수로 설정
        alien_width, alien_height = alien.rect.size
        #화면상에서 에일리언 2마리 분의 두게를 제외한 공간을 확보
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # Determine the number of rows of aliens that fit on the screen.
        #배의 높이와 비교하여 사용가능한 전체 공간에 에일리언을 만든다
        ship_height = self.ship.rect.height
        #kwon_ 난이도별 에일리언 생성
        df = 1
        df = self.difficulty
        if df == 0 :
            df = 5
        elif df == 1 :
            df = 3
        elif df == 2 :
            df = 2    
        available_space_y = (self.settings.screen_height - ( df * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # Create the full fleet of aliens.
        #해당 공간의 dimension이 x,y값으로 결정 됐고 , 해당영역에 모두 에일리언을 배치한다
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.place_alien_in_row(alien_number, row_number)


    #에일리언 생성과정에서 row에 나열하는 과정을 나타낸 함수
    def place_alien_in_row(self, alien_number, row_number):
        alien = Alien(self)
        #에일리언 사이즈 초기 변수설정
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    

    #에일리언 군대의 마지막 사이드의 위치를 체크하는 함수
    #엣지에 도달했다면 _change_fleet_direction를 이용하여 에일리언의 방향을 바꿔준다
    def _check_fleet_edges(self):
          for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    #에일리언군대가 엣지를 만났을 때 방향을 바꾸고 속도를 증가시켜주는함수
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    #스크린 업데이트
    #배경과 배, 에일리언, 총알 스코어보드, 버튼 모두다 최신결과값으로 업데이트한다
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.draw()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.score_board.show_score()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            if self.info.status:
                self.info.draw_screen()
                for button in self.buttons[5:]:
                    button.draw_button()
            else:
                for button in self.buttons[:5]:
                    button.draw_button()

        pygame.display.flip()

    # 버튼 클릭 이벤트를 위한 메소드
    def button_check(self, pos):
        # get_button() 메소드에 인자로 pos를 넘겨주어 클릭된 버튼 가져옴
        button = self.get_button(pos)
        # Info 화면을 보고 있을 경우
        if self.info.status:
            # Info 화면을 클릭했는지 확인
            info_clicked = self.info.rect.collidepoint(pos)
            # Info 화면 밖을 클릭했을 때 Info 화면 끄고 페이지를 1페이지로 변경
            if not info_clicked:
                self.info.status = False
                self.info.currentPage = 1
            # Info 화면 내부를 클릭했을 때
            else:
                # 현재 Info 페이지가 1페이지이고, -> 버튼을 클릭했을 때
                if self.info.currentPage == 1 and button == self.buttons[5]:
                    #Hyun Info 페이지를 2페이지로 변경
                    self.info.currentPage = 2
                # 현재 Info 페이지가 2페이지이고, <- 버튼을 클릭했을 때
                elif self.info.currentPage == 2 and button == self.buttons[6]:
                    # Info 페이지를 1페이지로 변경
                    self.info.currentPage = 1
        # 메인 화면일 경우
        else:
            # Play 버튼
            if button == self.buttons[0]:
                # 게임 시작
                self.start_game_if_player_clicks_play()
            # 난이도 설정 버튼들
            elif button in self.buttons[1:4]:
                df_buttons = self.buttons[1:4]
                # 각 난이도 버튼 별 색상 변경
                for df_button in df_buttons:
                    # 선택한 버튼은 빨간색으로
                    if df_button == button:
                        df_button.change_color(color=(255, 0, 0))
                    # 선택한 버튼 외 버튼들은 녹색으로
                    else:
                        df_button.change_color()
                # 각 난이도 별 기본 속도 설정
                self.difficulty = df_buttons.index(button)
                self.settings.alien_speed = 0.5 * (df_buttons.index(button) + 1)
                
            # Info 버튼
            elif button == self.buttons[4]:
                # Info 화면 띄움
                self.info.status = True

    #Hyun 클릭된 버튼을 반환해주는 메소드
    def get_button(self, pos):
        #Hyun 버튼들을 저장한 self.buttons를 반복문으로 돌려 클릭된 버튼을 반환해줌
        for button in self.buttons:
            clicked = button.rect.collidepoint(pos)
            if clicked:
                return button