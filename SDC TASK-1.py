#SDC TASK-1
# To cover the conepts of Data types,varibales,operators and program constructs
# here is my TASK 1 "Employee Management System"
#Input from user is to be collected,based on that the bonus and tax amount will be calculated.

name=str(input("Enter Employee's name: "))
id=input("Enter Employee's ID: ")
des=input("Enter Employee's Designation: ")
sal=int(input("Enter Employee's Salaary: "))
rat=float(input("Enter Employee's perfomance rating: "))

print(name,"\n",id,"\n",des,"\n",rat,"\n",sal,"\n" )

if(rat>=4.5):
    s1=sal*0.2
    print("The salary with bonus is ",sal+s1 )
elif(sal>=3.5 and sal<=4.4):
    s2=sal*0.1
    print("The salary with bonus is ",sal+s2)
else:
    print("Perfom better to earn with more rating and bonus")

if(sal>=1000000):
    s3=sal*0.2
    print("Tax to be paid is : ",sal+s3)
elif(sal>=500000 and sal<=1000000):
    s4=sal*0.1
    print("Tax to be paid is : ",sal+s4)
else:
    print("No tax to be paid your salary is less than 500000!")


