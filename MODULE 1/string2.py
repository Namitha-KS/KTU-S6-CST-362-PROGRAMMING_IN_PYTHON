string1 = 'HELLO'
string2 = ' WORLD'
# TYPE1
print(string1+string2)
# TYPE2
print(string1,string2)
# TYPE3
print("".join([string1,string2]))
#  TYPE4
print("%s%s"%(string1,string2))
# TYPE5
print("{}{}".format(string1,string2))
# TYPE6
print(f"{string1}{string2}")
print("{string1}{string2}")

greeting = f"THIS IS {string1} {string2} FROM STRING CONCATENATION OF MODULE1"
print(greeting)
