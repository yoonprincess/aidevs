numbers: list[int] = [1, 2, 3, 4, 5]

# 1. 출력
print("numbers: ", numbers)

for num in numbers:
    print("-", num)

# 2. 마지막 6을 추가
numbers.append(6)

print("------------------------------")
for num in numbers: 
    print("-", num)

# 3_1. 전체 합과 평균을 출력 (for문 사용)
tot = 0

for num in numbers:
    tot += num

print("------------------------------")
print("전체 합:", tot)
print("평균:", tot / len(numbers))

# 3_2. 전체 합과 평균을 출력 (for문 사용 X)
total_sum = sum(numbers)
average_num = total_sum / len(numbers)

print("------------------------------")
print(f"전체 합: {total_sum}")
print(f"평균: {average_num:.1f}")

# 3_2. 전체 합과 평균을 출력 (단, 짝수만)
tot_sum = 0
tot_count = 0

for num in numbers:
    if num % 2 == 0 :
        tot_sum += num
        tot_count += 1

print("------------------------------")
print(f"짝수의 합은 {tot_sum}이고, 평균은 {tot_sum / tot_count}입니다.")

# 수정: 제너레이터 표현식으로 짝수만 필터링한 리스트를 생성 (변수 최소화)
even_numbers = [x for x in numbers if x % 2 == 0]

# 수정: 리스트가 비어있지 않을 때만 평균 계산 (ZeroDivisionError 방지 삼항 연산자)
even_avg = sum(even_numbers) / len(even_numbers) if even_numbers else 0.0

print(f"짝수의 합: {sum(even_numbers)}")
print(f"짝수의 평균: {even_avg:.1f}")
