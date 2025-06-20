'''
1) Global Scope VS Local Scope
# 파이썬은 Local Scope를 먼저 탐색한 후에 Global Scope를 탐색한다
'''
b = 20

def foo():
    b = 30
    print(f"foo : {b}")

def foo2():
    print(f"foo2 : {b}")

foo()
foo2()

'''
2) Keyword - global
global 키워드없이 Local Scope 내에서 전역변수를 수정할 수 없다
gloabal 키워드가 수식된 변수는 Local Scope에서의 수정값이 반영된다
'''
c = 20

def foo3():
    global c
    c = c + 10

print(f"Before foo3 : {c}")
foo3()
print(f"After  foo3 : {c}")

'''
3) Keyword - nonlocal
함수의 안에서 함수를 리턴하는 Closure에서 사용한다
Inner Scope에서 Outer Scope의 변수를 사용하기 위해 사용한다 
'''
def outer():
    d = 70
    i = 0

    # closure
    def inner():
        nonlocal d
        nonlocal i
        i += 1
        d += 10
        print(f"No.{i} value of d : {d}")
    return inner

in_test = outer()
in_test() # i와 d의 값이 저장되어 호출할때마다 1과 10씩 증가하여 출력됨

'''
4) locals 함수 : Local Scope 안의 모든 구성요소들을 리턴한다
리턴하는 형식은 딕셔너리이다
'''
def func(var):
    x = 10
    def printer():
        print(f"From Inner")
    # locals 함수를 통해 해당 scope의 구성요소들을 가져올 수 있음
    print("From Outer", locals())

func('hi')

'''
5) globals 함수 : Global Scope의 모든 구성요소들을 리턴한다
locals 함수와 동일하게 딕셔너리 형식으로 리턴한다
'''
print("From Global Scope", globals())

'''
Local Scope와 Global Scope의 구성요소가 모두 딕셔너리로 반환되므로
이를 조작하면 'Local Scope'안에서 전역변수의 생성도 가능하다
'''
for i in range(1, 10):
    for k in range(1, 10):
        globals()[f'plus_{i}_{k}'] = i + k

print(globals())
print(plus_2_3)