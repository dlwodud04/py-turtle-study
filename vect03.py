#%% 특수 메소드
class Vect2 : 
    ndim = 2    # 클래스 변수
    
    def __init__(self,x,y): # 생성자
        self.x, self.y = x,y
        
if __name__ == '__main__' :
    v1 = Vect2(3,5)
    print('v1 = ', v1)
    print('v1(x,y) = ', v1.x, v1.y)

#%% __repr__() 메소드

class Vect2 : 
    ndim = 2  # 클래스 변수
    
    def __init__(self,x,y):  # 생성자
        self.x, self.y = x,y
    
    def __repr__(self):   # 정보 표기 메소드
        return 'Vector['+'%.2f'%self.x + ',' + '%.2f'%self.y +']'
    
if __name__ == '__main__' :
    v1 = Vect2(3,5)
    print('v1 = ', v1)
    print('v1(x,y) = ', v1.x, v1.y)
#%% 연산자 오버로딩

class Vect2 : 
    ndim = 2  # 클래스 변수
    
    def __init__(self,x,y):  # 생성자
        self.x, self.y = x,y
    
    def __repr__(self):   # 정보 표기 메소드
        return 'Vector['+'%.2f'%self.x + ',' + '%.2f'%self.y +']'
    
    def __add__(self,other): # 벡터 덧셈을 계산
        new = Vect2(0,0)
        new.x = self.x + other.x
        new.y = self.y + other.y
        return new
    
if __name__ == '__main__' :
    v1 = Vect2(3,5)
    v2 = Vect2(7,4)
    v3 = v1 + v2
    print(v1,v2,v3)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    