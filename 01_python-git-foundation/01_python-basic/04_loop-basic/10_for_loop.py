# 1~5 합

data_numbers : list = [1, 2, 3, 4, 5]
print(type(data_numbers), data_numbers) # <class 'list'> [1, 2, 3, 4, 5]

tot_num : int = 0

for num in data_numbers:
    tot_num += num

print("1부터 5까지의 합:", tot_num)
print("1부터 5까지의 평균:", tot_num / len(data_numbers))