#%%
import turtle

aList = []

for i in range(4):
    a1 = turtle.Turtle()
    a1.shape("turtle")
    aList.append(a1)
    
for i in range(4):
    aList[i].left(i*90)
    
    for j in range(4):
        aList[i].fd((i+1)*50)
        aList[i].left(90)