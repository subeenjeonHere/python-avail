li = [10, 15, 255]
str = ''
for i in range(len(li)):
    str += hex(li[i])

print(str)

n = int(input())
li2 = list()

for i in range(1, n + 1):
    if i % 2 == 0:
        li2.append(i)
    else:
        li2.append(hex(i))
print(li2)
