#SDC-3
#Here come's my task-3 where I'm supposed to design a Online Menu card (whichupdates the food items availbable )of a Hotel using
#any of the collections(Lists,tuples,dictionary,sets)

print("Welcome to Hotel Datracrunch\n")
di={}
meal=int(input("Enter which meal to be updated (1 for breakfast,2 for lunch,3 for dinner, 4 for beverages,5 for desserts,6 for snacks) : "))
def bf():
    n=int(input("Enter Number of food items in Menu : "))
    for i in range (n):
        ke=input("Enter the food item : ")
        pp=input("Enter price of the food item : ")
        di[ke]=pp    
    print("The Food Items available for Breakfast are :",di)
def lu():
    n=int(input("Enter Number of food items in Menu : "))
    for i in range (n):
        ke=input("Enter the food item : ")
        pp=input("Enter price of the food item : ")
        di[ke]=pp    
    print("The Food Items available for lunch are :",di)
def din():
    n=int(input("Enter Number of food items in Menu : "))
    for i in range (n):
        ke=input("Enter the food item : ")
        pp=input("Enter price of the food item : ")
        di[ke]=pp    
    print("The Food Items available for Dinner are :",di)
def be():
    n=int(input("Enter Number of food items in Menu : "))
    for i in range (n):
        ke=input("Enter the food item : ")
        pp=input("Enter price of the food item : ")
        di[ke]=pp    
    print("The Beverages available  are :",di)
def de():
    n=int(input("Enter Number of food items in Menu : "))
    for i in range (n):
        ke=input("Enter the food item : ")
        pp=input("Enter price of the food item : ")
        di[ke]=pp    
    print("The Desserts available  are :",di)
def sc():
    n=int(input("Enter Number of food items in Menu : "))
    for i in range (n):
        ke=input("Enter the food item : ")
        pp=input("Enter price of the food item : ")
        di[ke]=pp    
    print("The Snacks available  are :",di)
if meal==1:
    bf()
elif meal==2:
    lu()
elif meal==3:
    din()
elif meal==4:
    be()
elif meal==5:
    de()
elif meal==6:
    sc()
else:
    print("Enter valid Option!")
print("Happy Crunching - With LOVE Hotel DatraCrunch")
