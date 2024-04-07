import re

txt = "I feel like restoring my previous routine and creating the peaceful environment by removing the extra people from my life, looking forward to that"
pattern = r"peaceful"
lol = re.split("\s",txt,8)
lol1 = re.search("\s", txt)
lol2 = re.findall("^I.*life$",txt)
lol3 = re.search("^I.*that$", txt)
lol4 = re.sub(pattern,"cozy",txt)

if lol:
    print("You go rock giiiirrrrrlll!")
else:
    print("Anyway you rock girl! ")


if lol1:
    print("You go rock giiiirrrrrlll!")
else:
    print("Anyway you rock girl! ") 


if lol2:
    print("You go rock giiiirrrrrlll!")
else:
    print("Anyway you rock girl! ")   


if lol3:
    print("You go rock giiiirrrrrlll!")
else:
    print("Anyway you rock girl! ")


if lol4:
    print("You go rock giiiirrrrrlll!")
else:
    print("Anyway you rock girl! ")            


print(lol)        
print(lol1)
print(lol2)
print(lol3)
print(lol4)