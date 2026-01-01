"""
# self: 인스턴스 객체
# ⭐⭐ 클래스 안에 있는 self의 주소와 만들어진 인스턴스의 주소는 동일
# self는 인스턴스 그 자체
"""


class SelfTest:
    # 클래스 변수
    name = "tjduxxx"

    def __init__(self, x):
        self.x = x

    @classmethod
    def func1(cls):
        print(f"cls: {cls} (func1)")

    def func2(self):
        print(f"self: {self}, class안의 self 주소: {id(self)}")


test_obj = SelfTest(17)

# ⭐ self의 주소와 만들어진 인스턴스의 주소는 동일
test_obj.func2()  # self: <__main__.SelfTest object at 0x00000190C08F8440>, class안의 self 주소: 1721217549376
SelfTest.func1()  # cls: <class '__main__.SelfTest'> (func1)
print(f"인스턴스의 주소: {id(test_obj)}")  # 인스턴스의 주소: 1721217549376

# 인스턴스에서 클래스 메소드 실행, 클래스 변수 접근
test_obj.func1()  # cls: <class '__main__.SelfTest'> (func1)
print(test_obj.name)  # tjduxxx

# 클래스에서 인스턴스 메소드 실행, 인스턴스 변수 접근
# SelfTest.func2() ⚠️ TypeError: SelfTest.func2() missing 1 required positional argument: 'self'
# print(SelfTest.x) ⚠️ AttributeError: type object 'SelfTest' has no attribute 'x'
