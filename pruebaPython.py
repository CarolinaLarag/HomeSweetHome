def multiplicar (valor1,valor2):
    total = valor1 * valor2
    print (total)
    print ("esto es sin retorno")

def dividir (valor1,valor2):
    total = valor1 / valor2
    return total

#main
valor1=10
valor2=5
multiplicar(valor1,valor2)
print (dividir(valor1,valor2))
print (" // este del retorno debe llamarse con un print //")

valor = 8

if valor > 0:
    print ("mayor a 0")
elif valor == 0:
    print("vale 0")
else:
    print("Menor a 0")


nombre = "juan"
genero= "M"

if nombre == "juan":
    if genero == "S":
        print ("Juan usted es hombre")
    else:
        print("Juan usted no es hombre")
else:
    print ("usted no es juan")

numero= 0
while (numero <= 10):
    print ("numero :", numero)
    numero = numero + 1



valida = True 

while valida == True:
    print ("1)Ingresar")
    print ("2)Mostrar")
    print ("3)Salir")

    opcion = int(input())
    
    if opcion ==1:
        print ("Ingresando")
    elif opcion ==2:
        print ("Listando")
    elif opcion ==3:
        valida= False
        print ("Saliendo")
    else:
        print ("Opcion Inválida")



