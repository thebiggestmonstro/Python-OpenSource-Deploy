
# type 함수를 이용한 동적 클래스 생성
# 인자는 다음과 같다
# Name : 클래스 이름
# Bases : 상속받을 클래스들
# Dct : 생성할 클래스의 어트리뷰트와 메서드

# 1) type 함수를 이용한 클래스 동적 생성
s1 = type('SampleA', (), {})
print(s1)           # <class '__main__.SampleA'> , 클래스 SampleA가 출력
print(type(s1))     # <class 'type'>, 메타 클래스 type이 출력
print(s1.__base__)  # <class 'object'>, 파이썬에서 모든 클래스는 object로부터 상속됨
print(s1.__dict__)  # 클래스가 갖고 있는 어트리뷰트와 메서드 출력

# 2) 클래스 동적 생성 + 클래스 상속
class Parent1:
    pass

s2 = type('Child1', (Parent1,), dict(attr1=100, attr2='Hi'))
print(s2)           # <class '__main__.Child1'>
print(type(s2))     # <class 'type'>
print(s2.__base__)  # <class '__main__.Parent1'>
print(s2.__dict__)  # {'attr1': 100, 'attr2': 'Hi', '__module__': '__main__', '__doc__': None}
print(s2.attr1, s2.attr2)

# 3) 클래스 동적 생성 + 메서드 설정
s3 = type(
        'Sample2',
        (),
        dict(attr1=30, attr2=100,add=lambda x, y : x + y, multiple=lambda x, y : x * y )
    )

print(s3)                                   # <class '__main__.Sample2'>
print(type(s3))                             # <class 'type'>
print(s3.__base__)                          # <class 'object'>
print(s3.__dict__)                          # {'attr1': 30, 'attr2': 100, 'add': <function <lambda> at 0x00000253E4E78F40>, 'multiple': <function <lambda> at 0x00000253E4ED94E0>, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'Sample2' objects>, '__weakref__': <attribute '__weakref__' of 'Sample2' objects>, '__doc__': None}
print(s3.attr1, s3.attr2)                   # 30 100
print(s3.add(s3.attr1, s3.attr2))           # 130
print(s3.multiple(s3.attr1, s3.attr2))      # 3000