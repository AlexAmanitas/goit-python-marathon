import pygame 
from pygame.constants import QUIT
import random

pygame.init()

RED = 255,0,0
BLACK = 0,0,0

screen = width, height= 800, 600

main_surface =  pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(RED)
ball_rect = ball.get_rect()
ball_speed = [1, 1]

is_working = True

while is_working:
   for event in pygame.event.get():
      if event.type == QUIT:
        is_working = False

   ball_rect = ball_rect.move(ball_speed) 

   if ball_rect.bottom >= height or ball_rect.top <= 0:
      red = random.randint(0,255)
      green = random.randint(0,255)
      blue = random.randint(0,255)
      ball_speed[1] = -ball_speed[1]
      ball.fill((red, green, blue))
      
   if ball_rect.right >= width or ball_rect.left <= 0:
      red = random.randint(0,255)
      green = random.randint(0,255)
      blue = random.randint(0,255)
      ball_speed[0] = -ball_speed[0]
      ball.fill((red, green, blue))

   main_surface.fill(BLACK)    
   main_surface.blit(ball, ball_rect)		
   
   pygame.display.flip()