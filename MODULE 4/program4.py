'''Write a program that opens a
file and writes "Hello Good moring" to it. Handle exceptions
that can be generated during I/O operations'''

try:
    f = open("open.txt",'w')
    f.write("Hello Good morning")
    f.close()
    
except IOError as e:
    print(f"ERROR IN OPENING THE FILE {f}")