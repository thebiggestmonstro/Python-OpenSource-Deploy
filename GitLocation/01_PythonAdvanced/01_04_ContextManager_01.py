'''
__(언더스코어 2개)가 수식된 메서드 : Magic 메서드 또는 Special 메서드
어떤 인스턴스가 초기화될 때 Python에서 정한 규칙대로 호출되는 메서드를 의미한다
'''

# Context Manager : 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할

# 예제 1 - with 구문 추가 이전
file = open('./testfile1.txt', 'w')
try:
    file.write('Context Manager Test1\nContextlib Test1.')
finally:
    file.close()

# 예제 2 - with 구문
with open('./testfile2.txt', 'w') as f:
    f.write('Context Manager Test2\nContextlib Test2.')

# 예제 3 - 사용자 정의 ContextManager
class MyFileHandler():
    def __init__(self, file_name, method):
        print('MyFileHandler started : __init__')
        self.file_obj = open(file_name, method)

    def __enter__(self):
        print('MyFileHandler enter : __enter__')
        return self.file_obj

    def __exit__(self, exc_type, value, trace_back):
        print('MyFileHandler started : __exit__')
        if exc_type:
            print(f'Logging Execption {exc_type} {value} {trace_back}')
        self.file_obj.close()


with MyFileHandler('./testfile3.txt', 'w') as f:
    f.write('Context Manager Test3\nContextlib Test3.')
