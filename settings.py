class Settings:

    def __init__(self):
        #초기 스크린 크기와 배경색을 세팅한다
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #목숨의 갯수
        self.ship_limit = 3

        #총알의 크기와 색을 결정
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        #최대 총알갯수
        self.bullets_allowed = 100
        #hyun_ 총알 발사 속도
        self.fire_speed = 0.2
        #hyun_ 버프 지속 시간(초)
        self.buff_duration = 5

        # 에일리언 떨어지는 속도를 설정
        self.fleet_drop_speed = 10

        # 속도 업데이트 스케일 설정
        self.speedup_scale = 1.1
        # 속도가 빨라짐에 따라 점수의 변화 스케일 설정
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    #초기 역학적 움직임 값 설정
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        #배 속도
        self.ship_speed = 1.5
        #총알 속도
        self.bullet_speed = 3.0
        #에일리언 속도
        self.alien_speed = 1.0

        #에일리언 방향설정 +1 -> 오른쪽 , -1 -> 왼쪽
        self.fleet_direction = 1

        # 초기 스코어
        self.alien_points = 50 

    #스크린 업데이트를 진행할때 , 속도를 증가시키는 값들 변화
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale 

        self.alien_points = int(self.alien_points * self.score_scale)


    #kwon_ 원래 속도는 1.0, 빨강색을 격추하면 0.1 증가, 파랑색을 격추하면 0.1 감소
    def increase_speed_alien(self,color) :
        # 초록색일 경우 아무것도 안함
        if color == 1 :
            return 0           
        elif color == 2 :    
            self.alien_speed += 0.1 
            print("속도 증가")
        elif color == 3 :
            self.alien_speed -= 0.1 
            print("속도 감소")
        # 검정색일 경우도 아무것도 안함    
        elif color == 10 :
            return 0  
