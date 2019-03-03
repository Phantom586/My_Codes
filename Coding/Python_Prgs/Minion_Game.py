"""
And then comes a little optimization - if you know the starting letter,
you can add all substrings of different length that start with this letter.
It will be len(s) - i

For i=1 we are sure that there is an occurrence for all this substrings that start with a vowel (s[i] = 'A'):

- A
- AN
- ANA
- ANAN
- ANANA
So we add len(s)-i = 6-1 = 5 to kevin score.
"""

def minion_game(str):
    a = 0
    b = 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            a += len(s) - i
        else:
            b += len(s) - i
    if a == b:
        print("Draw")
    elif a < b:
        print("Stuart", b)
    else:
        print("Kevin", a)




if __name__ == "__main__":
    str = input()
    minion_game(str)