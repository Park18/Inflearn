import Character
import pygame

BACKGROUND_IMG = "resource/paper_background_480_640.jpg"
DOG_IMG = "resource/Stand_Dog_70_95.png"
FECES_IMG = "resource/Smile_Feces_70_65.png"
SCORE_SIZE = 10

class Game:

    def __init__(self):

        # pygame 초기화
        pygame.init()

        # 화면 정의
        self.screen_width = 480
        self.screen_height = 640
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        # 타이틀 정의
        pygame.display.set_caption("똥 피하기")

        # FPS를 위한 clock
        self.clock = pygame.time.Clock()

        # 게임 점수
        self.score = 0

    def load_resource(self):

        # 이미지 관련
        self.background = pygame.image.load(BACKGROUND_IMG)
        self.dog = Character.Dog(DOG_IMG, 0.6, self.screen_width, self.screen_height)
        self.feces = Character.Feces(FECES_IMG, 0.01)
        
        # 텍스트 관련
        self.game_font = pygame.font.Font(None, 40)

    def display_update(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.dog.img, (self.dog.x_pos, self.dog.y_pos))
        self.screen.blit(self.feces.img, (self.feces.x_pos, self.feces.y_pos))
        
        self.score_display = self.game_font.render(str(self.score), True, (0, 0, 0))
        self.screen.blit(self.score_display, (10, 10))

        pygame.display.update()

    def event_check(self):
        for event in pygame.event.get():

            # 종료 이벤트
            self.quit_event(event)

            # 키보드 이벤트
            self.key_event(event)

    def quit_event(self, event):
        if event.type == pygame.QUIT:
            self.close_run()

    def key_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.dog.update_to_x(True)
            elif event.key == pygame.K_RIGHT:
                self.dog.update_to_x(False)

        if event.type == pygame.KEYUP:
            self.dog.stop()

    def move_object(self, dt):
        self.dog.move(dt)
        self.feces.down(dt)

    def border_check(self):

        # 강아지의 경계 처리, 
        if self.dog.x_pos <= 0:
            self.dog.x_pos = 0

        elif self.dog.x_pos >= self.screen_width - self.dog.width:
            self.dog.x_pos = self.screen_width - self.dog.width

        # 똥의 경계처리
        # 똥이 경계에 닿게되면 떨어지는 행동을 종료하고 점수를 증가시킨다.
        if self.feces.y_pos >= self.screen_height - self.feces.height:
            self.downing = False
            self.score += SCORE_SIZE

    def check_colision(self):
        self.dog.update_rect()
        self.feces.update_rect()

        if self.dog.rect.colliderect(self.feces.rect):
            self.close_run()
            
    def close_run(self):
        self.running = False
        self.downing = False

    def run(self):

        # 메인 루프
        self.running = True
        while self.running:
            self.feces.pos_init(self.screen_width)

            # 똥이 떨어지는 동안의 루프
            self.downing = True
            while self.downing:
                dt = self.clock.tick(60)

                # 이벤트 체크
                self.event_check()

                # 객체 이동
                self.move_object(dt)      

                # 객체간 충격 처리
                self.check_colision()

                # 경계 처리
                self.border_check()

                # 화면 갱신
                self.display_update()

        pygame.quit()

    def process(self):
        self.load_resource()
        self.run()
        pygame.time.delay(2000)