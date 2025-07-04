# type 함수 예제
class SampleA():
    pass

obj = SampleA()
print(f"__class__ 메서드를 사용하여 인스턴스로부터 클래스 타입 판별 : {obj.__class__}")
print(f"type 함수를 사용하여 인스턴스로부터 클래스 타입 판별 : {type(obj)}")
print(f"__class__ 메서드와 type 함수 실행결과 비교 : {obj.__class__ is type(obj)}")

print(f"__class__ 메서드를 사용하여 클래스로부터 클래스 타입 판별  : {obj.__class__.__class__}")
print(f"type 함수를 사용하여 클래스로부터 클래스 타입 판별 : {type(type(obj))}")
print(f"클래스에 대한 __class__ 함수와 type 함수 실행결과 비교 : {obj.__class__.__class__ is type(type(obj))}")

print(f"__class__ 메서드를 사용하여 type 메타 클래스로부터 클래스 타입 판별  : {type.__class__}")
print(f"type 함수를 사용하여 type 메타 클래스로부터 클래스 타입 판별  : {type(type)}")
print(f"type 메타 클래스에 대한 __class__ 함수와 type 함수 실행결과 비교 : {type.__class__ is type(type)}")

# 결론
# obj1은 SampleA 클래스의 인스턴스
# SampleA의 메타 클래스는 type 메타 클래스
# type 메타 클래스의 메타 클래스는 자기 자신인 type 메타 클래스

n = 10
d = {'a' : 10, 'b' : 20}

class SampleB():
    pass

obj2 = SampleB()

for i in (n, d, obj2):
    print(f"{type(i)} {type(i) is i.__class__} {i.__class__.__class__}")

for i in int, float, str, list, tuple, dict:
    print(f"{type(i)}")