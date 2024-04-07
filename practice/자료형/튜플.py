# 위치가변인자 -> 임의의 개수를 받는 함수를 가리켜 가변인자를 사용
# 인자를 튜플로 전달
def calc(check, *value):
    num = 0
    for i in value:
        num = num + i

    if check:
        return num, set(value), check
    else:
        return set(value)


def f(x, y, **dict):
    return x, y, dict
# 가변 파라미터 -> 키워드 인자
# 키워드를 딕셔너리로 전달하여 딕셔너리 자료형으로 반환
k = calc(1, 1, 2, 3, 4, 1, 2)
print(k)

j = f(1, 2, flag=True,
      mode='fast', header='debug')
print(j)
