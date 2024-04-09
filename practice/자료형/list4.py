lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(lst[2])  # [6,7,8,9]
print(lst[1][1])  # [5] xxxx => 5
for sub in lst:
    for item in sub:
        print(item, end="")  # item 뒤에 붙는 문자 end=~
    print()
# 123
# 45
# 6789
