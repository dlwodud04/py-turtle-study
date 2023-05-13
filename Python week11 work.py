#%% 과제(두 거북이 충돌 및 판단)

import turtle
import time

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

pos_list = [[0,0],
            [0,0]]
vel_list = [[5,5],
            [5,-5]]

t_list = []

startTime = time.time()

for i in range(len(pos_list)):
    t = turtle.Turtle()
    t.shape("turtle")
    t.goto(pos_list[i][0], pos_list[i][1])
    t_list.append(t)

for step in range(200):
    for i in range(len(pos_list)):
        pos_list[i][0] = pos_list[i][0] + vel_list[i][0]
        pos_list[i][1] = pos_list[i][1] + vel_list[i][1]
        
        t_list[i].goto(pos_list[i][0], pos_list[i][1])
        
        if pos_list[i][0] >= SCREEN_WIDTH/2:
            vel_list[i][0] = -vel_list[i][0]
            
        if pos_list[i][0] <= -SCREEN_WIDTH/2:
            vel_list[i][0] = -vel_list[i][0]
            
        if pos_list[i][1] >= SCREEN_HEIGHT/2:
            vel_list[i][1] = -vel_list[i][1]
            
        if pos_list[i][1] <= -SCREEN_HEIGHT/2:
            vel_list[i][1] = -vel_list[i][1]
             

endTime = time.time() - startTime
turtle.write(endTime)
turtle.exitonclick()
turtle.bye()           
            