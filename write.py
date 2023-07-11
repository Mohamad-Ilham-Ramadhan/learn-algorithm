f = open('content.txt', 'w')
import random
f.write('[')
for i in range(11): 
   f.write(str(random.randint(-5,10)) + ',')
f.write(']')