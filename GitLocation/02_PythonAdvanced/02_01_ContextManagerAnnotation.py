
# 1) Decorator를 통해 Context Manager 생성
# 보다 정교한 예외처리는 클래스 방식이 좋지만, 함수 형식이 훨씬 간단하다
import contextlib
import time

@contextlib.contextmanager
def my_file_writer(file_name, method):
    f = open(file_name, method)
    yield f   # __enter__
    f.close() # __exit__

with my_file_writer('TestFile4.txt', 'w') as f:
    f.write('Context Manager Test4.\nContextlib Test4.')

# 2) Decorator를 통해 기존의 타이머 예제 작성
@contextlib.contextmanager
def ExecutionWithTimer(msg):
    start = time.monotonic()
    try:
        # __enter__
        yield start
    except Exception as e:
        print(f'Error Ocurred : {msg} {e}')
        raise
    else:
        # __exit__
        print(f'Total time of {msg} : {time.monotonic() - start}')

with ExecutionWithTimer("Hello from decorator") as et:
    print(f'Start at {et}')
    for i in range(30000000):
        pass
    #raise Exception("Forced Error")