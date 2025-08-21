x=input("Enter text to write in the file: ")

a=open("output.txt","w")
b=a.write(x+"\n")
print("Data Successfully Written")
a.close()


y=input("Enter additional test: ")

c=open("output.txt","a")
d=c.write(y)
print("Data Successfully Written")
c.close()

print(" ")

print("Final content:- ")
z=open("output.txt","r")
print(z.read())

#It was hard