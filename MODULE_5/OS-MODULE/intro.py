import os

os.mkdir('TEST')
os.rename('file.txt','test.txt')
# os.remove('test.txt')
# os.rmdir('TEST')

path = os.path.join('directory','file.txt')
print(path)

print(os.path.exists('file.txt'))
print(os.path.isdir('directory'))

# for dirpath, dirnames, filenames in os.walk('PROGRAMS\MODULE_5\OS-MODULE'):
#     print(f"Directory: {dirpath}")
#     for dirname in dirnames:
#         print(f"Subdirectory: {dirname}")
#     for filename in filenames:
#         print(f"File: {filename}")
        
current = os.getcwd()
files = os.listdir(current)
for filename in files:
    print(filename)