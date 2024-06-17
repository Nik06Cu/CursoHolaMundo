
def suma(*numeros): #El argumento que definimos en la
                    # función permite pasarle cualquier cantidad de argumentos de un mismo tipo 
    Sum=0
    for i in numeros:
        Sum+=i
    print(Sum)

suma(1,2,3,4)
print("-"*50)
suma(4,23,56,34,23,12)
print("-"*50)
suma(4,6)