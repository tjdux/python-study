"""
1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.
2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.
3. 메서드 오버라이딩
4. super()
5. ⭐⭐ Python의 모든 클래스는 object 클래스를 상속한다: 모든 것은 객체다!
6. MyClass.mro() --> 상속 관계를 보여준다.
"""


class Robot:

    num_of_instances = 0

    def __init__(self, name):
        self.name = name
        Robot.num_of_instances += 1

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}")

    def cal_add(self, a, b):
        return a + b

    def __str__(self):
        return f"{self.name} robot 🤖"

    @classmethod
    def how_many(cls):
        return f"We have {cls.num_of_instances} robots."

    @staticmethod
    def get_num_of_instances():
        print(f"{Robot.num_of_instances} instances")


class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    # method overriding
    def say_hi(self):
        print("안녕하세요!!")

    def cal_mul(self, a, b):
        return a * b

    def calculate(self, a, b):
        return self.cal_mul(a, b) + self.cal_add(a, b)

    def overridden_method(self):
        super().say_hi()

    @classmethod
    def hello_apple(cls):
        print(f"{cls}")

    @classmethod  # classmethod overriding
    def how_many(cls):
        return f"We have {cls.num_of_instances} robots."


siri = Siri("siri", 51)
print(siri)  # siri robot 🤖
siri.say_hi()  # Greetings, my masters call me siri
print(siri.cal_mul(3, 5))  # 15
Siri.hello_apple()  # <class '__main__.Siri'>
Siri.get_num_of_instances()  # 1 instances
siri.say_hi()  # 안녕하세요!!
print(Siri.how_many())  # We have 1 robots.

siri.overridden_method()  # Greetings, my masters call me siri

# mro(): 클래스의 상속관계를 보여줌
print(
    Siri.mro()
)  # [<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>]
print(Robot.mro())  # [<class '__main__.Robot'>, <class 'object'>]

print(object)  # <class 'object'>

print(int.mro())  # [<class 'int'>, <class 'object'>]
print(bool.mro())  # [<class 'bool'>, <class 'int'>, <class 'object'>]


# 다중 상속 (안티 패턴)
class A:
    pass


class B:
    pass


class C:
    pass


class D(A, B, C):
    pass


print(
    D.mro()
)  # [<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
