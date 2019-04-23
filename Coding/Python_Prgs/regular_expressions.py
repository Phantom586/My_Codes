import re

example_string = """
                harshchaurasia586@gmail.com
                Ph@ntom#123
                586pboy@gmail.com
                Pboy1234
                h.chaurasia@gmail.com
                dyn_586@gmail.com
                Dyn_123@yahoo.com
                www.google.com
                https://www.packagecontrol.io
                http://www.continuum.io/downloads
                www.google.com/fun/have/some
                https://www.youtube.com/watch?v=K8L6KVGG-7o
                 """


# Match any type of emails
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+')


# Match any type of URL's
pattern = re.compile(r'(http|https)?(://)?[a-zA-Z]+\.[a-zA-Z0-9]+\.[a-z]+[/a-zA-Z0-9?=+-_]*')

matches = pattern.finditer(example_string)

for match in matches:
    print(match)
