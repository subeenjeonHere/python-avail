temp = 0
minidx = 0
a = [4, 2, 3, 5, 1]

for i in range(0, 4):
    minidx = i

    for j in range(i + 1, 5):
        if a[j] < a[minidx]:
            minidx = j

    temp = a[minidx]
    a[minidx] = a[i]
    a[i] = temp

print(a)
