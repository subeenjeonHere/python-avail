# 리스트 주소를 a, b에 저장하는 것
a = b = d = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

b[-1] = 5  # 마지막 요소를 5로 변경

d = a.copy()
d[-1] = 6

b = set(a)  # b에 a 리스트를 set -> set은 중복 제거되어 튜플 형태로
c = list(b)  # 튜플 b를 c에 리스트로 변환
print(a)
print(b)
print(c)
print(a is not b)
print(d)
