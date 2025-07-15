# 이전메 만든 클래스 import
# 파이썬에서 숫자로 시작하는 클래스는 import가 불가능함
from PythonAdvanced_04_02 import GIFGenerator as gfg

# 클래스 생성
g = gfg(inputPath='./project/images/*.png', outputPath='./project/image_out/result.gif', imgSize=(640, 480))

# 실행
g.generate_gif()

# 위와 같은 방법이 일반적인 외부 모듈 사용법
# 지금부터는 모듈을 패키지로 만들어 배포하는 방법을 알아본다
# 패키지를 만들어 배포하는 방법은 PyPI를 통해 이뤄진다
# PyPI에 속한 패키지는 pip 명령어를 통해 설치할 수 있다

# 절차
# 1) pypi에 회원가입
# 2) 패키지 설치 폴더에 pip 명령어로 설치하기 위한 이름의 폴더 생성
# 3) 2)에서 생성한 폴더 안에 __init__.py 파일 생성 -> 해당 파일이 없으면 패키지로 인식하지 않음
# 4) 이전에 생성한 클래스(모듈) 파일을 2)에서 생성한 폴더에 추가
# 5) 4)에서 추가한 파일의 이름을 패키지 이름으로 변경

# 여기까지가 패키지로서 배포하기 위한 기본 설정

# 패키지 설치 폴더 구성 알아보기
# 1) .gitignore : 불필요한 파일의 레포지터리 배포를 막음
# 2) LICENSE : 패키지의 라이센스 정의
# 3) MANIFEST.in : 파이썬과 관련되지 않았지만 설치해야 하는 파읻들을 명시
# 4) README.md : 사용자에게 해당 패키지에 대한 정보를 알려줌
# 5) requirements.txt : 필요한 패키지와 버전을 명시하는 텍스트 파일
# 6) setup.cfg : 패키지 설정 정보를 담는 파일
# 7) setup.py : 배포할 패키지와 관련된 정보를 기입

# 이 중에서 2) + 3) + 7) 파일들은 반드시 필요하다
# 그러나 Git을 통해 파일을 배포하지 않는 이상, 2) ~ 7)까지의 파일들은 기본적으로 사용하는 것이 좋다

# 이후의 작업
# 8) setuptools 플러그인과 wheel 플러그인을 설치하여 패키징
# 가상환경에서 작업하는 경우 설치 방법 : python -m pip install --upgrade setuptools wheel
# 가상환경에서 작업하지 않는 경우 설치 방법 : python -m pip install --user --upgrade setuptools wheel
# 9) 패키징된 패키지를 빌드하여 배포파일 생성 : python setup.py sdist bdist_wheel
# 10) 빌드 결과물 확인 : dist 폴더 -> 패키지 이름-버전.gz 압축파일
# 11) PYPI 배포 첫 번째 단계(필요한 플러그인 설치) : pip install twine
# 12) PYPI 배포 두 번째 단계(업로드) : python -m twine upload dist/*
# 13) 패키지 설치 확인 : pip install pygifgenerator_testver
# 14) 패키지 사용 : from pygifgenerator_testver.gifgenerator import GIFGenerator