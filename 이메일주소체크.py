import re

# Regular expression pattern for email address validation
# 이메일 주소의 유효성을 검사하기 위한 정규식 패턴입니다.
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'

# List of sample email addresses for testing
# 테스트를 위한 샘플 이메일 주소 목록입니다.
sample_emails = [
    "john.doe@example.com",     # 유효한 이메일 주소
    "user123@gmail.com",        # 유효한 이메일 주소
    "support@my-website.net",   # 유효한 이메일 주소
    "contact.me@company.co.uk", # 유효한 이메일 주소
    "invalid-email",            # 유효하지 않은 이메일 주소
    "user@.com",                # 유효하지 않은 이메일 주소
    "@domain.com",              # 유효하지 않은 이메일 주소
    "user@domain",              # 유효하지 않은 이메일 주소
    "user@.com.",               # 유효하지 않은 이메일 주소
    "user@.com.."               # 유효하지 않은 이메일 주소
]

# Function to check if an email is valid
# 주어진 이메일 주소가 유효한지 확인하는 함수입니다.
def is_valid_email(email):
    return re.search(email_pattern, email) is not None

# Test the sample email addresses
# 샘플 이메일 주소를 테스트합니다.
for email in sample_emails:
    if is_valid_email(email):
        print(f"{email} is a valid email address.")
        # 유효한 이메일 주소인 경우 출력
    else:
        print(f"{email} is not a valid email address.")
        # 유효하지 않은 이메일 주소인 경우 출력

