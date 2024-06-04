f = open("integer.txt",'r')

sum = 0
for line in f:
  line = line.strip()
  number = int(line)
  sum += number
f.close()

print(sum)
# Open a new file in append mode to store the sum
g = open("integer.txt", 'a')  # 'a' for append mode
g.write("\n"+str(sum))
g.close()
