f = open('content.txt', 'w')
import random
f.write('[')
for i in range(20): 
   f.write(str(random.randint(0,100)) + ',')
f.write(']')