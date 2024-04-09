a = [3, 4, 10, 5, 1]

for i in range(0, 5):
    for j in range(i + 1, 5):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
for k in a:
    print(k, end=" ")

print("\n")
b = set(a)
print(a)
print(b)