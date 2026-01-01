"""
# namespace: 개체를 구분할 수 있는 범위
# __dict__: 네임스페이스 확인
# dir(): 네임스페이스의 key 값 확인
# __doc__: class의 주석 확인
# __class__: 어떤 클래스로 만들어진 인스턴스인지 확인
"""


class Robot:
    """
    [Robot Class]
    Author: Park
    Role: ...
    """

    num_of_instances = 0

    def __init__(self, name, code):
        self.name = name
        self.code = code
        Robot.num_of_instances += 1

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}")

    def cal_add(self, a, b):
        return a + b

    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.num_of_instances -= 1
        if Robot.num_of_instances == 0:
            print(f"{self.name} was the last one.")

    @classmethod
    def how_many(cls):
        print(f"We have {cls.num_of_instances} robots.")


siri = Robot("siri", 5126823)
jarvis = Robot("jarvis", 85354687)
bixby = Robot("bixby", 18632)

print(Robot.__dict__)

print(siri.__dict__)  # {'name': 'siri', 'code': 5126823}

print(jarvis.__dict__)  # {'name': 'jarvis', 'code': 85354687}

# ✏️ 메모리 효율을 위해 인스턴스 네임스페이스가 아닌 클래스 네임스페이스에 인스턴스 메소드가 존재

print(siri.cal_add(2, 3))  # 5

# ✏️ 파이썬 내부적으로 인스턴스의 네임스페이스에 메소드 (또는 변수)가 없다면 그 인스턴스가 만들어진 클래스의 네임스페이스에서 메소드 (또는 변수)를 찾음

# 인스턴스에서 클래스 변수, 클래스 메소드 접근 가능
print(siri.num_of_instances)  # 3
siri.how_many()  # We have 3 robots.

# Robot.say_hi() ⚠️ TypeError: Robot.say_hi() missing 1 required positional argument: 'self'
Robot.say_hi(siri)  # Greetings, my masters call me siri
siri.say_hi()  # Greetings, my masters call me siri

# dir()
print(dir(siri))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__',
# '__subclasshook__', '__weakref__', 'cal_add', 'code', 'die', 'how_many', 'name', 'num_of_instances', 'say_hi']
print(dir(Robot))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__',
# '__subclasshook__', '__weakref__', 'cal_add', 'die', 'how_many', 'num_of_instances', 'say_hi']

# __doc__
print(Robot.__doc__)
# [Robot Class]
# Author: Park
# Role: ...

# __class__
print(siri.__class__)  # <class '__main__.Robot'>
