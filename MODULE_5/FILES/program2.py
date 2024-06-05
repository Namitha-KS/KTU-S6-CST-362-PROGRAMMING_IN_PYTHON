'''WRITE A PROGRAM TO READ THE CONTENTS OF A FILE AND WRITE INTO ANOTHER FILE AFTER DELETING THE DUPLICATES'''


f1 = open('example.txt','r')
f2 = open('test.txt','w')
readfile = f1.read()
words = readfile.split()

words_to_remove = set()
for word1 in words:
    for word2 in words:
        if (word1 == word2):
            print(word2)
            words_to_remove.add(word2)
            
for word in readfile:
    if word in words_to_remove:
        readfile = readfile.replace(word,'')
    
f2.write(readfile)
