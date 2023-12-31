# DemoRE.py
# 정규표현식(특정한 규칙)
import re

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())
# 함정 추가
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

result = re.search("apple", "this is Apple".lower())
print(result.group())

result = re.search("\d{4}", "올해는 2023년입니다")
print(result.group())

result = re.search("\d{5}", "우리 동네는 52300")
print(result.group())

#컴파일 함수를 사용
data = "Apple is big company and apple is delicious"
c = re.compile("apple", re.IGNORECASE) # IGNORECASE 의미 : 대소문자 구분없이
print(c.findall(data))

data = """다중 라인으로
만든 문자열

데이터"""

c = re.compile("^.+", re.MULTILINE) # MULTILINE의미 : 빈줄은 제외하고.... "^.+"는 ^시작, .글자, +1~N번
print(c.findall(data))