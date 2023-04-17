import turtle
import random

t1 = turtle.Turtle()
t1.shape("turtle")

t2 = turtle.Turtle()
t2.shape("turtle")

t1.color("blue")
t1.up()
t1.goto(0,200)
t1.down()

t2.color("red")
t2.up()
t2.goto(0,-200)
t2.down()

t1_sum = 0
t1_sum = int(t1_sum) 
t2_sum = 0
t2_sum = int(t2_sum) 

while True :
    text = turtle.textinput("경주게임", "파랑 or 빨강")
    if text == "파랑" or text == "빨강" :
        break

while True :
    a = random.randint(1,10)
    t1.forward(a)
    t1_sum += a
    b = random.randint(1,10)
    t2.forward(b)
    t2_sum += b
    print("t1 : ",t1_sum ,"vs","t2 : ",t2_sum)
    if t1_sum >= 300 or t2_sum >= 300 :
        break
print("끝")

font_a = ("굴림", 50)

t3 = turtle.Turtle()

if t1_sum > t2_sum and text == "파랑":
    t1.write("승리",font = font_a)
    t3.write("예측 성공")
elif t1_sum > t2_sum and text == "빨강" :
    t1.write("승리",font = font_a)
    t3.write("예측 실패")
elif t1_sum < t2_sum and text == "빨강" :
    t2.write("승리",font = font_a)
    t3.write("예측 성공")
elif t1_sum < t2_sum and text == "파랑" :
    t2.write("승리",font = font_a)
    t3.write("예측 실패")

screen = turtle.Screen()
screen.exitonclick()

    
    