s= "hello python"
# writing to a file

# with open("test.txt0", "w") as f:
#     f.write(s)

fp=open("test.txt0", "w")
fp.write(s)
fp.close()


#Reading the file
# with open("test.txt0", "r") as f:
#     s=f.read()
#     print(s)

f = open("test.txt0", "r")
s= f.read()
print(s)
f.close()