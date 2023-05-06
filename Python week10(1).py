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