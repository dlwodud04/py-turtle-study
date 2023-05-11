#%% import

import math
result = math.ceil(3.14)
print(result)
result = math.ceil(4.54)
print(result)

#%% import from

from math import ceil
result = ceil(3.14)
print(result)
result = ceil(4.54)
print(result)

#%% import from(2)

from math import *
result = ceil(3.14)
print(result)
result = ceil(4.54)
print(result)

#%% datetime 모듈

import datetime

nowTime = datetime.datetime.now()
print(nowTime)

#%% datetime 모듈 (날짜 계산하기)

import datetime

Memorial = datetime.date(2004, 7, 29)
nowTime = datetime.date.today()
timeDiff = nowTime - Memorial
print(timeDiff)

#%% datetime 모듈 (날짜 계산기)

from datetime import date

Memorial = date(2004, 7, 29)
nowTime = date.today()
timeDiff = nowTime - Memorial
print(timeDiff)

#%% datetime 모듈 (날짜 계산하기)

import datetime

Memorial = datetime.datetime(2004, 7, 29,00,00)
nowTime = datetime.datetime.now()
timeDiff = nowTime - Memorial
print(timeDiff)

#%% datetime 시간 차이 계산하기

from datetime import datetime

startTime = datetime.now()

while True : 
    currTime = datetime.now()
    timeDiff = currTime - startTime
    print(timeDiff)

#%% datetime 모듈 (세부 시간 확인하기)

from datetime import datetime

while True : 
    currTime = datetime.now()
    timeDiff = currTime - startTime
    print(timeDiff.microseconds)
    
#%% time 모듈 사용

import time

startTime = time.time()

while True :
    timeDiff = (time.time() - startTime)
    print(timeDiff)
    if timeDiff > 10 :
        break
    
#%% time 모듈 (프로그램 일시 중단)

import time

startTime = time.time()

while True :
    timeDiff = (time.time()-startTime)
    print(timeDiff)
    time.sleep(1.0)
    if timeDiff > 10:
        break

#%% time 모듈 활용

import turtle
import time

t = turtle.Turtle()
t.shape("turtle")

t.fd(100)
t.left(120)
time.sleep(0.5)
t.fd(100)
t.left(120)
time.sleep(0.5)
t.fd(100)

turtle.exitonclick()
turtle.bye()

#%% 충돌 판단하기 예제

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

outline()

asteroid = turtle.Turtle()
asteroid.shape("circle")

loc = [100,100]
vel = [4,-4]

asteroid.goto(loc[0],loc[1])

for i in range(100):
    loc[0] = loc[0] + vel[0]
    loc[1] = loc[1] + vel[1]
    
    if loc[0] >= SCREEN_WIDTH/2:
        loc[0] = SCREEN_WIDTH/2*2 - loc[0]
        vel[0] = -vel[0]
    
    if loc[1] <= -SCREEN_WIDTH/2:
        vel[1] = -vel[1]
        
    asteroid.goto(loc[0],loc[1])
    
turtle.exitonclick()
turtle.bye()


#%%
turtle.bye()




















