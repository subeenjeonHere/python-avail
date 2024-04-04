# - 기준으로 분리
arr_str = input('input String : ').split('-')

# 12 정수 입력
arr_len = int(input('input number: '))

# 변수 = 리스트 생성(range(0,12,2) 0에서 arr_len-1까지 2씩 증가하는 숫자를 리스트 형식으로 저장
arr_val = list(range(0, arr_len, 2))
print(arr_val)

# 4 제거
arr_val.remove(4)

print(arr_val)
# arr_str 1 인덱스에 i 있는지 찾고, 없으므로 -1 반환
# arr_Val[2]는  6 이므로 5반환
print(arr_str[1].find('i') + arr_val[2])
