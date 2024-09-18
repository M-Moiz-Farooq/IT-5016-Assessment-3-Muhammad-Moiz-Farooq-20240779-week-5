idcount=0
uniqueid=idcount+1
ids=[] # store as tuple instead of string
def collectuserdata():
    global uniqueid
    #apply condition
    while True:
        name=input("enter your name(enter done to exit):")
        if name.lower()=="done":
                break
    #prompt user to input name,age,email
       
        age=input(F"Hi {name} can you please enter your age:")
        email=input(F"Hi {name} can we please have your email too? : ")
        print(F"Hi {name} your unique id is: {uniqueid}")
        ids.append((name,uniqueid))
        uniqueid += 1

    print("\nList of unique ids created:")
    for name,uniqueid in ids:
         print(F"{name}:{uniqueid}")    
      

def shoppinglist():
     #prompt user to enter item name
    total=0
    shoppinglistitemsp=[] 
    while True:
        itemname=input("enter item name:")
        if itemname.lower()=="done":
             break
        itemprice=float(input("enter price of item:"))
        total+=itemprice
        shoppinglistitemsp.append((itemname,itemprice))
    print("\nShopping list:")
    for itemnames,itemprice in shoppinglistitemsp: 
         print(F"{itemnames}:{itemprice:.2f}")
    print(F"Your total is : ${total:.2f}")        
    #requesting sumary
    print("\nRequesting Summary:")
    if total<150:
         print("Category:Low")
         print("Proceed with standard routine")
    else:
         print("Category:High")
         print("Review for potential discount")     


collectuserdata() 
shoppinglist()    