import re

example_string = """
                daniel#1234@gmail.com
                Fhewfb#186
                Juven5876@gmail.com
                HDFKHG287#
                Phantom#123
                Dyn_586
                ImIn54n3
                h.kdjfhkdf@gmail.com
                DFj_545@gmail.com
                Fdhfh_4551@yahoo.com
                www.google.com
                https://www.packagecontrol.io
                http://www.continuum.io/downloads
                www.google.com/fun/have/some
                https://www.youtube.com/watch?v=K8L6KVGG-7o
                 """


# Match any type of emails
email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+')


# Match any type of URL's
url_pattern = re.compile(r'(http|https)?(://)?[a-zA-Z]+\.[a-zA-Z0-9]+\.[a-z]+[/a-zA-Z0-9?=+-_]*')

# Matching Passwords
pass_pattern = re.compile(r'[A-Z]+[a-zA-Z0-9!@#$%^&*()_+]+[!@#$%^&*()_+]+[a-zA-Z0-9]+')

match1 = email_pattern.finditer(example_string)

match2 = url_pattern.finditer(example_string)

match3 = pass_pattern.finditer(example_string)

# for match in match3:
#     print(match)
print(pass_pattern.match("ph@ntom#123"))

# for match in match2:
#     print(match)
