num = int(input("당신의 나이를 입력하세요 :"))
if num <20 :
    print(">>>입장료 : 5000원")
if num >=20:
    print(">>>입장료 : 10000원")
    
#%%
num = int(input("양의 정수 입력:"))
if num > 0 :
    print(">>>양수입니다.")
if num == 0 :
    print(">>>양수도 음수도 아닙니다.")
if num < 0 :
    print(">>>음수입니다.")
#%%
num = int(input("양의 정수 :"))
if num %2 == 0 :
    print("짝수입니다.")
else : 
    print("홀수입니다.")
#%%
score = 95
if score > 90:
    print(">>>합격입니다.")
    print(">>>장학급대상자입니다.")
print(">>>수고하셨습니다.")
#%%
age = 5
height = 160
if (age >= 10):
    if(height >=110):
        print(">>>탑승가능합니다.")
    else : 
        print(">>>키제한으로 탑승불가능합니다.")
        print(">>>죄송합니다.")
else :
    print(">>>나이제한으로 탑승불가능합니다.")
    print(">>>죄송합니다.")
#%%
age = 15
height = 190
if (age >= 10 and height >= 100) :
    print(">>>탑승가능합니다.")
else : 
    print(">>>탑승불가능합니다.")
    print(">>>죄송합니다.")
    
#%%
# 실습 (입장료 계산기)
age = int(input("나이 :"))
money = int(input("돈 :"))

if age < 20 :
    if money >= 5000 :
        print(">>>입장가능")
        print(">>>거스름돈 : ",money-5000)
else : 
    print(">>>입장불가능")
    print("추가필요금액 : ",10000-money)
    
#%%
# 과제1
y = int(input("year:"))
if y%4==0 and y%100 == 0 and y%400==0 :
    print(y,"년은 윤년입니다.")
elif y%4==0 and y%100 == 0 :
    print(y,"년은 평년입니다.")
elif y%4 ==0 :
    print(y,"년은 윤년입니다.")
else :
    print(y,"년은 평년입니다.")
    
#%%
# 과제2
import turtle
t = turtle.Turtle()
t.shape("turtle")

x = 100
y = 50
size1 = 200
size2 = 50

print("원점에서의 거리(계산):",(x ** 2 + y ** 2) ** 0.5)

t.dot(size1*2,"green")
t.fd(x)
t.left(90)
t.fd(y)
t.dot(size2*2,"blue")

print("거북이 위치: ",t.pos())
print("원점까지의 거리(거북이): ", t.distance(0,0))

print("충돌 판단=>")
d = (x ** 2 + y ** 2) ** 0.5
if size1-size2 > d :
    print("충돌/내부위치")
elif size1 - size2 <= d <= size1 + size2:
    print("충돌/접점존재")
else:
    print("비충돌")

turtle.exitonclick()
turtle.bye()

