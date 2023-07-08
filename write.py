f = open('content.txt', 'w')
import random
f.write('[')
for i in range(15): 
   f.write(str(random.randint(-10,20)) + ',')
f.write(']')