# 컴프리헨션(함축) 개념
numList = []
for num in range(1,6):
    numList.append(num)
    
print(numList)

#%%
numList = [num for num in range(1,6)]
numList

#%% 리스트 = [수식 for 항목 in range() if 조건식]
numList = [num*num for num in range(1,6)]
numList

#%% 
numList = [num * num for num in range(1,6) if num % 3 == 0]
print(numList)

#%% 딕셔너리의 개념
dic1 = {1:'a',2:'b',3:'c'}
print(dic1)

#%% 세트(가변형 데이터 형식)

mySet1 = {1,2,3,3,4}
print(mySet1)

#%% 세트(두 세트 사이의 교집합, 차집합, 대칭 차집합)

mySet1 = {1,2,3,4,5}
mySet2 = {4,5,6,7}

print(mySet1.intersection(mySet2))          # 교집합
print(mySet1.union(mySet2))                 # 합집합
print(mySet1.difference(mySet2))            # 차집합
print(mySet1.symmetric_difference(mySet2))  # 대칭 차집합

#%% 문자열(불변형 데이터 형식)

ss = "자료구조&알고리즘"
print(ss[0])
print(ss[1:4])
print(ss[4:])
print(len(ss))

#%% 튜플(불변형 데이터 형식)

tt1 = (10,20,30)
tt2 = 10,20,30
print(tt1)
print(tt2)

#%% 딕셔너리 반복문 활용
# keys() 키 반복, values() 값 반복

phone_book = {"홍길동" : "010-1234-5678"}

for k,v in phone_book.items():
    print(k+"의 전화번호는", v)

#%% 
import random

lottoNum = []

for i in range(1,7):
    while True :
        pickNum = random.randrange(1,46)
        if pickNum in lottoNum:
            continue
        else:
            lottoNum.append(pickNum)
            break

print("로또번호")
print(lottoNum)

#%%
poet = """죽는 날까지 하늘을 우러러
한 점 부끄럼이 없기를,
잎새에 이는 바람에도
나는 괴로워했다.
별을 노래하는 마음으로
모든 죽어가는 것을 사랑해야지
그리고 나한테 주어진 길을
걸어가야겠다.
"""

Dic = dict()

for ch in poet :
    if ch in Dic :
        Dic[ch] +=1 
    else:
        Dic[ch] = 1
del(Dic[' '])
del(Dic['\n'])

print(Dic)




























