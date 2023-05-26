#%% 객체지향 프로그래밍
class Rect : 
    count = 0 # 클래스 변수(공통)
    
    def __init__(self):
        self.width, self.height = 1,1 # 객체 인스턴스 변수(객체 고유)
        Rect.count +=1
        
if __name__ == '__main__':
    r1 = Rect()
    print('[1] r1(width, height,count) = ', r1.width, r1.height,r1.count)
    r2 = Rect()
    print('[2] r1(width, height,count) = ', r1.width, r1.height,r1.count)
    print('[2] r2(width, height,count) = ', r2.width, r2.height,r2.count)
    
#%% 
class Rect : 
    count = 0 # 클래스 변수
    
    def __init__(self,width,height):
        self.width, self.height = width,height # 인스턴스 변수
        Rect.count +=1  # 클래스 변수 값 수정
        
if __name__ == '__main__':
    r1 = Rect(3,5)
    r2 = Rect(4,7)
    print('[1] r1(width, height,count) = ', r1.width, r1.height,r1.count)
    print('[2] r2(width, height,count) = ', r2.width, r2.height,r2.count)
    
#%% 
# rect03. py : 사각형의 속성을 처리하는 Rect 클래스
# 속성 : count, rectid, width, hieght
# 메소드 : get_area(),get_peri()

class Rect : 
    count = 0 # 클래스 변수
    
    def __init__(self,width,height):
        self.width, self.height = width,height # 인스턴스 변수
        Rect.count +=1  # 클래스 변수 값 수정
        self.rectid = 'rectid_' + str(Rect.count) # 인스턴스 변수
        
    def get_area(self): # 사각형의 면적을 계산
        return (self.width * self.height)
    
    def get_peri(self): # 사각형의 둘레를 계산
        return 2 * (self.width + self.height)
    
if __name__ == '__main__':
    r1 = Rect(3,5)
    r2 = Rect(4,7)
    print('[1] r1(width, height,count) = ', r1.width, r1.height,r1.count)
    print('[2] r2(width, height,count) = ', r2.width, r2.height,r2.count)
    
    print(r1.get_area())
    print(r1.get_peri())
    print(r2.get_area())
    print(r2.get_peri())
    

    
    
    
    
    
    
    
    
    
    
    