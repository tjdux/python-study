"""
다형성 (polymorphism)
- 여러 형태를 가질 수 있도록 한다. 즉, 객체를 부품화할 수 있도록 한다.
- 같은 형태의 코드가 다른 동작을 하도록 하는 것
"""


class Robot:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Siri(Robot):
    def say_apple(self):
        print("🍎")


class SiriKor(Robot):
    def say_apple(self):
        print("사과")


class Bixbt(Robot):
    def say_samsung(self):
        print("samsung")
