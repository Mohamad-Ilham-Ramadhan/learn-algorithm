f = open('content.txt', 'w')
import random
f.write('[')
for i in range(5): 
   f.write(str(random.randint(0,10)) + ',')
f.write(']')