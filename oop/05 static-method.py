class Robot:

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

    # static method
    @staticmethod
    def Is_this_robot_class():
        print(True)


print(Robot.Is_this_robot_class())  # True
