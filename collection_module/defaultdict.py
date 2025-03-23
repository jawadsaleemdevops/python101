sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

reg_dict = {}
for word in words:
    if word in reg_dict:
        reg_dict[word] += 1
    else:
        reg_dict[word] = 1

print(reg_dict)



## DefaultDict

from collections import defaultdict

sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

d = defaultdict(int)
for word in words:
    d[word] += 1

print(d)
print(dict(d)) # convert to reg dict


## python list type as default factory

my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

reg_dict = {}
for acct_num, value in my_list:
    if acct_num in reg_dict:
        reg_dict[acct_num].append(value)
    else:
        reg_dict[acct_num] = [value]
print(reg_dict)
print("type: ",type(reg_dict))
print(reg_dict[345])


## using defaultdict

from collections import defaultdict

my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

d = defaultdict(list)
for acct_num, value in my_list:
    d[acct_num].append(value)
    

print(d[345])

## Using lambda as default_factory

from collections import defaultdict

animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'

print (animal['Nick'])

print (animal)


