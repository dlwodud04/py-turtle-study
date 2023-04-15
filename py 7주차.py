#%% 인덱스(index)
slist = ["영어","수학","사회","과학"]
print(slist)

print(slist[0])
print(slist[1])
print(slist[2])

#%% 리스트 생성 및 추가(확장)인덱스(index)

slist = []
slist.append("영어")
print(slist)
slist.append("수학")
print(slist)
slist.append("사회")
print(slist)
slist.append("과학")
print(slist)

#%% 요소 접근 및 변경
slist = ["영어","수학","사회","과학"]
print(slist)

print(slist[2])
slist[2] = "윤리"

print(slist)
print(slist[4]) # 리스트의 크기를 벗어나는 인덱스는 사용 불가

#%% 리스트 + Random + 반복문 예제 1
import random

num_list = [0,0,0,0,0]

for i in range(100):
    num_int = random.randint(1, 5)
    num_list[num_int-1] = num_list[num_int-1]+1

print(num_list)

#%% 리스트 + Random + 반복문 실습 1
import random 

num_list = [0,0,0,0,0,0,0,0,0,0]

for i in range(100):
    num_int = random.randint(0, 9)
    num_list[num_int] = num_list[num_int]+1
    
print(num_list)

#%% 리스트 실습 1
import turtle

result = 0
input_list = []

while True :
    num = int(turtle.textinput("누적", "1~10, 0:종료"))
    input_list.append(num)
    if num == 0:
        break
    result += num
    print(result)
    
print(input_list)
turtle.bye()

#%% 함수 정의

def print_address():
    print("서울지 종로구 1번지")
    print("파이썬 빌딩 7층")
    print("홍길동")
    
print_address() # 함수 호출

#%% 인수 전달

def print_address(name):
    print("서울지 종로구 1번지")
    print("파이썬 빌딩 7층")
    print(name)
    
print_address("홍길동")
print_address("김코드")
print_address("나함수")

#%% 2개 이상의 인수 전달

def get_sum(start,end):
    sum = 0
    for i in range(start,end+1):
        sum+=i
    print("sum =", sum)

get_sum(1,10)
get_sum(1,20)

#%% 기본 매개변수(default parameter)

def get_sum(start,end = 10):
    sum = 0
    for i in range(start,end+1):
        sum+=i
    print("sum =", sum)

get_sum(1)
get_sum(1,20)
get_sum(5)
get_sum(5,10)

#%% return 사용

def rectangular(x,y):
    area = x*y
    return area

area_a = rectangular(3,4)
area_b = rectangular(5,6)
print(area_a)
print(area_b)

area_sum = rectangular(3,4) + rectangular(5,6)
print(area_sum)

#%% return 미사용

def rectangular(x,y):
    area = x * y
    return area

rectangular(3, 4) # 출력 없음

#%% 복수 개의 반환 값

def get_size():
    return 3,4

x,y = get_size()
print(x, ",", y)

#%% 반환 값이 없는 return 사용

def odd_even(num):
    if num % 2 == 0 :
        print("짝수")
        # return
    print("홀수")
    
odd_even(4)

#%% 함수 인수 예제

import turtle

t = turtle.Turtle()
t.shape("turtle")

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

square(100)
t.up()
t.goto(200,0)
t.down()
square(100)

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

#%% 전역 변수

def rectangular_area():
    result = x*y
    return result

x = 3
y = 4
area = rectangular_area()
print(area)

#%% 지역변수

def rectangular_area():
    result = x*y
    return result

x = 3
y = 4
rectangular_area()
print(result)

#%% 전역 변수 활용 1

result = 0
def rectangular_area():
    result = x*y
    
x = 3
y = 4
rectangular_area()
print(result)

#%% 전역 변수 활용 2

result = 0
def rectangular_area():
    global result
    result = x*y
    
x = 3
y = 4
rectangular_area()
print(result)

#%% 위치 인수 (positional argument) = 인수 위치 구분
#   키워드 인수 (keyword argument) = 인수 앞 키워드 구분

def calc(x,y) :
    return x - y

print(calc(10,20))
print(calc(20,10))

print(calc(x=10,y=20))
print(calc(y=20,x=10))

#%% 키워드 인수 활용

def calc(x,y,z):
    return x + y + z

print(calc(10,y=20,z=30))

print(clac(x=10,20,30))
# -반드시 위치 인수가 키워드 인수보다 앞에 나와야 함

#%% 키워드 인수 전달 문제

def func1(x,y,z):
    print(x*y+z)
    return x * y + z

func1(1,3,5)        # 8
func1(y=7,z=5,x=2)   # 19
func1(z=2,x=4,y=5)  # 22
func1(5,z=10,y=2)   # 20
func1(z=10,5,x=2)   # 에러(위치인수가 뒤에 존재)
func1(5,x=2,z=20)   # 에러(x 중복 할당)

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

































































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    