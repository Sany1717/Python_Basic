import re

text = "The rain is Spain"
print(re.findall("[a-m]",text))

Text = "1 is the special characters"
pattern = "^1"
a = re.findall(pattern,Text)

if a:
    print("yes,1 is characters special")
else:
    print("nope,1 is not special characters")

Text1 = "1 is the characters special"
pattern1 = "special$"
a1 = re.findall(pattern1,Text1)

if a1:
    print("yes,is it special characters")
else:
    print("nope,is it not special characters")