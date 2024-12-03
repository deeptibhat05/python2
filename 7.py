def calc1(num1,num2):
    sum1=num1+num2
    dif1=num1-num2
    mul1=num1*num2
    div1=num1/num2
    div2=num1//num2
    rem1=num1%num2
    exp1=num1**num2
    s2=str(sum1)+" "+str(dif1)+" "+str(mul1)+" "+str(div1)
    print(s2)
f1=open("in2.txt","r")
s1=f1.readline()
list1=s1.split(",")
num1=int(list1[0])
num2=int(list1[1])
calc1(num1,num2)
