with open('myfile.txt', 'w') as f:
    f.write("This is my first file! ")
    f.write("Second line! ")
    f.write("Last line! ")
    f.write("Kishan is Noob noob noob")

with open('myfile.txt','r') as w:
    li=w.read()
    l2=li.split()
    print(l2)
dic={}
for word in l2:
    if word in dic:
        dic[word]=dic[word]+1
    else :
        dic[word]=1
print(str(dic))