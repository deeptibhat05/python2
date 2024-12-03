f1=open("inconvert1.txt")
f2=open("out1.txt","w")

for i in range(0,3,1):
    
    s1=f1.readline().replace("\n","")
    list1=s1.split(" ")
    
    lhs_value=int(list1[0])
    lhs_units=list1[1]
    equals=list1[2]
    rhs_value=int(list1[3])
    rhs_units=list1[4]

    info1=str(1)+lhs_units+equals+str(rhs_value/lhs_value)+rhs_units
    info2=str(1)+rhs_units+equals+str(lhs_value/rhs_value)+lhs_units
    print(info1)
    print(info2)
    f2.write(info1+"\n")
    f2.write(info2+"\n")
f2.close()
