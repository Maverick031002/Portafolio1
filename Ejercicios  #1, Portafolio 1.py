#Ejercicios de recursividad (Portafolio 1)

"""
Entradas: Un numero entero positivo
Salidas: Retornar los divisores de num
Restricciones: numeros enteros positivos
"""
def divisores(num): #Nombre de la funcion
    if(isinstance(num,int) and (num>0)): #Validaciones
        return divisoresAux(n,n)
    else:
        return "El número debe ser mayor a cero y positivo"

def divisoresAux(num,counter):   #Funcion Auxiliar
    if (counter==0): #Condicion de parada
        return 0
    else:
        if(num%counter)==0:
            print(counter)
        return divisoresAux(num,counter-1)

#-------------------------------------------------------------------------------------------------------------------------#

"""
Entradas: Los numeros ingresados deben ser enteros positivos
Salidas: Retornar el resultado de la operacion.
Restricciones: num y factor deben ser enteros positivos no se puede utilizar la operacion de multilpicar
"""
def multiplicarRecursivo(num,factor):#Nombre de la funcion
    if(isinstance(num,int)):#Validaciones
        return multiplicarRecursivoAux(num,factor)
    else:
        return "Error: Los valores ingresados deben ser enteros positivos"

def multiplicarRecursivoAux(num,factor):#Funcion de auxiliar
    if(factor==0): #Condicion de parada
        return 0
    else:
        return num+multiplicarRecursivoAux(num,factor-1) #Recurción


#_____________________________________________________________________________________#
"""
Entradas: Los numeros ingresados deben ser enteros positivos
Salidas: Retornar el resultado de la operacion.
Restricciones: divisor y dividendo deben ser enteros positivos no se puede utilizar la operacion de dividir
"""
def divisionRecursivo(divisor,dividendo): #Nombre de la funcion
    if(isinstance(divisor,int) and isinstance(dividendo,int)): #Validaciones
        return divisionRecursivoAux(divisor,dividendo,0)
    else:
        return "Error: Digite un numero entero positivo"

def divisionRecursivoAux(divisor,dividendo,counter): #Funcion Auxiliar
    if(counter<=divisor):
        return 0
    elif(counter>divisor):
        return -1
    else:
        return 1+divisionRecursivoAux(divisor,dividendo,counter+dividendo) #Recurcion

















    
