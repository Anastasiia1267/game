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
            self.loss_Of_Life()
            self.speed = 0
            self.up = 0
            self.time_return = 60
            self.start = True
            
               
    def loss_Of_Life(self):
        if self.life:
            self.life -= 1

class pipes(pygame.sprite.Sprite):
    def __init__(self, x, y, img_pipes_top, img_pipes_bottom, *group):
        super().__init__(*group)
        self.w = 800
        self.h = 600
        self.rect.x = x
        self.rect.y = y
        self.pipe.x = self.w
        self.pipe.y = self.h
        self.pipes = []
        self.img_pipes_top = img_pipes_top
        self.img_pipes_bottom = img_pipes_bottom


    def motion(self):   
        for i in range(len(self.pipes) - 1, - 1, - 1):
            pipe = self.pipes[i]
            self.pipe.x -= 3
            if pipe.right < 0:
                self.pipes.remove(pipe)
            self.start = True
            

    def creation(self):            
        if len(self.pipes) == 0 or self.pipes[len(self.pipes) - 1].x < self.w - 200:
            self.pipes.append(pygame.Rect(self.w, 0, 70, 140))
            self.pipes.append(pygame.Rect(self.w, 420, 70, 220))
        
def update(self,img_pipes_top, img_pipes_bottom):
    self.img_pipes_top = img_pipes_top
    self.img_pipes_bottom = img_pipes_bottom
    press = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    click = keys[pygame.K_SPACE] or press[0]
    self.frame = (self.frame + 0.05) % 7   
    self.image = self.images.subsurface(111 * int(self.frame), 0, 111, 106)
    self.move(click)
    if self.time_return > 0:
        self.time_return -= 1
    for pipe in self.pipes:
        if self.pipe.y== 0:
            self.rect = self.img_pipes_top.get_rect(bottomleft = pipe.bottomleft)
        else:
            self.rect = self.img_pipes_bottom.get_rect(topleft = pipe.topleft)
    
        # if state == 'start':
        #     if click and timer == 0 and len(pipes) == 0:
        #         state = 'play'
            
        # elif state == 'play':
        #     if click:
        #         ay = -2
        #     else:
        #         ay = 0
        #     if not(player.top < 0 or player.bottom > HEIGHT):
        #         scores += 1

        #     py += sy
        #     sy = (sy + ay + 1) * 0.95
        #     player.y = py

        #     if len(pipes) == 0 or pipes[len(pipes) - 1].x < WIDHT - 200:
        #         pipes.append(pygame.Rect(WIDHT, 0, 70, 140))
        #         pipes.append(pygame.Rect(WIDHT, 420, 70, 220))

        #     if player.top < 0 or player.bottom > HEIGHT:
        #         state = 'fall'

        #     for pipe in pipes:
        #         if player.colliderect(pipe):                
        #                 state = 'fall'
        # elif state == 'fall':          
        #     lives -= 1
        #     if lives == 0:
        #         start_menu() 
        #     sy, ay = 0, 0
        #     state = 'start'
        #     timer = 60  