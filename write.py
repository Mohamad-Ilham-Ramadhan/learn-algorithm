f = open('content.txt', 'w')
f.write('[')
import random
for i in range(0, 5):
   f.write(str(random.randint(1, 100)) + ',')
f.write(']')