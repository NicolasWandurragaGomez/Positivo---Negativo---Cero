# Programa para verificar si un numero es negativo positivo o cero

# imput

X= int(input("digite el numero: "))

# processing

if X > 0:
    RTA= "Positivo"

elif X== 0:
    RTA= " El numero es neutro"

else:
    RTA= "Negativo"

# output
    
print("el numero",X," es ",RTA)