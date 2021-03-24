def menu():
    print("Que operación desea realizar")
    print("  (1) ¿Quieres pasar numeros flotantes a enteros positivos?")
    print("  (2) ¿Quieres contar los dígitos de un número flotante?")
    print("  (3) ¿Devolver un número según su indice?")
    print("  (4) ¿Devolver un numero segun indices?")
    print("\n")
    print("\nCual opcion selecciona:")

    opcion=int(input())

    if opcion == 1:
        num = float(input("Digite un número flotante: "))
        return corrimientoAEntero(num)
    
    elif opcion == 2:
        num = float(input("Digite un numero flotante: "))
        return contarDigitosFlotantes(num)

    elif opcion == 3:
        num = int(input("Digite el numero"))
        i = int(input("Digite el indice"))
        return indiceNumero(num,i)
    
    elif opcion ==4:
        num=int(input("Digite un numero"))
        exponente1=int(input("Digite el Primer Exponente"))
        exponente2=int(input("Digite el Segundo Exponente"))
        return cortarNumero(num,exponente1,exponente2)

#----------------------------------------------------------------------------------------------------------#
"""
Entradas: Un parametro llamado num
Salidas: Pasar numeros flotantes a enteros
Restricciones: El numero debe ser un flotante
"""
def corrimientoAEntero(num):
    if(isinstance(num,float) and num>0):
        return corrimientoAEnteroAux(num)
    else:
        return "El número debe ser positivo"

def corrimientoAEnteroAux(num):
    if(isinstance(num,float)):
        num=num%10**10*100000
        num=int(num)
        return corrimientoAEnteroAux(num)
    elif(num%10==0):
        return corrimientoAEnteroAux(num//10)
    else:
        return num
#---------------------------------------------------------------------------------------------------------#
"""
Entradas: Un parámetro flotante positivo
Salidas: Largo de un numero flotante
Restricciones: El numero debe de ser un flotante mayor a cero
"""
def contarDigitosFlotantes(num):
    if(isinstance(num,float) ):
        if num<0:
            resultado=num*-1
            resultado=resultado%10**10*100000
            resultado=int(resultado)
            return pasarNegativo(resultado)
        else:
            num=(num%10**10*100000)
            num=int(num)
            return contarFlotantesAux(num)
    else:
        return "El dígito que ingresó debe ser un flotante positivo"

def contarFlotantesAux(num):
    if(num%10==0):
        return contarFlotantesAux(num//10)
    elif(num < 10):
        return 1
    else:
        return 1+contarFlotantesAux(num//10)

def pasarNegativo(resultado):
    if resultado<10:
        return 1
    elif resultado%10==0:
        return contarFlotantesAux(resultado//10)
    else:
        1+contarFlotantesAux(resultado//10)
    




    
#-------------------------------------------------------------------------------------------------------#
"""
Entradas: Dos parametros llamados "num" y "i"
Salidas: Pasar numeros flotantes a enteros
Restricciones: "num" y "i" deben ser enteros positivos
"""
def indiceNumero(num,i):
    if(isinstance(num,int)and num >= 0):
        if(isinstance(i,int)and i >= 0):
            return indiceNumeroAux(num,i)
        else:
            return "El indice debe ser un numero entero positivo"
    else:
        return "digite un numero entero positivo"

def indiceNumeroAux(num,exponente):
    if(exponente >= 0):
        num=str(num)
        print(int(num[exponente]))
    else:
        return "El numero debe de ser un entero positivo"

#---------------------------------------------------------------------------------------------------------#
"""
Entradas: Tres parametros llamados num, exponente1, exponente2
Salidas: Pasar numeros flotantes a enteros
Restricciones: num, exponente1, exponente2 deben ser enteros positivos
"""    
def cortarNumero(num,exponente1, exponente2):
    if(isinstance(num,int)and num >= 0):
        if(isinstance(exponente1,int)):
            if (isinstance(exponente2,int)):
                return cortarNumeroAux(num,exponente1, exponente2)
            else:
                return "exponente2 debe ser un numero entero positivo"
        else:
             return "exponente1 un numero entero positivo"
    else:
        return "digite un numero entero positivo"

def cortarNumeroAux(num,exp1,exp2):
    if(exp1 >= 0) and (exp2 >= 0):
        num=str(num)
        print(int(num[exp1])*10+(int(num[exp2])))
    else:
        return "Error"








