def exam(num1, num2=2):
    # 인자 2개, num1 num2을 받음
    # num2는 기본값 2인데 함수 호출 시 num2에 대한 값 전달하지 않으면 default 2가 사용

    print('a=', num1, 'b=', num2)


# num1은 20으로, num2는 기본값인 2로 설정됨
exam(20)


# a=0 b=2
# ans: a= 20 b= 2

def test(num1, num2=30, num3=30):
    # 기본값이 지정된 인자 뒤에 기본값이 없는 인자 올 수 없음
    # num3에 인자 지정해주면 에러해결
    print('a= ', num1, 'b= ', num2, 'c= ', num3)

test(100,200)







