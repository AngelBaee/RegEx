import re

txt = "People to people, party to place"
x = re.search(r"\bp\w+", txt)
print(x.string)
