# decorator
def copyright(func):
    def new_func():
        print("@copyright")
        func()

    return new_func


@copyright
def smile():
    print("😀")


@copyright
def angry():
    print("😡")


@copyright
def love():
    print("🥰")


@copyright
def curios():
    print("🧐")


smile()
# @copyright
# 😀
