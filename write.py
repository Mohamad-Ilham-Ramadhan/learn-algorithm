f = open('content.txt', 'w')
f.write('[')
import random
for i in range(10000, -1, -1):
   f.write(str(random.randint(0,100)) + ',')
f.write(']')