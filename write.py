f = open('content.txt', 'w')
import random
f.write('[')
for i in range(200): 
   f.write(str(random.randint(0,1000)) + ',')
f.write(']')