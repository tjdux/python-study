class Cal:
    # 생성자 함수: 메모리에 올라오는 순간 즉시 실행
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


cal1 = Cal(1, 2)
print(cal1.a)  # 1
print(cal1.b)  # 2
print(cal1.add())  # 3
print(cal1.sub())  # -1
print(cal1.mul())  # 2
print(cal1.div())  # 0.5

cal2 = Cal(3, 4)
print(cal2.a)  # 3
print(cal2.b)  # 4

cal2.a = 5
print(cal2.a)  # 5
print(cal2.add())  ## 9
