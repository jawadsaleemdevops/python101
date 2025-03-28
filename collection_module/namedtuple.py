from collections import namedtuple

Parts = namedtuple("Parts", "id_num desc cost amount")
auto_parts = Parts(id_num="1234", desc="Ford Engine", cost=1200.00, amount=10)
print(auto_parts.id_num)



# using Dictionary
from collections import namedtuple

Parts = {'id_num':'1234', 'desc':'Ford Engine',
     'cost':1200.00, 'amount':10}
parts = namedtuple('Parts', Parts.keys())(**Parts)
print (parts)



# above function split into two parts
from collections import namedtuple

Parts = {'id_num':'1234', 'desc':'Ford Engine',
     'cost':1200.00, 'amount':10}
parts = namedtuple('Parts', Parts.keys())
print (parts)


auto_parts = parts(**Parts)
print (auto_parts)
