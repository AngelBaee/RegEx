import re 

kk = "Need to appreciate on time"
pp = re.search("^Need.*time$", kk)
pp = re.findall("e", kk)
pp1 = re.findall("Hell what?", kk)

if pp:
    print("Totally bae!")

else:
    print("Hell no")

print(pp)
print(pp1)

       

if (pp1):
  print("Hell yeah")

else:
  print("Get the hell out!")    
