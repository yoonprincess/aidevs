student: dict[str, str | int] = {
    "name": "Jean",
    "ko": 95,
    "en" : 85,
    "math" : 90,
    "science": 80,
}

# student의 점수 합과 평균을 구하고 "sum", "avg"를 추가하고 출력하기
score_sum = 0
score_count = 0

for key, value in student.items():
    if key != "name":
        score_sum += value
        score_count += 1

student["sum"] = score_sum
student["avg"] = score_sum / score_count

print("student: ", student)
