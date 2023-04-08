#%% (과제1) 가위,바위,보 게임

import random

select_user = input("가위, 바위, 보? : ")
select_com = random.choice(["가위","바위","보"])
print("COM : ",select_com)
if select_user == "가위" and select_com == "보" :
    print("win")
elif select_user == "가위" and select_com == "바위":
    print("lose")
elif select_user == "보" and select_com == "바위" :
    print("win")
elif select_user == "보" and select_com == "가위":
    print("lose")
elif select_user == "바위" and select_com == "가위" :
    print("win")
elif select_user == "바위" and select_com == "보":
    print("lose")
else :
    print("draw")
    
#%% (과제2) 주사위 게임 만들기

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
    
