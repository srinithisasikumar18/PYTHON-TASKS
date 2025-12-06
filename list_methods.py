li=[]
num=int(input("Enter the size of the list: "))
for i in range(num):
    val=int(input("Enter the Values: "))
    li.append(val)
options=["1.Insert","2.Delete","3.Sort","4.Reverse","5.Exit"]
while True:
    print(options)
    op=int(input("Enter the Option Number: "))
    if op==1:
        ins_val=int(input("Enter the value to be inserted: "))
        li.append(ins_val)
        print(li)
    elif op==2:
        del_val=int(input("Enter the value to be deleted: "))
        if del_val in li:
            li.remove(del_val)
            print(li)
        else:
            print("No such Value in the list")
    elif op==3:
        li.sort()
        print(li)
    elif op==4:
        li.reverse()
        print(li)
    elif op==5:
        print("exiting the program")
        break
    else:
        print("No such option")
