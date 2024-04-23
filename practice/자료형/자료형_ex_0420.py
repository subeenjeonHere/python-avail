a = b = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(id(a))
print(id(b))
# a,b는 같은 메모리 주소를 참조함

b[-1] = 5
b = set(a)
# set(a)로 b에 새로운 set 객체를 할당
print(id(a))
print(id(b))
# b의 메모리 주소는 변경됨
# 4366535040
# 4366963360

c = list(b)
print(a)
print(b)
print(c)
print(a is b)