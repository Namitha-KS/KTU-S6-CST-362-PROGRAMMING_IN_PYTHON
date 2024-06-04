f = open("textfile.txt",'r')
j=0
x = 0
print("WORDS WITH FOUR LETTERS")
for i in f:
    j+=1
    words = i.strip().split()
    # print(words)
    for word in words:
        if (len(word)==4):
            print(word)
            x+=1
print("NUMBER OF LINES IN THE FILE ", j)

print("TOTAL NUMBER OF WORDS WITH FOUR LETTERS ARE : ",x)

