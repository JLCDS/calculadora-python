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
    try:
        option = int (input("opcion: "))
        if (option == 1):
            suma1 = int (input ("ingrese el primer numero: "))
            suma2 = int (input ("ingrese el segundo numero: "))
            print ("la suma es: ", suma1 + suma2)
        elif (option == 2):
            resta1 = int (input ("ingrese el primer numero: "))
            resta2 = int (input ("ingrese el segundo numero: "))
            print ("la resta es: ", resta1 - resta2)
        elif (option == 3):
            multi1 = int (input ("ingrese el primer numero: "))
            multi2 = int (input ("ingrese el segundo numero: "))
            print ("la multiplicacion es: ", multi1 * multi2) 
        elif (option == 4):
            div1 = int (input ("ingrese el primer numero: "))
            div2 = int (input ("ingrese el segundo numero: "))
            try:
                print ("la division es: ", div1 / div2)
            except ZeroDivisionError:
                print ("no se puede dividir por cero")

        elif (option == 5):
            fin = True
        else:
            print ("opcion invalida")
    except ValueError:
        print ("Error debe ingresar un numero")