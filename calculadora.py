fin = False
print ("""
===calculadora===
Menu Principal  -> elija una opcion 
\n 1. Suma  
\n 2. Resta
\n 3. Multiplicacion
\n 4. Division
\n 5. Salir
""")
while not fin:
    option = int (input("opcion: "))
    if (option == 1):
        suma1 = int (input ("ingrese el primer numero: "))
        suma2 = int (input ("ingrese el segundo numero: "))
        print ("la suma es: ", suma1 + suma2)
    elif (option == 2):
        resta1 = int (input ("ingrese el primer numero: "))
        resta2 = int (input ("ingrese el segundo numero: "))
        print ("la resta es: ", resta1 - resta2)
