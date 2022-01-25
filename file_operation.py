# f = open("text.txt",'r',encoding ='utf-8' )
# f.read()

# f.close()

# with open("test.txt",'w',encoding = 'utf-8') as f:
#    f.write("my first file\n")
#    f.write("This file\n\n")
#    f.write("contains three lines\n")

f = open("test.txt",'r',encoding = 'utf-8')
f.write(''' This is my file and my file name is test.txt 
and it has some valuable contained. ''')
# print(f.read())

# f.seek(0) 
# for line in f:
#     print(line, end = '')