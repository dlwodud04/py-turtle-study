# 1차원 리스트, 2차원 리스트
num = [10,20,30,40,50,60]
print(num)

num = [[10,20,30],[40,50,60]]
print(num)

#%% 2차원 리스트

num = [[10,20,30],[40,50,60]]

print(num[0][0])
print(num[0][1])
print(num[0][2])
print(num[1][0])
print(num[1][1])
print(num[1][2])

num[1][2] = 100
print(num)

#%% 2차원 리스트 예제 1코드
# [i 인덱스] vs [in List]

import turtle

pos_list = [[100,100],
            [100,-100],
            [-100,100],
            [-100,-100]]

for i in range(len(pos_list)):
    t = turtle.Turtle()
    t.shape("turtle")
    t.goto(pos_list[i][0],pos_list[i][1])
    
turtle.extionclick()
turtle.bye()

#%% [in List]

import turtle

pos_list = [[100,100],
            [100,-100],
            [-100,100],
            [-100,-100]]

for pos_each in pos_list:
    t = turtle.Turtle()
    t.shape("turtle")
    t.goto(pos_each[0],pos_each[1])
    
turtle.extionclick()
turtle.bye()

#%% 거북이 리스트 저장 가능 (t_list)

import turtle

pos_list = [[100,100],
            [100,-100],
            [-100,100],
            [-100,-100]]

t_list = []
for i in range(len(pos_list)):
    t = turtle.Turtle()
    t.shape("turtle")
    t_list.append(t)
    
for i in range(len(t_list)):
    t_list[i].goto(pos_list[i][0],pos_list[i][1])
    
turtle.extionclick()
turtle.bye()
  
#%% 이미지 압축 실습

from PIL import Image

image = Image.open('pet01.gif')    
photo = image.convert('RGB')

photo.show()

#%% 이미지 압축 실습

from PIL import Image

image = Image.open('pet02.gif')    
photo = image.convert('RGB')

photoAry=[]
h = photo.height
w = photo.width
for i in range(h):
    for k in range(w):
        r,g,b = photo.getpixel((i,k))
        value = (r+g+b) // 3
        photoAry.append(value)
        
# 이 부분에 필요한 내용을 추가
pos = 0
px = photo.load()
for i in range(h):
    for k in range(w):
        r = g = b = photoAry[pos]
        pos += 1
        px[i,k] = (r,g,b)
photo.show()

#%% 1차원 배열을 흑백 값으로 변환 후 출력

from PIL import Image

image = Image.open('pet02.gif')    
photo = image.convert('RGB')

# 이 부분에 필요한 내용을 추가
for i in range(len(photoAry)):
    if photoAry[i] <= 127:
        photoAry[i] = 0
    else : 
        photoAry[i] = 255

pos = 0
px = photo.load()
for i in range(h):
    for k in range(w):
        r = g = b = photoAry[pos]
        pos += 1
        px[i,k] = (r,g,b)
photo.show()

#%% 0과 255를 나누는 기준 값을 127에서 midValue(중앙값)으로 변경

from PIL import Image

image = Image.open('pet02.gif')    
photo = image.convert('RGB')

# 이 부분에 필요한 내용을 추가
dataAry = photoAry[:]
dataAry.sort()
midValue = dataAry[h*w // 2]

for i in range(len(photoAry)):
    if photoAry[i] <= midValue :
        photoAry[i] = 0
    else : 
        photoAry[i] = 255

pos = 0
px = photo.load()
for i in range(h):
    for k in range(w):
        r = g = b = photoAry[pos]
        pos += 1
        px[i,k] = (r,g,b)
photo.show()

#%% 

import turtle

t = turtle.Turtle()
t.shape("turtle")

x = 0
y = 0
x_vel = 3
y_vel = 3

for i in range(100):
    x = x+ x_vel
    y = y+ y_vel
    t.goto(x,y)
    
turtle.exitonclick()
turtle.bye()



#%% 속도 예제

pos_list = [[0,0],
            [0,0],
            [0,0]]

vel_list = [[2,0],
            [0,2],
            [2,2]]

for step in range(10):
    for i in range(len(pos_list)):
        pos_list[i][0] = pos_list[i][0] + vel_list[i][0] 
        pos_list[i][1] = pos_list[i][1] + vel_list[i][1]
    print(pos_list)

#%% 2차원 리스트 실습 코드

import turtle

t = turtle.Turtle()
t.shape("turtle")

pos_list = [[0,0],
            [0,0],
            [0,0]]

vel_list = [[2,0],
            [0,2],
            [2,2]]

t_list = []

for i in range(len(pos_list)):
    t = turtle.Turtle()
    t.shape("turtle")
    t_list.append(t)
    
for i in range(100):
    for i in range(len(pos_list)):
        pos_list[i][0] = pos_list[i][0] + vel_list[i][0] 
        pos_list[i][1] = pos_list[i][1] + vel_list[i][1]
        
        t_list[i].goto(-pos_list[i][0],pos_list[i][1])
        
turtle.exitonclick()
turtle.bye()

#%% 외각선 그리기

import turtle

tline = turtle.Turtle()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

tline.up()
tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
tline.down()

tline.goto(-SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
tline.goto(-SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
tline.goto(SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

turtle.exitonclick()
turtle.bye()

#%% 외각선 그리기 함수

import turtle

def outline():
    tline = turtle.Turtle()
    
    tline.up()
    tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    tline.down()

    tline.goto(-SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    tline.goto(-SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300


# 충돌 위치 판단 예제

import turtle

outline()

asteroid = turtle.Turtle()
asteroid.shape("circle")

loc = [0,0]
vel = [0,5]

asteroid.goto(loc[0], loc[1])

for i in range(200):
    loc[0] = loc[0] + vel[0]
    loc[1] = loc[1] + vel[1]
    
    asteroid.goto(loc[0],loc[1])
    
    if loc[1] >= SCREEN_HEIGHT/2:
        vel[1] = -vel[1]
    
    if loc[1] <= -SCREEN_HEIGHT/2:
        vel[1] = -vel[1]
turtle.exitonclick()
turtle.bye()




























