# 일반 복사의 종류는 총 3개
# 1 - 1) Call by Value : 변수의 값을 복사하여 전달, 원본에 영향을 미치지 않음
# 1 - 2) Call by Reference : 변수의 메모리 주소를 전달, 원본에 영향을 미침
# 1 - 3) Call by Share : 변수의 메모리 주소를 복사하여 전달, 새로운 객체를 생성하면 원본에 영향을 주지 않음

# mutable 객체를 다루는 경우라면 얕은 복사와 깊은 복사에 주의해야 한다
# 그렇다면 얕은 복사와 깊은 복사는 무엇인가?
# 2 - 1) 얕은 복사 : 객체의 참조 값만 복사하여 원본 객체와 복사본이 같은 메모리 위치를 가리키도록 하는 복사
# -> 얕은 복사의 문제점 : 중첩된 객체의 경우 Outer의 경우 문제없이 복사하지만, Innter는 복사해주지 않음
# 2 - 2) 깊은 복사 : 객체의 모든 데이터를 새로운 메모리 공간에 복사하여 원본 객체와 완전히 독립적인 복사본을 만듬
# -> 얕은 복사의 문제점이었던 중첩된 객체의 경우에도 문제없이 복사해줌


# 1) 일반복사 - Call by Reference 예제
a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list

# 파이썬에서 객체의 주소를 출력 : id(객체)
print(id(a_list))
print(id(b_list))

b_list[2] = 100

print(a_list)
print(b_list)

b_list[3][2] = 100

print(a_list)
print(b_list)

# 위의 에제에서 볼 수 있듯이 muttable(가변형) 변수는 사용에 유의해야 한다 -> list, set, dict
# immutable(불변형) 변수 : int, str, bool, float

# 2) 얕은 복사 예제
import copy

c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list)

print(id(c_list))
print(id(d_list))

d_list[2] = 100

print(c_list)
print(d_list)

d_list[3][2] = 100

print(c_list)
print(d_list)

# 3) 깊은 복사
e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list)

print(id(e_list))
print(id(f_list))

f_list[2] = 100

print(e_list)
print(f_list)

f_list[3][2] = 100

print(e_list)
print(f_list)