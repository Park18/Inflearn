import pygame
import random

class Character:
    def __init__(self, img_path, speed):
        self.img = pygame.image.load(img_path)
        self.size = self.img.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x_pos = 0
        self.y_pos = 0
        self.speed = speed
        self.rect = self.img.get_rect()
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos

    def update_rect(self):
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos

class Dog(Character):
    def __init__(self, img_path, speed, screen_width, screen_height):
        super().__init__(img_path, speed)
        self.x_pos = (screen_width / 2) - (self.width / 2)
        self.y_pos = screen_height - self.height
        self.to_x = 0

    def update_to_x(self, is_left):
        if is_left:
            self.to_x -= self.speed
        else:
            self.to_x += self.speed

    def move(self, dt):
        self.x_pos += self.to_x * dt

    def stop(self):
        self.to_x = 0

class Feces(Character):
    def __init__(self, img_path, speed):
        super().__init__(img_path, speed)
        self.to_y = 0

    def down(self, dt):
        self.to_y += self.speed
        self.y_pos += self.to_y * dt

    def pos_init(self, screen_width):
        #print(str(self.widht) + ',' + str(screen_width))
        self.x_pos = random.randrange(0, (screen_width - self.width + 1))
        self.y_pos = 0
        self.to_y = 0