#calculator
def calculation():
    x=int(input("enter first number:"))
    y=int(input("enter second number:"))
 
    print ("select operation to perform\n\
+(addition)\n-(subtraction)\n*(multiplication)\n/(division)")
    
    a=input()

    if a=="+":
        result=x+y
        print (result)
        print()
    elif a=="-":
        result=x-y
        print (result)
    elif a=="*":
        result=x*y
        print (result)
    elif a=="/":
        if y!=0:
            result=x/y
            print (result)
            
        else:
            print("change the second number")
            y=int(input("enter second number: "))
            result=x/y
            print (result)
            
    else:
        print ("check the operation you entered")
        
def decision():
    print ("do you want to calculate")
     
    a=int(input("1.Yes\n2.No\n"))
    if a==1:
        calculation()
        decision()
    else:
        quit()


decision()
