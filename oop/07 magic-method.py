class Robot:

    num_of_instances = 0

    def __init__(self, name):
        self.name = name
        Robot.num_of_instances += 1

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}")

    def __str__(self):
        return f"{self.name} robot 🤖"

    # callable 하지 않은 인스턴스를 callable하게 변경
    def __call__(self):
        print("call")
        return f"{self.name} is called"


droid = Robot("R2-D2")
droid.say_hi()  # Greetings, my masters call me R2-D2
print(droid)  # R2-D2 robot 🤖

droid()  # call 👈 droid 인스턴스가 callable하게 됨
