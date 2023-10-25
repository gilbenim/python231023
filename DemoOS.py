# DemoOS.py
from os.path import *
from os import *
import glob

print("전체경로:", abspath("python.exe"))
print("파일명:", basename("c;\\work\\demo.txt")) #\\두번쓰는 이유는 특수문자 처리를 안전하게 하기 위함

# 특수문자로 가공하지 않은 상태 (raw string notation)
strPython = r"c:\python310\python.exe"
if exists(strPython):
    print("파일크기 : {0}".format(getsize(strPython)))
else:
    print("파일없음")

# 외부 실행파일 수행
# system("notepad.exe")

# 운영체제
print("운영체제이름:", name)
print("환경변수:", environ)

# result = glob.glob("c:\\work\\*.py")
# print(result)

for item in glob.glob("c:\\work\\*.py"):
    print(item)

# 공부 더 하고 싶으면 --> 점프 투 파이썬 (라이브러리 예제 편) 참고