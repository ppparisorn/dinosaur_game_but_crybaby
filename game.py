import pygame
from sys import exit
from random import randint

def obstacle_movement(obstacle_list):
    if obstacle_list :
        for obstacle_rect in obstacle_list :
            obstacle_rect.x -= 5
            if obstacle_rect.y == 490 : screen.blit(floor_surface , obstacle_rect)
            else : screen.blit(fly_surface , obstacle_rect)
    obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.right > 0]
    return obstacle_list

def collisions(player , obstacles):
    global title , game_active
    if obstacles :
        for obstacle_rect in obstacles :
            if player.colliderect(obstacle_rect): title = game_active = False
def display_score() :
    current_time = (pygame.time.get_ticks() - start_time)//1000
    score_surface = test_font.render(f'{current_time}' , False , 'Black')
    score_rect = score_surface.get_rect(center = (1523/2 , 50))
    screen.blit(score_surface , score_rect)
  #  print(current_time)
    return current_time

pygame.init()
screen = pygame.display.set_mode((1523 , 780))
pygame.display.set_caption('My game.')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Mali-Regular.ttf' , 50)

ground_surface = pygame.image.load('ground.jpg').convert_alpha()
game_over_surface = pygame.image.load('game_over.jpg').convert_alpha()

text_surface = test_font.render('The coward child' , False , 'Black')
text_rect = text_surface.get_rect(center = (1523/2 , 50))

game_surface = test_font.render('Press "SPACE" to start' , False , 'Black')
game_rect = text_surface.get_rect(center = (1523/2 , 600))

#Obstacle
fly_surface = pygame.image.load('fly.png').convert_alpha()
fly_rect = fly_surface.get_rect(topleft = (600 , 390))

floor_surface = pygame.image.load('floor.png').convert_alpha()
floor_rect = floor_surface.get_rect(topleft = (600 , 490))

obstacle_rect_list = []
#Player
baby_surface = pygame.image.load('baby.png').convert_alpha()
baby_rect = baby_surface.get_rect(midbottom = (200 , 670))
baby_title = baby_surface.get_rect(center = (1523/2 , 350))
baby_gravity = 0

start_time = 0

game_active = False
title = True

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer , 2000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
                pygame.quit()
                exit()
        if game_active :
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE : baby_gravity = -25
        else :
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
                game_active = True
                floor_rect.left = 800
                fly_rect.left = 800
                start_time = pygame.time.get_ticks()
        if event.type == obstacle_timer and game_active :
            if randint(0,2): obstacle_rect_list.append(fly_surface.get_rect(topleft = (randint(1523 , 1600) , 490)))
            else : obstacle_rect_list.append(fly_surface.get_rect(topleft = (randint(1523 , 1600) , 200)))
    
    if game_active :

        screen.blit(ground_surface , (0 , -100))
        score = display_score()
      #  screen.blit(text_surface , text_rect)
        '''
        fly_rect.x -= 6
        if fly_rect.right < 0 : fly_rect.left = 1523
        screen.blit(fly_surface , fly_rect)

        floor_rect.x -= 7
        if floor_rect.right <= 0 : floor_rect.left = 1523
        screen.blit(floor_surface , floor_rect)
'''
        baby_gravity += 1
        if baby_gravity <= 0 or baby_rect.y < 360 : baby_rect.y += baby_gravity
        if baby_rect.y > 360 : baby_rect.y = 360
        screen.blit(baby_surface , baby_rect)
        
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        collisions(baby_rect , obstacle_rect_list)

        if baby_rect.colliderect(floor_rect) or baby_rect.colliderect(fly_rect) : 
            game_active = False
            title = False
    elif title :
        screen.fill((255 , 255 , 255))
        screen.blit(baby_surface , baby_title)
        screen.blit(text_surface , text_rect)
        screen.blit(game_surface , game_rect)
    
    else : 
        obstacle_rect_list = []
        score_message = test_font.render(f'Your score : {score}' , False , 'Black')
        screen.blit(game_over_surface , (0 , 0))
        screen.blit(score_message , (10 , 10))

    pygame.display.update()
    clock.tick(60)