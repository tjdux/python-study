# 절차 지향 
car_company_1 = "Ferrari"
car_detail_1 = [
    {"color": "white"},
    {"horsepower": 400},
    {"price": 8000}
]

car_company_2 = "BMW"
car_detail_2 = [
    {"color": "black"},
    {"horsepower": 270},
    {"price": 5000}
]

car_company_3 = "Audi"
car_detail_3 = [
    {"color": "silver"},
    {"horsepower": 300},
    {"price": 6000}
]

# 리스트 구조: 관리하기 어려움, 휴먼 에러 가능성
car_companies_list = ["Ferrari", "BMW", "Audi"]
car_details = [
    {"color": "white", "horsepower": 400, "price": 8000},
    {"color": "black", "horsepower": 270, "price": 5000},
    {"color": "silver", "horsepower": 300, "price": 6000}
]

del car_companies_list[1]
del car_details[1]

print(car_companies_list)
print(car_details)

# 딕셔너리 구조: 코드 반복, 키 중복 문제 (키는 유일해야 함), 키 조회 예외 처리 등
car_dicts = [
    {
        "car_company": "Ferrari",
        "car_detail": {"color": "white", "horsepower": 400, "price": 8000}
    },
    {
        "car_company": "BMW",
        "car_detail": {"color": "black", "horsepower": 270, "price": 5000},
    },
    {
        "car_company": "Audi", 
        "car_detail": {"color": "silver", "horsepower": 300, "price": 6000}
    }
]

del car_dicts[1]
car_dicts[0].pop("car_company")
print(car_dicts)

# 클래스 구조: 재사용성 증가, 코드 반복 최소화, 메소드 활용
class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    # ⭐ 사람이 읽기 좋은 문자열 표현을 정의하는 메소드
    # 사용자 입장의 출력
    def __str__(self):
        return f"str: {self._company} - {self._details}"
    
    # 객체 상태를 정확히 표현할 때 (개발자 입장)
    # __str__ 메소드가 없다면 __repr__ 메소드를 실행 
    def __repr__(self):
        return f"repr: {self._company} - {self._details}"
        
car1 = Car("Ferrari", {"color": "white", "horsepower": 400, "price": 8000})
print(car1) # str: Ferrari - {'color': 'white', 'horsepower': 400, 'price': 8000}
print(car1.__dict__) # 인스턴스의 namespace 
print(dir(car1)) # 인스턴스의 메타정보

# 리스트 선언
car2 = Car("BMW", {"color": "black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color": "silver", "horsepower": 300, "price": 6000})
cars_list = [car1, car2, car3]

print(cars_list)
##[repr: Ferrari - {'color': 'white', 'horsepower': 400, 'price': 8000}, repr: BMW - {'color': 'black', 'horsepower': 270, 'price': 5000}, repr: Audi - {'color': 'silver', 'horsepower': 300, 'price': 6000}]

for car in cars_list:
    print(car)