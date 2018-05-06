# EasyDict makes you access the attributes just like you access the variables

d = {'brother': 3, 'sister': 5}

age = d['brother']

print("Age of the brother is", age)

from easydict import EasyDict as edict

x = edict(d)

print(x.brother)

print(x.sister)

