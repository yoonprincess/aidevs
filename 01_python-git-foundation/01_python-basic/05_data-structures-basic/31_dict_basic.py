students: dict[str, str | int] = [
    {
        "name": "미도리아",
        "score": 95,
    },
    {
        "name": "바쿠고",
        "score": 99,
    },
    {
        "name": "쇼토",
        "score": 96,
    },
]

print("student: ", students)

# for 반복문을 사용하여 학생들의 이름과 점수를 출력
for s in students:
    print(f"학생 이름: {s['name']} / 점수: {s['score']}")

# 학생들 성적의 합과 평균 출력
score_sum = 0

for s in students:
    score_sum += s['score']

print(f"학생들 성적의 합: {score_sum} / 평균: {score_sum / len(students)}")

print("-" * 30)
# 수정: 별도의 합산용 루프 변수 없이 리스트 컴프리헨션과 sum()을 활용해 일괄 처리
scores = [student["score"] for student in students if isinstance(student["score"], int)]

total_sum = sum(scores)
average = total_sum / len(scores) if scores else 0.0

print(f"성적 합계: {total_sum}")
print(f"성적 평균: {average:.1f}")