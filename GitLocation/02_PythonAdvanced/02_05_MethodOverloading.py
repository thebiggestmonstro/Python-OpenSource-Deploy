# 파이썬은 동적 타입 언어

# 1) 패킹을 이용한 오버로딩
class SampleA():
    # 패킹을 통해 오버로드를 수행
    def add(selfsel, *args):
        return sum(args)

a = SampleA()
print(f"add ver 01 {a.add(10, 20)}")
print(f"add ver 02 {a.add(10, 20, 30)}")
print(f"add ver 03 {a.add(1.05, 1.02, 1.03)}")

# 2) 자료형의 분기에 따른 오버로딩
class SampleB():
    def add(self, datatype, *args):
        if datatype == 'int':
            return sum(args)

        if datatype == 'str':
            return ''.join([word for word in args])

b = SampleB()

print(f"add ver 01 {b.add('str', "app", "ple")}")
print(f"add ver 02 {b.add('int', 20, 30)}")

# 3) Multiple Dispatch, multipledispatch 플러그인 설치해야 함
from multipledispatch import dispatch

class SampleC():
    @dispatch(int, int)
    def add(self, x, y):
        return x + y

    @dispatch(int, int, int)
    def add(self, x, y, z):
        return x + y + z

    @dispatch(str, str, str)
    def add(self, w1, w2, w3):
        return w1 + w2 + w3


c = SampleC()
print(f"add ver 01 {c.add(10, 20)}")
print(f"add ver 02 {c.add(20, 30, 50)}")
print(f"add ver 03 {c.add("Hello,", "World ", "from Python")}")