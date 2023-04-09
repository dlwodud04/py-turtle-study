#%% (과제3 세 거북이와 사각형 실습

import turtle
t1 = turtle.Turtle()
t1.shape("turtle")

t2 = turtle.Turtle()
t2.shape("turtle")

t3 = turtle.Turtle()
t3.shape("turtle")

t1.color("blue")
t1.up()
t1.goto(100,100)
t1.down()
t1.goto(100,100)
for i in range(4):
    t1.fd(50)
    t1.left(90)

t2.color("red")
t2.up()
t2.goto(100,-100)
t2.down()
t2.goto(100,-100)
for i in range(4):
    t2.fd(50)
    t2.left(90)

t3.color("green")
t3.up()
t3.goto(-100,-100)
t3.down()
t3.goto(-100,-100)
for i in range(4):
    t3.fd(50)
    t3.left(90)

turtle.exitonclick()
turtle.bye()

#%%(과제4) 승자맞추기

import random
import turtle

text = turtle.textinput("주사위 게임", "t1 or t2")
print("나의 예측 번호 : ", text)

t1_sum = 0
t1_sum = int(t1_sum) 
t2_sum = 0
t2_sum = int(t2_sum) 

while True :
    t1 = random.randint(1,6)
    t1_sum += t1
    t2 = random.randint(1,6)
    t2_sum += t2
    print("t1 : ",t1_sum ,"vs","t2 : ",t2_sum)
    if t1_sum >= 30 or t2_sum >= 30 :
        break
    
if t1_sum > t2_sum and text == "t1":
    print("t1 승리")
    print("맞췄습니다.")
elif t1_sum > t2_sum and text == "t2" :
    print("t1 승리")
    print("틀렸습니다.")
elif t1_sum < t2_sum and text == "t2" :
    print("t2 승리")
    print("맞췄습니다.")
elif t1_sum < t2_sum and text == "t1" :
    print("t2 승리")
    print("틀렸습니다.")
else : 
    print("무승부")

turtle.exitonclick()
turtle.bye()