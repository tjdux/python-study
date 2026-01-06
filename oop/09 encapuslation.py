"""
public vs. private
- private
클래스 내부에서만 직접 접근 가능
상속받은 클래스에서도 접근 불가
변수, 메서드 앞 __
- protected
파이썬에서는 지원하지 않으므로 변수 앞에 _를 붙이면 protected로 간주
"""


class Robot:
    num_of_instances = 0

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private
        Robot.num_of_instances += 1


class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
        # print(self.__age) # AttributeError: 'Siri' object has no attribute '_Siri__age'
        self.__age = 999
        print(self.__age)  # 99


robot1 = Robot("aaa", 8)
# print(robot1.__age)  # ⚠️AttributeError: 'Robot' object has no attribute '__age'

siri = Siri("iphone", 9)
# print(siri.__age) # ⚠️ AttributeError: 'Siri' object has no attribute '__age'
