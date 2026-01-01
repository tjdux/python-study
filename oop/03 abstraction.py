# 추상화: 불필요한 정보는 숨기고 중요한 (필요한) 정보만을 표현함으로써
# 공통의 속성, 값이나 행위를 하나로 묶어 이름을 붙이는 것
class Robot:

    # 클래스 변수
    num_of_instances = 0

    # 생성자 함수
    def __init__(self, name, code):
        self.name = name  # 인스턴스 변수
        self.code = code
        Robot.num_of_instances += 1

    # 인스턴스 메소드
    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}")

    def cal_add(self, a, b):
        return a + b

    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.num_of_instances -= 1
        if Robot.num_of_instances == 0:
            print(f"{self.name} was the last one.")

    # 클래스 메소드
    @classmethod
    def how_many(cls):
        print(f"We have {cls.num_of_instances} robots.")


siri = Robot("siri", 5126823)
jarvis = Robot("jarvis", 85354687)
bixby = Robot("bixby", 18632)

siri.say_hi()  # Greetings, my masters call me siri
print(siri.cal_add(2, 3))  # 5

print(Robot.num_of_instances)  # 3
Robot.how_many()  # We have 3 robotss.
siri.how_many()  # We have 3 robots.
