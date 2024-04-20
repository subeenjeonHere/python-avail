def calc(check, *val):
    num = 0
    for i in val:
        num = num + i

    if check:
        # return num, set(val), check # 튜플 형태로 반환
        # return [num, set(val), check]  # 리스트 형태 반환

        # 딕셔너리 자료형으로 반환
        # 파이썬 가변인자 받을 때 튜플로 처리 ( )
        # {'total': 21, 'val': (1, 2, 3, 4, 5, 6)}
        return {"total": num, "val": val}

        # 리스트로 반환하고 싶으면
        # return {"total": num, "val": list(val)}


k = calc(1, 1, 2, 3, 4, 5, 6)
print(k)
