# Descriptor 핵심 키워드
# descriptor, set, get, del, property

# Descriptor : 객체(클래스)에서 다른 객체(클래스)를 속성값으로 가지는 것
# Read / Write / Delete 등을 미리 정의 가능
# 데이터를 수정하는 경우 : data descriptor라고 부름, 대표적으로 set, del
# 데이터를 수정하지 않는 경우 : non-data descriptor라고 부름, 대표적으로 get
# Descriptor를 사용하여 의도하는 방향으로 클래스를 생성할 수 있음

# 1) 기본적인 Descriptor
class DescriptorEx1():
    def __init__(self, name="Default"):
        self.name = name

    def __get__(self, obj, objtype):
        return f'Get method called / self : {self} / obj : {obj} / objtype : {objtype} / name : {self.name}'

    def __set__(self, obj, name):
        print(f"Set method called")
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('Name Should be string')

    def __delete__(self, obj):
        print(f"Delete method called")
        self.name = None

class Sample1():
    name = DescriptorEx1()

s1 = Sample1()
s1.name = "Descriptor Test1"

print(f"{s1.name}")

del s1.name

# 2) property 클래스를 사용하여 Descriptor 직접 구현
# property 클래스의 구성 : class property(fget=None, fset=None, fdel=None, doc=None)
# 이렇게 만드는 경우 메서드 이름을 직접 정의할 수 있음
class DescriptorEx2():
    def __init__(self, value):
        self._name = value

    def getter(self):
        return f'Get method called / self : {self} / name : {self._name}'

    def setter(self, value):
        print(f'Set method called')
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError('value should be str')

    def deletter(self):
        print(f'Delete method called')
        self._name = None

    name = property(getter, setter, deletter, 'Property class example')

s2 = DescriptorEx2('Descriptor Test2')

print(f'{s2.name}')

s2.name = "New Name"

del s2.name

print(f"{DescriptorEx2.name.__doc__}")