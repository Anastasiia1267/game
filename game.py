import sys
import pygame
import pygame_menu
import os
from random import randint
from sprite import Player,Pipes


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

# подгрузка изображений
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

# Дизайн меню
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
# Содержимое меню
def start_menu(theme = my_theme):
    """Запуск меню"""
    menu = pygame_menu.Menu('', width = WIDHT,height = HEIGHT, theme=theme)
    menu.add.button('PLAY', start_game)
    menu.add.button('EXIT', pygame_menu.events.EXIT)
    # цикл меню
    menu.mainloop(window)
#  Игра
def start_game():
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    pipe_group = pygame.sprite.Group()
    player = Player(img_fin, WIDHT // 3, HEIGHT // 2, 111, 106, player_group, all_sprites)
    pipes = [] 
    scores = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()               
        scores += 1

        # движение фона
        for i in range(len(bgs) - 1, - 1, - 1):
            bg = bgs[i]
            bg.x -= 1
            if bg.right < 0:
                bgs.remove(bg)
            if bgs[len(bgs) - 1]. right <= WIDHT:
                bgs.append(pygame.Rect(bgs[len(bgs) - 1].right, 0, 600, 600))

        # добавление труб
        if len(pipes) == 0 or pipes[len(pipes) - 1].rect.x < WIDHT - 200:
            pipes.append(Pipes(WIDHT+ randint(100, 250), 0,[img_pipes_bottom, img_pipes_top], pipe_group, all_sprites))
            pipes.append(Pipes(WIDHT + randint(20, 200), 500,[img_pipes_bottom, img_pipes_top], pipe_group, all_sprites))          
        player_group.update()
        pipe_group.update(player, player_group)

        # прорисовка фона
        for bg in bgs:
            window.blit(img_bg, bg)

        # если игрок проигрывает, то переходит в финальное окно
        if player.life == 0:
            game_over(scores)

        #  текст
        all_sprites.draw(window)
        text = font_35.render('SCORES: ' + str(scores), 1, pygame.Color('black'))
        window.blit(text, (10, 10))
        text = font_35.render('LIFES: ' + str(player.life), 1, pygame.Color('black'))
        window.blit(text, (10, HEIGHT - 30))

        pygame.display.update()
        clock.tick(FPS)

# дизайн финального окна
img_game_over = pygame_menu.baseimage.BaseImage(
    image_path='img/menu.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
    drawing_offset = (0, 0)   
)
img_game_over.resize(WIDHT, HEIGHT)
my_theme_game_over = pygame_menu.themes.Theme(
    background_color=img_game_over,
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

# содержимое финального окна
def game_over(scores, theme = my_theme_game_over):
    menu = pygame_menu.Menu("GAME OVER \n YOUR SCORES: " + str(scores), width = WIDHT,height = HEIGHT, theme=theme)
    menu.add.button('BACK TO GAME', start_game)
    menu.add.button('EXIT', pygame_menu.events.EXIT)
    menu.mainloop(window)

# выход из игры 
def terminate():
    """Выйти из игры"""
    pygame.quit()
    sys.exit()

start_menu()

