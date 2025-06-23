'''
lambda의 특징
1) 메모리에서 생성되는 함수와는 다르게 힙 영역에서 생성되어 사용하면 즉시 소멸
2) 람다 함수의 객체는 사용 후 소멸되므로 참조 카운트가 0이 되어 가비지 컬렉션 대상이 되어 사용한 공간을 회수함 = 메모리 관리 호율이 좋음
'''

# 1) 람다의 사용방식 : 람다객체 = lambda 매개변수 : Lambda식
cal = lambda a, b, c : a * b + c
print(cal(10, 15, 20))

# 2) 시퀀스안에서의 람다 사용 : [로직 for 순회인덱스 in range(n, len(시퀀스))]
digits1 = [x * 10 for x in range(1, 11)]
print(digits1)

# 3) Lambda와 map 함수 사용 : 객체 = map(lambda식 또는 lambda 객체, 시퀀스)
# lambda 식을 사용
res1 = list(map(lambda i : i ** 2, digits1))
print(res1)

# lambda 객체 사용
lambdaEx = lambda i : i ** 2
res2 = list(map(lambdaEx, digits1))
print(res2)

# Closure 구조에서 사용
def doSquare(nums):
    def double(x):
        return x ** 2
    return list(map(double, nums))

print(doSquare(digits1))

# 4) lambda와 filter 함수 사용 : filter(람다식 또는 람다 객체, 시퀀스)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res3 = list(filter(lambda i : i % 2 == 0, nums))
print(res3)

# Closure 구조에서 사용
def doFindEvenNumbers(nums):
    def even(x):
        return x % 2 == 0
    return list(filter(even, nums))

print(doFindEvenNumbers(nums))

# 5) lambda와 reduce 함수 사용(단, 파이썬 3부터 외부에서 모듈을 포함해야 함)
# 사용방식 : reduce(람다식 또는 람다객체, 시퀀스)
from functools import reduce

nums2 = [x for x in range(1, 101)]

res4 = reduce(lambda x, y : x + y, nums2)
print(res4)

# Closure 구조에서 사용
def doAddSequence(nums):
    def add(x, y):
        return x + y
    return reduce(add, nums)

print(doAddSequence(nums2))