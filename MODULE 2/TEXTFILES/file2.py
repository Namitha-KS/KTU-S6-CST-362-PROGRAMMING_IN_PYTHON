f = open("integer.txt",'w')

for i in range(10):
    f.write(str(i)+"\n")


import random
for j in range(50):
    number = random.randint(1,50)
    f.write("RANDOM NUMBER : "+ str(number) + "\n")

f.close()