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

    def move(self):
        pass


    def loss_Of_Life(self):
        pass


    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1, 
                                   random.randrange(3) - 1)
        press = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        click = keys[pygame.K_SPACE] or press[0]
        self.frame = int((self.frame + 0.05) % 7)    
        self.image = self.images.subsurface(111 * self.frame , 0, 111, 106)
        if state == 'start':
            if click and timer == 0 and len(pipes) == 0:
                state = 'play'
            py += (HEIGHT // 2 - py) * 0.1
            player.y = py
        elif state == 'play':
            if click:
                ay = -2
            else:
                ay = 0
            if not(player.top < 0 or player.bottom > HEIGHT):
                scores += 1

            py += sy
            sy = (sy + ay + 1) * 0.95
            player.y = py

            if len(pipes) == 0 or pipes[len(pipes) - 1].x < WIDHT - 200:
                pipes.append(pygame.Rect(WIDHT, 0, 70, 140))
                pipes.append(pygame.Rect(WIDHT, 420, 70, 220))

            if player.top < 0 or player.bottom > HEIGHT:
                state = 'fall'

            for pipe in pipes:
                if player.colliderect(pipe):                
                        state = 'fall'
        elif state == 'fall':          
            lives -= 1
            if lives == 0:
                start_menu() 
            sy, ay = 0, 0
            state = 'start'
            timer = 60             
                      


