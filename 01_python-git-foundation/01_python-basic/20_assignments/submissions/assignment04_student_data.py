# # Assignment 04 - Data Structures

# 자료구조를 사용해 학생 관리 데이터를 만듭니다.

# ## 과제 파일

# ```text
# submissions/assignment04_student_data.py
# ```

# ## 요구사항

# ```text
# 1. 학생 3명 이상의 정보를 list 안의 dict로 저장합니다.
# 2. 각 학생 dict에는 name, score, tags를 포함합니다.
# 3. tags는 list로 저장합니다.
# 4. 모든 학생의 이름과 점수를 출력합니다.
# 5. 평균 점수를 계산합니다.
# 6. 60점 이상인 학생만 출력합니다.
# 7. 전체 tags를 set으로 변환해 중복을 제거합니다.
# ```

# ## 데이터 예시

# ```python
# students = [
#     {"name": "Jean", "score": 95, "tags": ["python", "backend"]},
#     {"name": "Mina", "score": 82, "tags": ["python", "ui"]},
# ]
# ```

# ## 추가 과제

# ```text
# 가장 높은 점수를 받은 학생 이름을 출력합니다.
# ```

# ## 확인 기준

# ```text
# list, dict, set을 모두 사용했는가?
# 반복문으로 자료구조를 처리했는가?
# 중복 태그가 제거되었는가?
# ```

# 1. 학생 3명 이상의 정보를 list 안의 dict로 저장합니다.
# 2. 각 학생 dict에는 name, score, tags를 포함합니다.
students: list[dict[str, str | int | list[str]]] = [
    {"name": "미도리아", "score": 70, "tags": ["python", "backend"]},
    {"name": "바쿠고", "score": 60, "tags": ["python", "ui"]},
    {"name": "쇼토", "score": 50, "tags": ["python", "frontend"]},
]

# 3. tags는 list로 저장합니다.
all_tags_list: list[str] = []

for student in students:
    all_tags_list.extend(student["tags"])

print(f"중복 제거 전 (list): {all_tags_list}") 
print("-----------------------------------")

# 4. 모든 학생의 이름과 점수를 출력합니다.
print("[모든 학생 정보]")

for s in students:
    print(f"이름: {s['name']} / 점수: {s['score']}")

print("-----------------------------------")

# 5. 평균 점수를 계산합니다.
print("평균 점수:", sum([s['score'] for s in students]) / len(students))
print("-----------------------------------")

# scores = [student["score"] for student in students if isinstance(student["score"], int)]
# average_score = sum(scores) / len(scores) if scores else 0.0
# print(f"전체 학생 평균 점수: {average_score:.1f}점")
# print("-----------------------------------")

# 6. 60점 이상인 학생만 출력합니다.
print('[점수가 60점 이상인 학생 목록]')

for s in students:
    if s['score'] >= 60 :
    # if isinstance(student["score"], int) and student["score"] >= 60:
        print(f"- {s['name']} ({s['score']}점) | 태그: {', '.join(s['tags'])}")

print("-----------------------------------")

# 7. 전체 tags를 set으로 변환해 중복을 제거합니다.
# 7_1
all_tags: set[str] = set()

for s in students:
    all_tags.update(s['tags'])

print(f"중복 제거된 전체 태그 목록(set): {all_tags}")

# 7_2
unique_tags = {tag for student in students for tag in student["tags"]}
print(f"중복 제거된 전체 태그 목록(set): {unique_tags}")

# 7_3
unique_tags: set[str] = set(all_tags_list)  # 3번에 만든 list
print(f"중복 제거 후 (set): {unique_tags}")
