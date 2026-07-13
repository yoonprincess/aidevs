"""자료구조를 처리하는 함수 예제입니다.

함수는 숫자나 문자열뿐 아니라 list, dict 같은 자료구조도 받을 수 있습니다.

백엔드 개발에서는 사용자 목록, 메시지 목록, API 응답 데이터를
함수로 나누어 처리하는 일이 많습니다.
"""


# def calculate_average(scores):
#     total = 0

#     for score in scores:
#         total += score

#     return total / len(scores)

def calculate_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)


def print_user(user: dict[str, str | bool]) -> None:
    print("이름:", user["name"])
    print("역할:", user["role"])
    print("활성 상태:", user["active"])
    # 값을 리턴하지 않고, 출력만 하고 끝나는 함수


score_list = [90, 85, 77, 92]
average = calculate_average(score_list)
print("평균 점수:", average)

user = {
    "name": "Jean",
    "role": "admin",
    "active": True,
}

print_user(user)


def filter_passed_students(students: list[str, str | int]) -> list[str, str | int]:
    passed_students = []

    for student in students:
        if student["score"] >= 60:
            passed_students.append(student)

    return passed_students
    # return tuple(passed_students) # 불변성


students = [
    {"name": "Jean", "score": 95},
    {"name": "Mina", "score": 72},
    {"name": "Jun", "score": 58},
]

passed = filter_passed_students(students)
print("통과 학생:", passed)

print("===========================")

# 각 데이터의 평균보다 큰 수를 리턴하는 함수 구현
data1 = [1, 2, 3, 4, 5]
data2 = [6, 7, 8, 9, 10]

def get_over_avg(numbers: list[int]) -> list[int]:
    # avg_val = sum(numbers) / len(numbers)
    avg_val = calculate_average(numbers)    # 위에 정의한 함수 사용한 버전
    return [n for n in numbers if n > avg_val]

    # result = []
    # for n in numbers:
    #     if n > avg_val:
    #         result.append(n)
        
    # return result

print("[리스트 반환 결과]")
print("data1 평균보다 큰 수:", get_over_avg(data1))
print("data2 평균보다 큰 수:", get_over_avg(data2))

# 튜플로 반환하는 과정
def get_elements_above_average_tuple(numbers: list[int | float]) -> tuple[int | float, ...]:
    if not numbers:
        return ()

    avg = calculate_average(numbers)    # 위에 정의한 함수 사용한 버전
    
    # 수정: 대괄호[] 대신 소괄호()와 tuple() 생성을 조합하여 튜플로 반환
    # tuple(...) 내부의 제너레이터 표현식은 메모리를 아주 적게 씁니다.
    return tuple(num for num in numbers if num > avg)


result_tuple1 = get_elements_above_average_tuple(data1)
result_tuple2 = get_elements_above_average_tuple(data2)

print("[튜플 반환 결과]")
print(f"data1 평균보다 큰 수: {result_tuple1}\ndata2 평균보다 큰 수: {result_tuple2}")
