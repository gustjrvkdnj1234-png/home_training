#class
# 실제 객체를 만들기 위한 설계도
# 실제 객체 (데이터, 동작(기능))

class Person:
    def __init__(self, age, height, job, money, hobby):
        self.age = age
        self.height = height
        self.job = job
        self.money = money
        self.hobby = hobby

    def introduce(self):
        print(f'저는 {self.age}살이고 직업은 {self.job}입니다.')

# 객체 인스턴스
금기륜 = Person(None, 177.1, '강사', '두쫀쿠2개', '게임')

금기륜.introduce()