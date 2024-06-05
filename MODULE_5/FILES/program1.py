#  WRITE A PROGRAM TO FIND THE LONGEST WORD IN THE FILE

f = open('example.txt','r')
longest_word = ''
length = 0
for line in f:
    words = line.split()
    for word in words:
        if len(word)>length:
            length = len(word)
            longest_word = word
print(f"LONGEST WORD : {longest_word}")