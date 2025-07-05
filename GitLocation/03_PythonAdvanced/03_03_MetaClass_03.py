
# 1) type 클래스를 상속하지 않는 커스텀 메타 클래스
def custom_multiple(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d

def custom_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new

# 새로운 리스트 클래스 생성
CustomList1 = type(
    'CustomList1',
    (list,),
    {
        'desc' : '커스텀 리스트 1',
        'custom_multiple' : custom_multiple,
        'custom_replace' : custom_replace,
    }
)

c1 = CustomList1([1,2,3,4,5,6,7,8,9])
c1.custom_multiple(1000)
print(f"{c1}")

c1.custom_replace(1000, 7777)
print(f"{c1}")

print(f"{c1.desc}")


# 2) type 클래스를 상속받은 커스텀 메타 클래스
# type 클래스를 상속받으면 클래스 내부에 새롭게 동작하는 매직 메서드를 정의할 수 있음
# 매직 메서드 호출 순서는 new -> init -> call 순서로 이뤄진다
# 매직 메서드 내에서 조건에 따라 분기하여 처리하도록 하는 방식을 후킹이라고 한다
class CustomListMeta(type):

    # 클래스의 인스턴스를 생성, 메모리 초기화
    def __new__(metacls, name, bases, namespace):
        print('__new__ : ', metacls, name, bases, namespace)
        namespace['desc'] = '커스텀 리스트2'
        namespace['custom_multiple'] = custom_multiple
        namespace['custom_replace'] = custom_replace

        return type.__new__(metacls, name, bases, namespace)

    # 생성된 인스턴스를 초기화
    def __init__(self, object_or_name, bases, dict):
        print(f'__init__ : {self} {object_or_name} {bases} {dict}')
        super().__init__(object_or_name, bases, dict)

    # 생성한 인스턴스 실행, 클래스에서 넘겨준 파라미터를 인자로 사용함
    def __call__(self, *args, **kwargs):
        print('__call__ : ', self, *args, **kwargs)
        return super().__call__(*args, **kwargs)

CustomList2 = CustomListMeta('CustomList2',(list, ),{})
c2 = CustomList2([1, 2, 3, 4, 5, 6, 7, 8, 9])

c2.custom_multiple(100)
print(f"{c2}")

c2.custom_replace(100, 777)
print(f"{c2}")

print(f"{c2.desc}")
print(f"{CustomList2.__mro__}") # 상속 확인