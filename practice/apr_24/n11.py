x = input()
x = x.capitalize()
# 각 단어 첫 글자를 대문자로 변경하여 x에 저장
y = x.split()
# 공백 기준 y에 배열 형태 저장
print(y)
print(y[1])
print(y[0][::2], end='*')
# y의 0번지부터 2씩 증가하면서, 각 글자 출력, 종료문자 * 출력

print(y[1][3:6])
# y[1]에 저장된 문자열 3번째 부터 5번째 까지 출력
