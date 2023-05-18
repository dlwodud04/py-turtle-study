#%% 
import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()



#%% pygame 기본 구조

import pygame
import sys # 파이썬 인터프리터 제어
import time 

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init() # pygame 초기화
pygame.display.set_caption('SpaceShuttle') # 창 제목 설정
# 지정 크기 창 생성
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
myFont = pygame.font.SysFont("arial", 30, True,False)
imgShuttle = pygame.image.load('rocket.png')
clock = pygame.time.Clock()


loc = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2] # 화면 가운데 설정
vel = [4,0]
startTime = time.time()

while True:
    clock.tick(30)
    screen.fill((0,0,0))
        
    for event in pygame.event.get():  # 발생한 입력 event 목록의 event 마다 검사
        if event.type == pygame.QUIT: # event의 type이 QUIT에 해당할 경우
            pygame.quit()             # pygame을 종료한다
            sys.exit()                # 창을 닫는다
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        loc[0] -=3
    if keys[pygame.K_RIGHT]:
        loc[0] +=3
    if keys[pygame.K_UP]:
        loc[1] -=3
    if keys[pygame.K_DOWN]:
        loc[1] +=3
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
    
    loc[0] = loc[0] + vel[0]
    loc[1] = loc[1] + vel[1]
    
    if loc[0] >= SCREEN_WIDTH:
        vel[0] = -vel[0]
    if loc[0] <= -SCREEN_WIDTH:
        vel[0] = -vel[0]
    if loc[1] >= SCREEN_HEIGHT:
        vel[1] = -vel[1]
    if loc[1] <= -SCREEN_HEIGHT:
        vel[1] = -vel[1]
    
    loc_text = myFont.render(str(loc),1,(255,255,255))
    screen.blit(loc_text, [20,20])
    loc_text = myFont.render(str(loc),1,(255,255,255))
    screen.blit(loc_text, [200,20])
    pygame.draw.circle(screen, (255,255,255),(SCREEN_WIDTH/2,SCREEN_HEIGHT/2) , 10)
    time_diff = str(time.time() - startTime)
    currentTime_text = myFont.render(time_diff,1, (255,255,255))
    screen.blit(currentTime_text,[SCREEN_WIDTH-70,20])
    screen.blit(imgShuttle, loc)
    pygame.display.update()
#%%

import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init() # pygame 초기화
pygame.display.set_caption('SpaceShuttle')

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
myFont = pygame.font.SysFont("arial", 30, True,False)

clock = pygame.time.Clock()

loc = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
vel = [4,]

while True:
    clock.tick(30)
    screen.fill((0,0,0))
        
    for event in pygame.event.get():  # 발생한 입력 event 목록의 event 마다 검사
        if event.type == pygame.QUIT: # event의 type이 QUIT에 해당할 경우
            pygame.quit()             # pygame을 종료한다
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
        
    loc[0] = loc[0] + vel[0]
    loc[1] = loc[1] + vel[1]

    if loc[0] >= SCREEN_WIDTH:
        vel[0] = -vel[0]
    if loc[0] <= 0 :
        vel[0] = -vel[0]
    if loc[1] >= SCREEN_HEIGHT:
        vel[1] = -vel[1]
    if loc[1] <= 0 :
        vel[1] = -vel[1]
        
    loc_text = myFont.render(str(loc),1,(255,255,255))
    screen.blit(loc_text, [20,20])
    loc_text = myFont.render(str(loc),1,(255,255,255))
    screen.blit(loc_text, [200,20])

    pygame.draw.circle(screen, (255,255,255),loc , 10)
    pygame.display.update()

#%% 충돌 판단

import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init() # pygame 초기화
pygame.display.set_caption('SpaceShuttle')

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
imgShuttle = pygame.image.load('rocket.png')
img_width = imgShuttle.get_width()
img_height = imgShuttle.get_height()
clock = pygame.time.Clock()

loc_rock = [100, 100]
size_rock = 10

loc_ship = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
size_ship = 20

myFont = pygame.font.SysFont("arial",30,True,False)
def collision_check(loc_rock, size_rock, loc_ship, size_ship):
    dist_x = loc_rock[0] - loc_ship[0] - img_width/2
    dist_y = loc_rock[1] - loc_ship[1] - img_height/2
    dist = (dist_x**2 + dist_y**2)**(0.5)
    
    if dist < (size_rock + size_ship):
        text = myFont.render("collision", 1, (255,0,0))
        screen.blit(text,[20,20])
    
while True:
    clock.tick(30)
    screen.fill((0,0,0))
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        loc_ship[0] -=3
    if keys[pygame.K_RIGHT]:
        loc_ship[0] +=3
    if keys[pygame.K_UP]:
        loc_ship[1] -=3
    if keys[pygame.K_DOWN]:
        loc_ship[1] +=3
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
        
    for event in pygame.event.get():  # 발생한 입력 event 목록의 event 마다 검사
        if event.type == pygame.QUIT: # event의 type이 QUIT에 해당할 경우
            pygame.quit()             # pygame을 종료한다
            sys.exit()

    pygame.draw.circle(screen,(0,255,0),loc_rock, size_rock,2)
    
    pygame.draw.circle(screen,(255,255,255),(loc_ship[0]+img_width/2,loc_ship[1]+img_height/2), size_ship,1)    
    screen.blit(imgShuttle,loc_ship)
    
    collision_check(loc_rock, size_rock, loc_ship, size_ship)
    pygame.display.update()










