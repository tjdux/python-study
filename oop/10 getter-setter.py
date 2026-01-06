"""
[property]
인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을 때
인스턴스 변수 값에 대한 유효성 검사 및 수정
"""


class Robot:
    __num_of_instances = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Robot.__num_of_instances += 1

    @property
    def name(self):
        return f"hi {self.__name}"

    # getter
    @property
    def age(self):
        return self.__age

    # setter
    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise TypeError("invalid age")
        self.__age = new_age


droid = Robot("R2-D2", 2)
print(droid.age)  # 2

droid.age = 7
print(droid.age)  # 7

droid.age += 1
print(droid.age)  # 8

# droid.age = -999  # TypeError: invalid age

print(droid.name)  # hi R2-D2
