from re import T
import pygame

# Инициализация
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self,images, x, y, w, h,*group):
        super().__init__(*group)
        self.frame = 0
        self.images = images
        self.image = self.images.subsurface(111 * self.frame , 0, 111, 106)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.life = 3
        self.speed = 0
        self.start = True
        self.time_return = 10
        self.gravity = y 
        self.y = y
        self.up = 0

    def move(self, click) :
        if self.start:
            if click and self.time_return == 0:
                self.start = False
            self.gravity  += (self.y - self.gravity ) * 0.1
            self.rect.y = self.gravity         
        elif not self.start: 
            if click:
                self.speed = -2
            else:
                self.speed = 0
            self.gravity += self.up
            self.up = (self.up + self.speed  + 1) * 0.95
            self.rect.y = self.gravity
        
        if self.rect.top < 0 or self.rect.bottom > (self.y * 2):
            self.fall()
            
    def fall(self):
        self.loss_Of_Life()
        self.speed = 0
        self.up = 0
        self.time_return = 60
        self.start = True

    def update(self):
        press = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        click = keys[pygame.K_SPACE] or press[0]
        self.frame = (self.frame + 0.05) % 7   
        self.image = self.images.subsurface(111 * int(self.frame), 0, 111, 106)
        self.move(click)
        if self.time_return > 0:
            self.time_return -= 1
        
    def loss_Of_Life(self):
        if self.life:
            self.life -= 1

class Pipes(pygame.sprite.Sprite):
    def __init__(self, x, y, imges, *group):
        super().__init__(*group)
        self.w = 800
        self.h = 600  
        if y == 0:
            self.image = imges[0]
        else:
            self.image = imges[1]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y      

    def update(self, target, group_target):
        self.rect.x -= 3
        if self.rect.right < 0:
                self.kill()
        if pygame.sprite.spritecollide(self, group_target, False): 
            target.fall()
