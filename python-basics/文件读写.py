file1 = open("123.txt","r")
file2 = open("456.txt","w")

words = file1.read()

for a in words:
    if a >= "a" and a <="z" or a >= "A" and a <="Z":
      file2.write(a)
file1.close()
file2.close()
