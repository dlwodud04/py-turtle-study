#%% Random 예제1
import random

num_int = random.randint(1, 10)
print(num_int)

num_float = random.random()
print(num_float)

#%% Random 예제2
import random

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

for i in range(100):
    num_int = random.randint(1,5)
    if(num_int == 1):
       num1 = num1 + 1
    elif(num_int == 2):
       num2 = num2 + 1
    elif(num_int == 3):
       num3 = num3 + 1
    elif(num_int == 4):
       num4 = num4 + 1
    elif(num_int == 5):
       num5 = num5 + 1
            
print(num1,num2,num3,num4,num5)

#%% Random 실습1
import random

for i in range(30):
    num_int = random.randint(1,5)
    print(" "*(num_int-1),num_int)

#%% Random 과제 1

import random

select_user = input("가위, 바위, 보? : ")
select_com = random.choice(["가위","바위","보"])
print("COM : ",select_com)
if select_com == "가위" and select_user == "보" :
    print("win")
elif select_com == "가위" and select_user == "바위":
    print("lose")
elif select_com == "보" and select_user == "바위" :
    print("win")
elif select_com == "보" and select_user == "가위":
    print("lose")
elif select_com == "바위" and select_user == "가위" :
    print("win")
elif select_com == "바위" and select_user == "보":
    print("lose")
else :
    print("draw")
    
#%% Random 과제 2

import random

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
    
if t1_sum > t2_sum :
    print("t1 승리")
elif t2_sum > t1_sum :
    print("t2 승리")
else : 
    print("무승부")
    
#%% * Turtle Graphics
# 문자열 입력 예제 1
import turtle
text = turtle.textinput("제목", "내용")

print(text)

turtle.bye()

#%% 문자열 입력 예제 2

import turtle
score = int(turtle.textinput("점수", "1~100"))
grade = ""
if 90 <= score and score <=100:
    grade = "A"
elif 80 <= score and score <= 89:
    grade = "B"
elif 70 <= score and score <= 79:
    grade = "C"
else :
    grade = "D"

print("학점은",grade,"입니다.")

turtle.bye()

#%% 문자열 입력 실습

import turtle
while True:
    cho = turtle.textinput("선택", "t1 or t2")
    if cho == "t1" or cho == "t2":
            break
print(text)

#%% 문자열 출력 예제 1

import turtle

turtle.color("green")
turtle.write("거북이")

#%% 문자열 출력 예제 2

import turtle
turtle.shape("turtle")

font_a = ("굴림", 20)
font_b = ("굴림", 30)

turtle.write("거북이")
turtle.color("red")
turtle.fd(100)
turtle.write("고양이",font = font_a)
turtle.color("blue")
turtle.fd(100)
turtle.write("코끼리",font = font_b)

#%% 거북이 펜 제어 예제

import turtle
t = turtle.Turtle()
t.shape("turtle")

t.up()
t.goto(0,200)
t.down()
t.goto(200,-200)

#%% 거북이 추가

import turtle
t1 = turtle.Turtle()
t1.shape("turtle")

t2 = turtle.Turtle()
t2.shape("turtle")

t1.color("blue")
t1.up()
t1.goto(0,200)
t1.down()
t1.goto(200,200)

t2.color("red")
t2.up()
t2.goto(0,-200)
t2.down()
t2.goto(200,-200)

turtle.exitonclick()
turtle.bye()

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

























