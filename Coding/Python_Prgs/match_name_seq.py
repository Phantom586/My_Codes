import re

pattern = re.compile(r'[A-Z][a-zA-Za-z]+\ (Nakamoto)')

str = """
    Satoshi Nakamoto
    Alice Nakamoto
    RoboCop Nakamoto
    satoshi Nakamoto
    Mr. Nakamoto
    Nakamoto
    Satoshi nakamoto
    """

p = pattern.finditer(str)
for i in p:
    print(i.group())