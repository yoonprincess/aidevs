# # Assignment 05 - Functions

students = [
    {"name": "Jean", "score": 95},
    {"name": "Mina", "score": 82},
    {"name": "Jun", "score": 58},
    {"name": "미도리아", "score": 95},
    {"name": "바쿠고", "score": 82},
    {"name": "쇼토", "score": 58},
]

"""
1. 학생들의 평균 점수를 출력

1) 학생들의 점수를 list로 받음
2) 평균을 반환하는 함수 구현

함수: calculate_average(students: list[str, int | str]) -> float:
결과: 학생들의 평균 점수를 출력
"""
def calculate_average(students_list: list[dict[str, str | int]]) -> float:
    # 1) 학생들의 점수를 list로 받음
    score_list = [int(student["score"]) for student in students]
    return sum(score_list) / len(students)

print("1. 학생들의 평균 점수:", calculate_average(students))
print("--------------------------------------------")

"""
2. 학생의 학점과 패스 여부를 출력

1) 학점 범위(A: 90 이상, B: 80 이상, C: 70 이상, D: 60 이상)
2) 패스 여부는 60점 이상
3) 학점과 패스 여부를 튜플에 담아 출력

함수: print_student_status(student: dict) -> tuple(str, bool):
"""
def print_student_status(student: dict[str, str | int]) -> tuple[str, bool]:
    score = int(student["score"])
    
    # 1) 학점 범위 계산
    # A: 90 이상, B: 80 이상, C: 70 이상, D: 60 이상
    #  그 외 F 임의로 추가
    if score >= 90:
        level = "A"
    elif score >= 80:
        level = "B"
    elif score >= 70:
        level = "C"
    elif score >= 60:
        level = "D"
    else:
        level = "F"

    if student["score"] >=60:
        status = True
    
    # 2) 패스 여부는 60점 이상
    status = score >= 60

    # 3) 학점과 패스 여부를 튜플에 담아 출력
    return (level, status)
    
# 출력
for s in students:
    print(f"{s['name']} 학생: {s['score']}점 {print_student_status(s)}")

print("--------------------------------------------")

"""
3. 모든 학생의 평균 점수보다 낮은 학생들을 출력

1) 모든 학생의 평균 점수 계산
2) 평균 점수보다 점수가 낮은 학생들을 튜플에 담아
3) 출력

함수: filter_passed_students(students: list) -> tuple:
"""
def filter_passed_students(students_list: list[dict[str, str | int]]) -> tuple[str, ...]:
    # 1) 모든 학생의 평균 점수 계산 (1번 함수 재사용하여 결합도 향상)
    avg_score = calculate_average(students_list)
    
    # 2) 평균 점수보다 점수가 낮은 학생들의 이름을 컴프리헨션으로 수집
    # 3) 최종적으로 tuple로 변환하여 반환 (불변성 보장)
    return tuple(s["name"] for s in students_list if int(s["score"]) < avg_score)

# 출력
low_students = filter_passed_students(students)
print("3. 전체 평균보다 낮은 학생 목록:")
# 가독성을 위해 앞서 배운 join 문법을 f-string 안에 적용해 출력
print(f"{', '.join(low_students)}")
