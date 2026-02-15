import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"시작 시간: {time.strftime('%X')}")

    # 두 개의 코루틴을 동시에 예약
    await asyncio.gather(
        say_after(2, "hello"),
        say_after(1, "world")
    )

    print(f"종료 시간: {time.strftime('%X')}")

asyncio.run(main())

# world
# hello
# 소요 시간 2초