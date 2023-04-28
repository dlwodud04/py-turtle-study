# 피보나치 수열 문제
# 피보나치 수열 만들기
fibo_list = [1,1]

for n in range(2,12):
    fibo_new = fibo_list[n-1] + fibo_list[n-2]
    fibo_list.append(fibo_new)
    
print(fibo_list)

#%% 리스트 인덱스
List = ['A','B','C','D','E','F']

print(List[0])  # A
print(List[3])  # D
print(List[-1]) # F, 음수
print(List[-5]) # B, 음

#%% 슬라이싱 실습
List = ['A','B','C','D','E','F']

List2 = List[::2]
print(List2)
List3 = List2[::-1]
print(List3)

List2 = List[::-2]
print(List2)
List3 = List2[1::]
print(List3)

#%% 리스트 정렬 실습
List = [5,4,2,7,0,-5]

List.sort()
print(List)
List.sort(reverse = True)
print(List)

#%% 리스트 + Turtle
import turtle

aList = []

for i in range(4) :
    a1 = turtle.Turtle()
    a1.shape("turtle")
    aList.append(a1)
    
for i in range(4):
    aList[i].left(i * 90)
    
for a2 in aList : 
    a2.fd(100)
    
turtle.done()

#%% 리스트 + Turtle

import turtle

aList = []

for i in range(4):
    a1 = turtle.Turtle()
    a1.shape("turtle")
    aList.append(a1)
    
for i in range(4):
    aList[i].left(i * 90)
    aList[i].fd(i*50)

turtle.extionclick()
turtle.bye()

#%% 리스트 +  Turtle

import turtle

aList = []

for i in range(6):
    a1 = turtle.Turtle()
    a1.shape("turtle")
    aList.append(a1)
    
for i in range(6):
    aList[i].left(i*60)
    
for dist in [50,100,50,70,100,50,60,90]:
    for a in aList:
        a.fd(dist)
        a.left(30)
