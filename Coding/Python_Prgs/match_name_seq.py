# a regex that matches the full name of someone
# whose last name is Nakamoto? You can assume that the first name that
# comes before it will always be one word that begins with a capital letter

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