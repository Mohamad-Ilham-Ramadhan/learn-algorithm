f = open('content.txt', 'w')
f.write('[')
import random
for i in range(0, 10000):
   limit = 1
   if i < 100: 
      limit = 100
   elif i < 1000: 
      limit = 1000 
   elif i < 3000: 
      limit = 10000
   elif i < 9000: 
      limit = 99999
   else: 
      limit =999999999
   f.write(str(random.randint(1, limit)) + ',')
f.write(']')