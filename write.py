f = open('content.txt', 'w')
f.write('[')
import random
for i in range(0, 10000):
   f.write(str(i) + ',')
f.write(']')