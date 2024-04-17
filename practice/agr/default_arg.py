def func1(num1, num2=10):
    print('a=', num1, 'b=', num2)


def func2(num1=10, num2=20):
    print('a=', num1, 'b=', num2)


# def func3(num1=10, num2): Default argument가 오른쪽부터 지정되어야 함
#     print('a=', num1, 'b=', num2)


func1(5)
func2(5, 5)
func2()
# func3(1, 1)
