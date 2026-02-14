## 바운드

### I/O 바운드

- Input/Output
- 실행 속도가 I/O에 의해 제한됨을 의미
- 사용자가 키보드로 숫자를 입력하는 경우 뿐만 아니라, 컴퓨터끼리 통신을 할 때도 I/O 바운드 발생

```python
def io_bount_func():
  print("값을 입력해주세요.")
  input_value = input()
  return int(input_value) + 100

if __name__ == "__main__":
  result = io_bound_func()
  print(result)
```

```python
import requests

def io_bound_func():
  result = requests.get("https://google.com")
  return result

if __name__ == "__main__":
  for i in range(10):
    result = io_bound_func()
  print(result)
```

### CPU 바운드

- 프로그램이 실행될 때 실행 속도가 CPU 속도에 의해 제한됨을 의미
- 정말 복잡한 수학 수식을 계산하는 경우

```python
def cpu_bound_func(number: int):
  total = 1
  arrange = range(1, number+1)
  for i in arrange:
    for j in arrange:
      for k in arrange:
        total *= i * j * k

  return total


if __name__ == "__main__":
  result = cpu_bound_func(100)
  print(result)
```

<br/>

## 블로킹

- 바운드에 의해 코드가 멈추게 되는 현상이 일어나는 것
