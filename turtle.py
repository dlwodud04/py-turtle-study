x = 100
print(x)

# %%
score = 10
score = score + 1
print(score)

# %%
import turtle
t = turtle.Turtle()
t.shape("turtle")

# %%
size = 100
angle = 120

t.color("blue")
t.forward(size)
t.left(angle)

# %%
# turtle.done()
turtle.bye()

# %%
x = input("첫 번째 정수를 입력하시오 : ")
y = input("두 번째 정수를 입력하시오 : ")
print(x, "+", y , "=", x+y)

# %%
x_str = input("첫 번째 정수를 입력하시오 : ")
y_str = input("두 번째 정수를 입력하시오 : ")
x = int(x_str)
y = int(y_str)
print(x, "+", y , "=", x+y)

# %%
size_str = input("처음 이동할 거리를 입력하세요 : ")
size = int(size_str)
t.color("blue")
t.forward(size)

size_str = input("다음 이동할 거리를 입력하세요 : ")
size = int(size_str)
t.color("red")
t.forward(size)

size_str = input("마지막으로 이동할 거리를 입력하세요 : ")
size = int(size_str)
t.color("green")
t.forward(size)

# %%
size_str = input("집의 크기를 입력하시오 : ")
size = int(size_str)

roof = input("지붕의 색을 입력하시오 : ")
wall = input("벽의 색을 입력하시오 : ")
t.color(roof)
t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
t.forward(size)
t.left(30)
t.color(wall)
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)

#%%
s = int(input("전체 초를 입력하시오 : "))
m = s // 60
r = s % 60
print(m, "분", r , "초")

# %%
x = y = 100
print(x)
print(y)
# %%
x = 1000
print("초기값 x = ",x)
x +=2
print("x += 2 후의 x = ", x)
x -=2
print("x -= 2 후의 x = ", x)
x *=4
print("x *= 4 후의 x = ", x)
x +=5
print("x += 5 후의 x = ", x)

# %%
x = int(input("첫 번째 수 : "))
y = int(input("두 번째 수 : "))
z = int(input("세 번째 수 : "))


avg = (x + y + z) / 3
avg = int(avg)

print("평균=", avg)

# %%
a = int(input("투입한 돈 : "))
b = int(input("물건의 가격 : "))
c = a - b
d = c/500
e = c % 500
f = e/100
print("거스름돈 : ", c)
print("500원 동전의 개수 : ", int(d))
print("100원 동전의 개수 : ", int(f))
# %%
import turtle
t = turtle.Turtle()
t.shape("turtle")

x = int(input("가로 : "))
y = int(input("세로 : "))
angle = 90
print("원점에서의 거리(계산):",(x ** 2 + y ** 2) ** 0.5)
t.color("blue")
t.forward(x)
t.left(angle)
t.forward(y)
print("거북이 위치: ",t.pos())
print("원점까지 거리(거북이) : ",(t.xcor() ** 2 + t.ycor() ** 2) ** 0.5 )
turtle.exitonclick()
turtle.bye()





























