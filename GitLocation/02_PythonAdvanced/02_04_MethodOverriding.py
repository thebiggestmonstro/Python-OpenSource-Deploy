
# 예제 1 : 상속된 프로퍼티는 인스턴스화하면서 전달됨
class ParentEx1():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class ChildEx1(ParentEx1):
    pass

c1 = ChildEx1()
p1 = ParentEx1()

print(f"ChildEx1 Class : {ChildEx1.__dict__}")
print(f"ParentEx1 Class : {ParentEx1.__dict__}")

print(f"ChildEx1 Instance : {c1.__dict__}")
print(f"ParentEx1 Instance : {p1.__dict__}")

# 예제 2 : 메서드 오버라이딩
class ParentEx2():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class ChildEx2(ParentEx2):
    def get_value(self):
        return self.value * 10

c2 = ChildEx2()
print(f"c2 value : {c2.get_value()}")

class ParentEx3():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class ChildEx3(ParentEx3):
    def get_value(self):
        print("using parent`s value")
        return super().get_value() * 100

    def get_value2(self):
        print("using parent`s value 2")
        return super(ChildEx3, self).get_value()


c3 = ChildEx3()
print(f"c3 value : {c3.get_value()}")
print(f"c3 value : {c3.get_value2()}")