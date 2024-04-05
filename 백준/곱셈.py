from sys import getsizeof

a = int(input())
b = int(input())

# 숫자 리스트로 변환
list1 = list(map(int, str(a)))
list2 = list(map(int, str(b)))

res = [3, 3, 3]
res2 = []
a = 0
for i in res:
    line = []
    for j in range(i):
        a += 1
        line.append(a)
    res2.append(line)

# 이중 For문 역순 순회
# len(list2)-1 list 마지막 요소 인덱스
# -1 종료 조건
# -1 각 반복마다 인덱스 1씩 감소하며 역순 이동하도록
for j in range(len(list2) - 1, -1, -1):
    result = list()
    length = len(result)
    for i in range(len(list1) - 1, -1, -1):
        x1 = list1[i]
        x2 = list2[j]
        if x1 * x2 > 9:
            div = (int(x1 * x2) / 10)
            mod = (int(x1 * x2) % 10)
