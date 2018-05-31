import re

text = "JGood is a handsome boy, he is cool, clever, and so on..."
regex = re.compile(r'\w*oo\w*')

print(re.findall(r'\w*oo\w*', text))
print(regex.findall(text))