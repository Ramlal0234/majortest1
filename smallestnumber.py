num=int(input("Enter size of list:"))

list1=[int(ele) for ele in input("Enter list element:").split()]
list1.sort()
max=list1[-1]
for i in range(max):
    if((i+1) not in list1):
        print("missing number is :",i+1)    
        exit()
print("Missing first natural number is :",max+1)  