import pygame
import random

############################## 초기화 ##############################
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥 피하기")

clock = pygame.time.Clock()

############################## 배경, 캐릭터 ##############################

# 배경
background = pygame.image.load("pygame_basic/background.png")

# 캐릭터
char = pygame.image. load("pygame_basic/character.png")
char_size = char.get_rect().size
char_width = char_size[0]
char_height = char_size[1]
char_x_pos = (screen_width / 2) - (char_width / 2)
char_y_pos = screen_height - char_height
char_speed = 0.6
to_x = 0

# 똥
enemy = pygame.image.load("pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = 0
enemy_y_pos = 0
enemy_speed = 0.05
to_y = 0

# 폰트
game_font = pygame.font.Font(None, 40)

# 점수
score = 0
SCORE_SIZE = 10

############################## main ##############################
running = True
while running:
    enemy_x_pos = random.randrange(0, screen_width - enemy_width + 1)
    enemy_y_pos = 0
    to_y = 0

    downing = True
    while downing:
        dt = clock.tick(30)

        for event in pygame.event.get():
            # 종료 버튼 이벤트
            if event.type == pygame.QUIT:
                downing = False
                running = False

            # 키보드 이벤트
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= char_speed
                elif event.key == pygame.K_RIGHT:
                    to_x += char_speed

            if event.type == pygame.KEYUP:
                to_x = 0

        char_x_pos += to_x * dt

        to_y += enemy_speed
        enemy_y_pos += to_y * dt

        if char_x_pos <= 0:
            char_x_pos = 0
        elif char_x_pos >= screen_width - char_width:
            char_x_pos = screen_width - char_width

        if enemy_y_pos >= screen_height - enemy_height:
            downing = False
            score += SCORE_SIZE

        char_rect = char.get_rect()
        char_rect.left = char_x_pos
        char_rect.top = char_y_pos

        enemy_rect = enemy.get_rect()
        enemy_rect.left = enemy_x_pos
        enemy_rect.top = enemy_y_pos

        if char_rect.colliderect(enemy_rect):
            downing = False
            running = False

        screen.blit(background, (0, 0))
        screen.blit(char,(char_x_pos, char_y_pos))
        screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

        score_label = game_font.render(str(score), True, (255, 255, 255))
        screen.blit(score_label, (10, 10))

        pygame.display.update()


pygame.time.delay(2000)

pygame.quit()