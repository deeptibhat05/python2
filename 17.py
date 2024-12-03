import datetime as dt
today=dt.datetime.now()
print(today)
y1=today.year
M1=today.month
d1=today.day
h1=today.hour
m1=today.minute
s1=today.second
f1=open("in4.txt","r")
fname1="out_"
fname3="_"+str(y1)+str(M1).zfill(2)+str(d1).zfill(2)+"_"+str(h1).zfill(2)+str(m1).zfill(2)+str(s1).zfill(2)
fname4=".txt"
s1=f1.readline()
list1=s1.split(",")
num1=int(list1[0])
num2=int(list1[1])
for j in range(num1,num2+1,1):
    fname2=str(j)
    fname=fname1+fname2+fname3+fname4
    f2=open(fname,"w")
    for i in range(1,11,1):
        print(j,i,j*i)
        f2.write(str(j)+" "+str(i)+" "+str(j*i))
        f2.write("\n")
    print()
    f2.write("\n")
f2.close()
