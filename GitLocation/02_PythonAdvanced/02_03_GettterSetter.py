
# 프로퍼티를 사용하면 얻을 수 있는 장점
# 1) 변수에 제약을 설정할 수 있다
# 2) 캡슐화를 이끌어낼 수 있다
# 3) Pythonic한 코드를 작성할 수 있다

class SampleA:
    def __init__(self):
        self.x = 0
        self._y = 0

    # getter
    @property
    def y(self):
        return self._y

        # setter
    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("값은 0보다 커야 합니다.")
        self._y = value

    # deleter
    @y.deleter
    def y(self):
        del self._y

a = SampleA()

print(f"Set하기 이전, 단순 Get한 값 : x = {a.x}, y = {a.y}")

a.x = 1
a.y = 5

print(f"Set한 이후 값 : x = {a.x}, y = {a.y}")

del a.y
#print(f"x : {a.x}, y : {a.y}")