import re

EMAIL_PATTERN = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

email_re = re.compile(EMAIL_PATTERN)

def validate_email( test_str ):
    return email_re.match( test_str)

