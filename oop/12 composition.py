"""
composition
- 다른 클래스의 일부 메서드를 사용하고 싶지만, 상속은 하고 싶지 않을 경우
1. 부모 클래스가 변하면 자식 클래스는 계속 수정되어야 한다.
2. 부모 클래스의 메서드를 오버라이딩하는 경우 내부 구현 방식의 얕은 이해로 오류가 생길 가능성 증가
"""


class Calc:
    def __init__(self) -> None:
        pass

    def cal_add(self, a, b):
        return a + b + 1


class Calc1:
    def __init__(self) -> None:
        self.Calc = Calc()

    def cal_add(self, a, b):
        return self.Calc.cal_add(a, b)
