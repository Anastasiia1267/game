import sys
import pygame
import pygame_menu
import os

from sprite import Player

# Инициализация
pygame.init()

#  основные переменные и константы
size = (WIDHT, HEIGHT) = (800, 600)
FPS = 60
window = pygame.display.set_mode((WIDHT, HEIGHT))
pipes = []
bgs = []
bgs.append(pygame.Rect(0, 0, 600, 600))
clock = pygame.time.Clock()

def load_image(name):
    '''Загрузка изображений из папки img'''
    fullname = os.path.join('img', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

# Дизайн
img_bg = load_image('background.png')
img_fin = load_image('fin.png')
font_35 = pygame.font.Font(None, 35)
img_pipes_bottom = load_image('pipes_bottom.png')
img_pipes_top = load_image('pipes_top.png')

# Меню
img_menu = pygame_menu.baseimage.BaseImage(
    image_path='img/menu.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
    drawing_offset = (0, 0)   
)
img_menu.resize(WIDHT, HEIGHT)
my_theme = pygame_menu.themes.Theme(
    background_color=img_menu,
    widget_alignment=pygame_menu.locals.ALIGN_LEFT,
    widget_background_color=(4, 21, 48),
    title_background_color=(0, 0, 0),
    widget_font=pygame_menu.font.FONT_FRANCHISE,
    title_font=pygame_menu.font.FONT_FRANCHISE,
    widget_font_size=50,
    title_font_size=35,
    widget_font_color=(255, 0, 0),
    widget_margin=(20, 50),
    widget_offset= (20, 300),
    widget_padding=10,
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE
)

def start_menu(theme = my_theme):
    """Запуск меню"""
    menu = pygame_menu.Menu('', width = WIDHT,height = HEIGHT, theme=theme)
    menu.add.button('Play', start_game)
    menu.add.button('Exit', pygame_menu.events.EXIT)
    # цикл меню
    menu.mainloop(window)

def start_game():
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    player = Player(img_fin, WIDHT // 3, HEIGHT // 2, 111, 106, player_group, all_sprites)
    
    scores = 0
    # frame = 0
    # state = 'start'
    # timer = 10
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()               
        # press = pygame.mouse.get_pressed()
        # keys = pygame.key.get_pressed()
        # click = keys[pygame.K_SPACE] or press[0]

        # if timer > 0:
        #     timer -= 1
        # frame = (frame + 0.05) % 7

        for i in range(len(bgs) - 1, - 1, - 1):
            bg = bgs[i]
            bg.x -= 1
            if bg.right < 0:
                bgs.remove(bg)
            if bgs[len(bgs) - 1]. right <= WIDHT:
                bgs.append(pygame.Rect(bgs[len(bgs) - 1]. right, 0, 600, 600))
                
        # for i in range(len(pipes) - 1, - 1, - 1):
        #     pipe = pipes[i]
        #     pipe.x -= 3
        #     if pipe.right < 0:
        #         pipes.remove(pipe)

        # if state == 'start':
        #     if click and timer == 0 and len(pipes) == 0:
        #         state = 'play'
        #     py += (HEIGHT // 2 - py) * 0.1
        #     player.y = py
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
        all_sprites.update()             

        for bg in bgs:
            window.blit(img_bg, bg)

        # for pipe in pipes:
        #     if pipe.y == 0:
        #         rect = img_pipes_top.get_rect(bottomleft = pipe.bottomleft)
        #         window.blit(img_pipes_top, rect)
        #     else:
        #         rect = img_pipes_bottom.get_rect(topleft = pipe.topleft)
        #         window.blit(img_pipes_bottom, rect)
            
        all_sprites.draw(window)
        # fin = img_fin.subsurface(111 * int(frame) , 0, 111, 106)
        # window.blit(fin, player)

        text = font_35.render('Очки: ' + str(scores), 1, pygame.Color('black'))
        window.blit(text, (10, 10))

        text = font_35.render('Жизни: ' + str(player.life), 1, pygame.Color('black'))
        window.blit(text, (10, HEIGHT - 30))

        pygame.display.update()
        clock.tick(FPS)


def terminate():
    """Выйти из игры"""
    pygame.quit()
    sys.exit()

start_menu()
