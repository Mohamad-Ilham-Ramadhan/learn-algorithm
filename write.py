f = open('content.txt', 'w')
import random
# f.write('[')
for i in range(10000): 
   f.write(str(random.randint(0,10000)) + ' ')
# f.write(']')