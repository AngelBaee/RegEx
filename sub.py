import re

txt = "Sometimes people exegerate and cross the line of the humanity without realizing the concept of their own actions, thats pathetic"

pattern = r"exegerate"

lol = re.sub(pattern,"overact",txt)

print(lol)