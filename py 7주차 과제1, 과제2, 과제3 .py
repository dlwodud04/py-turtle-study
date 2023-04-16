#%% 과제1 (함수 인수 실습)

import turtle

t = turtle.Turtle()
t.shape("turtle")

def square_move(x,y,length):
    t.up()
    t.goto(x,y)
    t.down()
    for i in range(4):
        t.forward(length)
        t.left(90)

square_move(0, 100, 50)
square_move(100, 50, 100)
square_move(-100, -100, 150)

#%% 과제2 (BMI 계산기)

import turtle

def bmi(weight,height):
    height = height / 100
    result = weight / (height * height)
    return result

while True : 
    weight = float(turtle.textinput("BMI","몸무게"))
    height = float(turtle.textinput("BMI","키"))
    
    if height == 0:
        break

    bmi_value = bmi(weight,height)
    print(bmi_value)

turtle.bye()

#%% 과제3 (환전 계산기)

import turtle

def change(mon,cont) :
    if cont == "미국" :
        TBR = 1117.5
    elif cont == "일본" : 
        TBR = 1022.56
    elif cont == "유럽 연합" : 
        TBR = 1343.24
    else :
        print("잘못된 국가 입력입니다.")
        print(0)
    result = mon / TBR
    return result

while True:
    money = float(turtle.textinput("환전계산기", "KRW"))
    contry = turtle.textinput("환전계산기", "국가")
    
    if money == 0:
        break
    
    change_value = change(money,contry)
    print(change_value)

turtle.bye()