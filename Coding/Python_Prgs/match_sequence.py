# a regex that matches a sentence where the first
# word is either Alice, Bob, or Carol; the second word is either eats, pets, or
# throws; the third word is apples, cats, or baseballs; and the sentence ends
# with a period? This regex should be case-insensitive.

import re

pattern = re.compile(r'(Alice|Bob|Carol)+\ (eats|pets|throws)+\ (apples|cats|baseballs)+\.', re.I)

str = """
    Alice eats apples.
    Bob pets cats.
    Carol throws baseballs.
    Alice throws Apples.
    BOB EATS CATS.
    RoboCop eats apples.
    ALICE THROWS FOOTBALLS.
    Carol eats 7 cats.
"""

for match in pattern.finditer(str):
    print(match.group())
