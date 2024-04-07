import re 
txt = "Jerk never last long"
x = re.search("\s", txt)
xp = re.search("Nerd",txt)
pp = re.split("\s", txt)

print("The first white-space character is located in position:", x.start())
print(xp)
print(pp)