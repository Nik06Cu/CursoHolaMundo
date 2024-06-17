
n=0

while True:
    n = int(input( "Ingrese el número ->"))
    if n !=0:
        break

while True:
    while True:
        op = input("Ingresar operación ->   ")
        if op == "-" or op == "+" or op == "*" or op == "/":
            n2= int(input("Ingrese el número a operar ->"))
            break

    if op == "-":
        Result = n-n2
    elif op == "+":
        Result = n+n2
    elif op == "*":
        Result = n*n2
    elif op == "/":
        Result = n/n2

    print(f"El resultado es:{Result}")

    n=Result

    opc=input("Escriba Salir para terminar ó Seguir para continuar: ")

    if opc.lower() == "salir":
        break