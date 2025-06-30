
# 예제 1 : 파이썬 인터프리터에서의 마지막 연산 값
# 예제 2: 값 무시(Unpacking)
for _, value in enumerate(range(5)):
    print(value)

for value in enumerate(range(5)):
    print(value)

a, b, c = (1, 2, 3)
print(a, c)

d, _, f = (10, 20, 30)
print(d, f)

x, *y, z = (1, 2, 3, 4, 5)
print(x, y, z)

xx, *_, zz = (10, 20, 30, 40, 50)
print(xx, zz)

# 예제 3 : 숫자 자리 구분
num1 = 1_000_000
num2 = 7777_7777_7777
print(num1)
print(num2)

# 예제 4 : 접근지정자
# 변수명 = public
# _변수명 = protected
# __변수명 = name mangling(해당 변수의 이름을 _클래스명__변수명으로 변경하는 동작) : 클래스가 여러 번 확장되더라도 충돌 없이 오버라이드를 하기 위함
class SampleA:
    def __init__(self):
        self.x = 0      # public
        self._y = 0     # protected
        self.__z = 0    # name mangling

a = SampleA()
a.x = 1

print(f"{a.x}")  # public 프로퍼티 출력
print(f"{a._y}") # protected 프로퍼티 출력, 파이썬의 접근제어자는 강제성을 띄지 않음
# print(f"{a.__z}")  # name mangling 프로퍼티는 변하기 이전의 변수를 사용하면 에러 발생
# print(f"{dir(a)}") # dir 함수로 클래스 구성을 확인해보면, 다른 프로퍼티와 다르게 __z는 _SampleA__z로 보여지고 있음
# 확인한 이후, 변한 이후의 변수명을 사용하여 값을 설정하고 출력
print(f"{a._SampleA__z}")