res = [3, 3, 3]
res2 = []
a = 0

# 리스트 123, 456,789 채우기
for i in res:
    line = list()
    for h in range(i):
        a += 1
        line.append(a)
    res2.append(line)
print(res2)
