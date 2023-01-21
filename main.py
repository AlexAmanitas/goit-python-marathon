import pygame 
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
import random

pygame.init()

FPS = pygame.time.Clock()

RED = 255,0,0
BLACK = 0,0,0
WHITE = 255,255,255
BLUE = 0,130,209
YELLOW = 255,209,0

font = pygame.font.SysFont('Verdana', 30)

screen = width, height= 800, 600

main_surface =  pygame.display.set_mode(screen)

# player = pygame.Surface((20, 20))
# player.fill(WHITE)

player = pygame.image.load('images/goose/1-1.png').convert_alpha()


# player = [
#     pygame.image.load('images/goose/1-1.png').convert_alpha(),
#     pygame.image.load('images/goose/1-2.png').convert_alpha(),
#     pygame.image.load('images/goose/1-3.png').convert_alpha(),
#     pygame.image.load('images/goose/1-4.png').convert_alpha(),
#     pygame.image.load('images/goose/1-5.png').convert_alpha(),
# ]

player_rect = player.get_rect()
player_speed = 8

anima_player_count = 0

bg = pygame.transform.scale(pygame.image.load('images/background.png').convert(), screen) 
bgX = 0
bgX2 = bg.get_width()
bg_speed = 3

def create_enemy():
    enemy = pygame.image.load('images/enemy.png').convert_alpha()
    enemy_rect = pygame.Rect(width, random.randint(0,height), *enemy.get_size())
    enemy_speed = random.randint(2,5)
    return [enemy, enemy_rect, enemy_speed]

CREATE_ENEMY = pygame.USEREVENT+1
pygame.time.set_timer(CREATE_ENEMY, 1500)

enemies = []

def create_bonus():
    bonus = pygame.image.load('images/bonus.png').convert_alpha()
    bonus_rect = pygame.Rect(random.randint(0,300), 0, *bonus.get_size())
    bonus_speed = random.randint(2,4)
    return [bonus, bonus_rect, bonus_speed]

CREATE_BONUS = pygame.USEREVENT+2
pygame.time.set_timer(CREATE_BONUS, 1000)

bonuses = []

scores = 0

is_working = True

while is_working:

    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
             is_working = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())

        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

    pressed_keys = pygame.key.get_pressed()

    # main_surface.blit(bg,(0,0)) 

    bgX -= bg_speed
    bgX2 -= bg_speed

    if bgX < -bg.get_width():
        bgX = bg.get_width()
        
    if bgX2 < -bg.get_width():
        bgX2 = bg.get_width()



    main_surface.blit(bg, (bgX,0))
    main_surface.blit(bg, (bgX2,0))

    main_surface.blit(player, player_rect)	
    main_surface.blit(font.render(str(scores), True, WHITE),( width - 30, 10))

    if anima_player_count == 4:
        anima_player_count = 0
    else:
        anima_player_count += 1

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2],0)
        main_surface.blit(enemy[0], enemy[1])	

        if enemy[1].left < 250:
            enemies.pop(enemies.index(enemy))

        if player_rect.colliderect(enemy[1]):
          is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0,bonus[2])
        main_surface.blit(bonus[0], bonus[1])	

        if bonus[1].bottom > height:
            bonuses.pop(bonuses.index(bonus))

        if player_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            scores += 1


    if pressed_keys[K_DOWN] and not player_rect.bottom >= height:
        player_rect = player_rect.move(0, player_speed)

    if pressed_keys[K_UP] and not player_rect.top <= 0:
        player_rect = player_rect.move(0, -player_speed)

    if pressed_keys[K_RIGHT] and not player_rect.right >= width:
        player_rect = player_rect.move( player_speed,0)

    if pressed_keys[K_LEFT] and not player_rect.left <= 0:
        player_rect = player_rect.move( -player_speed,0)

    pygame.display.flip()



 # enemy_rect = enemy_rect.move(-enemy_speed,0)

    # print(len(bonuses))

    # player_rect = player_rect.move(player_speed) 
  #  if player_rect.bottom >= height or player_rect.top <= 0:
  #     red = random.randint(0,255)
  #     green = random.randint(0,255)
  #     blue = random.randint(0,255)
  #     player_speed[1] = -player_speed[1]
  #     player.fill((red, green, blue))
      
  #  if player_rect.right >= width or player_rect.left <= 0:
  #     red = random.randint(0,255)
  #     green = random.randint(0,255)
  #     blue = random.randint(0,255)
  #     player_speed[0] = -player_speed[0]
  #     player.fill((red, green, blue))