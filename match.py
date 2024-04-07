import re

txt = "Be the better version of yourself,  only fight with yourself"
lol = re.search("er", txt)
lol_1 = re.search(r"\by\w+", txt)

print(lol)
print(lol_1.span())
