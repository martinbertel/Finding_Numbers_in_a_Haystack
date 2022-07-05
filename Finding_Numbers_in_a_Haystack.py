import re
hand = open('regex_sum_1484659.txt')
x = list()
for line in hand:
    y = re.findall('[0-9]+',line)
    x = x+y

sum = 0
for z in x:
    sum = sum + int(z)

print(sum)

#shorter_way

import re
print(sum([int(i) for i in (re.findall('[0-9]+',(open('regex_sum_1484659.txt','r').read())))]))

