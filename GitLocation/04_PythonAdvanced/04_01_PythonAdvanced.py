
# 패키지의 목적 : 정적인 이미지를 GIF로 변환하는 패키지

import glob
from PIL import Image

# GIF 파일에서 사용할 이미지들의 경로와 GIF 파일의 생성 경로
path_in = './project/images/*.png'
path_out = './project/image_out/result.gif'

# GIF 파일의 대표 이미지와 GIF 파일에서 사용할 이미지들
img, *images = [Image.open(f) for f in sorted(glob.glob(path_in))]

# 이미지간의 사이즈 통일
# 인자 : 조정할 사이즈, 이미지의 여백 제거
img, *images = [Image.open(f).resize((320, 240), Image.LANCZOS) for f in sorted(glob.glob(path_in))]

# 이미지 저장
img.save(
    fp = path_out,
    format='GIF',
    append_images=images,
    save_all=True,
    duration=500, # GIF의 프레임 전환 시간
    loop=0,       # 반복 여부
    disposal = 2
)