dinero = 11000
dinero_perdido = 8000

#if anidados y else if (elif)
if dinero > 10000:
    if dinero - dinero_perdido < 0:
        print("Estas en bancarrota")
    elif dinero - dinero_perdido > 3000:
        print ("Eres rico")
    else:
        print ("Ahorra")
    
    
elif dinero > 1000:
    print("Estás bien economicamente")
    
elif dinero > 500:
    print("Dinero justo")
    
else:
    print("Eres pobre")