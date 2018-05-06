# this is to excercise basic operations for dictionary
# new dictionary

import sys

info1 = {}
info2 = dict()

print (type(info1))
print (type(info2))

# initialize dictionary with values

info3 =  {'brother': 3, 'syster': 2}
info4 =  dict(brother=3, syster= 2)

print (type(info3))
print (type(info4))

# initialize dictionary with methods from_keys()

info5 = {}.fromkeys(['name', 'blog'], 'mytest_values')
print (info5)

# trigger exception with unexisted, get() methods would help retrieve the keys which is not existed gracefully.

#info5['mytest']

print(info5.get('mytest'))

# use update() which could update dictionary gracefully

info5.update({'name':'hehuang','sex' : 'male'})

print(info5)

# delete a item from dictionary

del(info5['sex'])

print(info5)

# iterations

for key, value in info5.items():
    print(key,':', value)



