file=open('for_file.csv','r')
f=file.readlines()
t=0
A=[]
for i in f:
    if t==0:
        i=i[3:len(i)-1]
        t=1
    else:
        i=i[:len(i)-1]
    A.append(list(map(int,i.split(';'))))
print(A)
k=0
for i in A:
    x=max(i)+min(i)
    if len(i)==len(set(i)) and ((x)*3<=(sum(i)-x)*2):
        k+=1
print(k)
