import re
file = open('sample1.txt','r')
text = file.read()
print(text)
pattern = r'\d{1,5}.\d{1,3}.\d{1,5}'
number= re.findall(pattern,text)
print(number)
