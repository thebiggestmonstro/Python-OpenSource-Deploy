
# 이전에 만들어본 Context Manager의 구성을 사용하는 타이머 예제 생성

import time

class ExecutionWithTimer(object):
    def __init__(self, msg):
        self.msg = msg

    # 작업을 시작하는 시점의 시간 저장
    def __enter__(self):
        # time.monotonic : 시간을 숫자형으로 반환
        self._start = time.monotonic()
        return self._start


    # __exit__ 매직 메서드가 호출되는 시점은 작업을 종료하는 시점인데,
    # (작업을 종료하는 시점의 시간 - 작업을 시작하는 시점의 시간)의 값을 반환하여 순수하게 작업한 시간을 반환
    def __exit__(self, errorType, errorValue, errorPoint):
        if(errorType):
            print(f"Execption occurred : {errorType} {errorValue} {errorPoint}")
            return False
        else:
            print(f"{self.msg} : {time.monotonic() - self._start}")
        return True

# 위와 같은 예제가 바로 사용자 정의 Context Manager의 장점
# with 메서드에서 해당 클래스를 사용하는 경우, 리소스를 다루는 작업에 소모한 시간을 출력할 수 있다
# 즉, Context Manager의 작업을 단순 리소스를 다루는 개념에서 확장해 줄 수 있다

with ExecutionWithTimer("Total time for execution") as ce:
    print(f'Received Start at {ce}')
    for i in range(30000000):
        pass
    raise Exception("Forced Error")