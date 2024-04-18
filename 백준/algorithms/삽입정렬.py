li = [2, 5, 6, 7, 3, 1]

for i in range(0, len(li)):
    for j in range(i + 1, len(li)):
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]

print(li)
