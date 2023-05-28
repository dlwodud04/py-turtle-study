# 상속의 예
class Rect : 
    def __init__(self,width,height=-1):
        if height < 0:                   # 정사각형인 경우
            height = width
        self.width, self.height = width,height # 인스턴스 변수
        
    def __repr__(self):
        return 'Rect(w='+'%.2f'%self.width+', h='+'%2.f'%self.height+')'
    
    def get_area(self):                 # 직사각형의 면적을 계산
        return (self.width * self.height)
    
    def get_peri(self):                 # 직사각형의 둘레를 계산
        return 2 * (self.width + self.height)
    
    def isSquare(self):
        return (self.width == self.height)
    
class Square(Rect):
    
    def __repr__(self):                 # 메소드 오버라이딩
        return 'Square(width='+'%.2f'%self.width+')'
    
    def isSqure(self):                  # 메소드 오버라이딩
        return True
    
if __name__ == '__main__':
    r1 = Rect(3,5)
    print(r1, ', 면적 : ', r1.get_area())
    r2 = Square(7)
    print(r2, ', 면적 : ', r2.get_area())
    r3 = Rect(6,6)
    print(r3, ', 면적 : ', r3.get_area())
    print(r1.isSquare(), r2.isSquare(), r3.isSquare())