from collections import Counter

counter = Counter('abcabbb')
print (list(counter))
print(counter)
print (list(counter.elements()))
print( counter.most_common(1))



# Counter Subtract
counter_one = Counter("superfluous")
print(counter_one)


counter_two = Counter("super")
print(counter_one.subtract(counter_two))


print(counter_one)