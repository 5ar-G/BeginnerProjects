principle=0
rate=0
time=0
is_running = True

#Functions to check if a string is a number.
def is_float(value):
    try:
        float(value)  
        return True   
    except ValueError:
        return False

def is_int(value):
    try:
        float(value)  
        return True   
    except ValueError:
        return False


#Main part
while is_running:

    #Validatind principle
    principle= input("Enter the principle amount: ")

    if is_float(principle):
        principle = float(principle)
        
    else:
        print("Invalid principle. PLEASE TRY AGAIN!")
        exit()

    if principle < 0:
        print("Principle cant't be less than zero!")
        exit()
    

    #Validating rate
    rate= input("Enter the interest rate amount: ")

    if is_float(rate):
        rate = float(rate)
        
    else:
        print("Invalid rate. PLEASE TRY AGAIN!")
        exit()

    if rate < 0:
        print("Rate cant't be less than zero!")
        exit()


    #Validating time
    time= input("Enter the time amount: ")
    
    if is_int(time):
        time = int(time)
    
    else:
        print("Invalid time. PLEASE TRY AGAIN!")
        exit()
    
    if time < 0:
        print("Time cant't be less than zero!")
        exit()

    #Exiting loop
    is_running = False


#Calculating and showing final results
total= principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s is: ${total:.2f}")