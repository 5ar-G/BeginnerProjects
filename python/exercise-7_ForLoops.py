'''import time
seconds =int(input("Enter seconds: "))

for x in range(seconds, 0, -1) :
    print(x)
    time.sleep(1)

print("Time is up!!")
'''

'''

import time
seconds =int(input("Enter seconds: "))

for x in reversed(range(seconds)) :
    print(x)
    time.sleep(1)

print("Time is up!!")'''



import time
seconds =int(input("Enter seconds: "))

for x in range(seconds, 0 , -1) :
    if x==2:
        continue
    else:
        
        print(x)
    time.sleep(1)

print("Time is up!!")
