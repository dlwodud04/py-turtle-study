for i in range(5):
    print("방문을 환영합니다.")
#%%
for i in range(3):
    print("방문을 환영합니다.")
    print("만나서 반갑습니다.")
#%%
for i in range(0,4):
    print(i)
#%%
for i in range(4):
    print(i)
#%%
for i in range(2,4):
    print(i)
#%%
for i in range(1,4):
    print(i)
#%%
for i in range(1,4,1):
    print(i)
#%%
for i in range(1,4,2):
    print(i)
#%%
for i in range(10,0,-1):
    print(i)
#%%
for i in range(10,0,-1):
    print(i, end=" ")
#%%
for i in range(10,0,-1):
    print(i, end=",")
#%% range() 실습 코드
sum = 0
for i in range(1,101):
    sum+=i
print("1부터 100까지의 합은", sum, "입니다.")

#%%
import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range(5) :
    t.forward(100)
    t.right(144)

 
turtle.exitonclick()
turtle.bye()
#%%
response = "아니"
while response == "아니":
    response = input("엄마, 다 됐어? : ")
print(">>>잘 먹겠습니다.")
#%%
# while문 예제(로그인 프로그램)
password = ""
while password != "python":
    password = input("암호를 입력하시오 : ")
print(">>>로그인 성공")

#%%
# while문 과제
password = ""
while True :
    password = input("암호를 입력하시오 : ")
    if password =="blue":
        break 
    if password == "red" :
        break
print(">>>로그인 성공")

#%%
# 중첩반복문 예제1
for i in range(5):
    for j in range(10):
        print("*",end=" ")
    print("")

#%%
# 중첩반복문 예제 2
for i in range(1,6):
    for j in range(0,i):
        print("*",end=" ")
    print("")

#%%
# 무한반복
sign = True
light = "red"

while sign : 
    light = input("신호등의 색상은?: ")
    if light == "blue":
        sign = False
print("전진!!")

#%%
# break문
while True :
    light = input("신호등의 색상은? : ")
    if light == "blue":
        break
print("전진!!")

#%%
# continue문
for n in range(10):
    if n % 2 == 0:
        continue
    print(n)
    if n > 7:
        break
#%%
# 제어문 실습
answer = 5
while True:
   number = int(input("정답은 ? : "))
   if number < answer :
       print("정답은 더 높은 수")
   elif number > answer :
       print("정답은 더 낮은 수")
   else  :
       break
print("정답입니다.")

#%%
#과제1
age = int(input("나이 : "))
if age < 20: 
    price = 5000
else :
    price = 10000
money_total = 0

while True :
    money = int(input("돈 : "))
    money_total += money
    if money_total > price:
        print(">>>거스름돈 : ", money_total - price)
        print(">>>입장가능")
        break
        
    else:
        print(">>>추가필요금액 : ",price - money_total)
        print(">>>입장불가")
#%%
#과제2
import turtle
t = turtle.Turtle()
t.shape("turtle")

size1 = 200
size2 = 50
move_length = 10

t.dot(size1*2, "green")
t.dot(size2*2, "blue")

for i in range(0,300,10):
    print("move",i)
    t.undo()
    t.fd(move_length)
    t.dot(size2*2, "blue")
    d = t.distance(0,0)
    print("거북이 위치 : ", t.pos())
    print("원점까지 거리(거북이): ",d)
    if d==0 :
        print("충돌/동심원")
    elif size1 - size2 > d :
        print("충돌/내부존재")
    elif size1 - size2 == d :
        print("충돌/내접")
    elif size1 - size2 < d < size1+size2 :
        print("충돌/두접점")
    elif size1 + size2 == d :
        print("충돌/외접")
    elif size1 + size2 < d :
        print("비충돌")
    else :
        print("불가능")


turtle.exitonclick()
turtle.bye()





