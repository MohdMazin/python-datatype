
a = []  # Define 'a' outside the functions

def create_list():
    return []

def create_tuple():
    return ()

def create_dictionary():
    return {}

print("L = List\nT = Tuple\nD = Dictionary")
ask_1 = input("Enter the type of datatype you want to work On (L/T/D): ").upper()

if ask_1 == "L":
    a = create_list()
elif ask_1 == "T":
    a = create_tuple()
elif ask_1 == "D":
    a = create_dictionary()
else:
    print("Enter a correct type of Datatype please!")
    exit()

print(f"The Datatype you selected: {ask_1}")

if ask_1 == "L":
    print("Datatype List is used!:- []")
    element1 = int(input("Enter the number of elements you want in the list: "))
    for _ in range(element1):
        data1 = input("Enter the Data you want to Enter (String Format will be used): ")
        a.append(data1)
    print(f"Your Datatype {ask_1}:-",a)

print("Updated Data:", a)

if ask_1 == "T":
    print("Datatype Tuple is used")
    element1 = int(input("Enter the number of elements you want in the list: "))
    for _ in range(element1):
        data1 = input("Enter the Data you want to Enter (String Format will be used): ")
        a += (data1,)
    print(f"Your Datatype {ask_1}:-",a)

if ask_1 == "D":
    print("The Datatype used here is dictionary!")
    element1 = int(input("Enter the number of elements you want in the Datatype:-"))
    for _ in range(element1):  
        key = input("Enter Any Kind of key:-")
        value = input("Enter Any Kind of Value:-")
        a[key] = value
    print(f"Your Datatype {ask_1}:-",a)

    
        

 

    
        

        


        
    
    
    



