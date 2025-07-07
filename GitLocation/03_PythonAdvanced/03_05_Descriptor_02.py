# Descriptor VS Property
# 전자 : get / set과 같은 데이터 조작 함수의 기능 확장
# 후자 : 어노테이션을 통한 데이터 조작 함수의 정의

# Descriptor의 장점
# 1) 상황에 맞는 메서드 구현을 통한 OOP 구현
# 2) Property와는 다르게 재사용이 가능함
# 3) ORM Framework(객체-관계 매핑) 사용

# 예제 - 1

import os

# Descriptor
class DirectoryFileCount:
    def __get__(self, obj, objtype=None):
        print(os.listdir((obj.dirname)))
        return len(os.listdir(obj.dirname))
class DirectoryPath:
    # Descriptor Instance
    size = DirectoryFileCount()

    def __init__(self, dirname):
        self.dirname = dirname

# 현재 경로
s = DirectoryPath('./')
s.size

# 이전 경로
g = DirectoryPath('../')
g.size

# 명확한 정보를 얻고 싶다면, 인스턴스 또는 클래스에 접근하여 __dict__ 함수 사용

# 예제 - 2
import logging

logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

class LoggedScoreAccess:

    def __init__(self, value=60):
        self.value = value

    def __get__(self, obj, objtype=None):
        logging.info('Accessing %r giving %r', 'score', self.value)
        return self.value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', 'score', self.value)
        self.value = value

class Student:
    # Descriptor instance
    score = LoggedScoreAccess()

    def __init__(self, name):
        # Regular instance attribute
        self.name = name


s1 = Student('Kim')
s2 = Student('Lee')

# 점수 확인(s1)
print(s1.score)
s1.score += 10
print(s1.score)

# 점수 확인(s2)
print(s2.score)
s2.score += 20
print( s2.score)

# __dict__ 확인
print(vars(s1))
print(vars(s2))
print(s1.__dict__)
print(s2.__dict__)
