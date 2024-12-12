import Pyro4

#Prompt the  user to enter the URI of the Server
uri=input("Enter the URI of the Server : ")

#Connect to the Server
calc=Pyro4.Proxy(uri)

#Function to Perform Addition
def perform_addition():
    x=float(input("Enter the First Number : "))
    y=float(input("Enter the Second Number : "))
    result=calc.add(x,y)
    print("Result of Addition : ",result)

#Function to Perform Subtraction
def perform_subtraction():
    x=float(input("Enter the First Number : "))
    y=float(input("Enter the Second Number : "))
    result=calc.subtract(x,y)
    print("Result of Addition : ",result)

#Interactive Menu
while True:
    print("\n Choose an Operation :")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")
    choice=input("Enter Your Choice (1/2/3): ")

    if choice=="1":
        perform_addition()
    elif choice=="2":
        perform_subtraction()
    elif choice=="3":
        print("Exiting Client.")
        break
    else:
        print("Invalid Choice. Please enter 1 , 2 or 3.")