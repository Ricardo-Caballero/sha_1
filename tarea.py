
'''
En esta primera parte lo que hacemos es ingresar un texto y convertirlo a su valor en binario
'''
print("-------------------------------------------------------------------------------------------------------")
print("------------------------------WELCOME YOU ARE INTO SHA-1-----------------------------------------------")
print("--------------------------------------------------------------------------------------------------------")
print("------------------------------FOLLOW THE INSTRUCTIONS---------------------------------------------------")

print("Aqui empieza el programa")
print("")

palabra = input("Ingresa una palabra para SHA-1:  ")# ingresa el texto a cifrar
print("")
p_binario = [format(ord(c),'08b') for c in palabra]# es una lista que tiene las funciones format y ord que obtiene los valores ASCII # y los convierte a binario
cadena_binaria = ''.join(p_binario)# guarda el número binario dentro de una nueva variable
print("Palabra o texto ingresado:  ", palabra)
print("Representación en Binario : ", cadena_binaria)
print("Total de bits:               ", len(cadena_binaria) )#IMPRIMIMOS EL LEN DE NUESTRO DICCIONARIO


"""
Paso #2
#vamos a crear una lista y vamos a guardar el valor de cadena_binaria
"""
new_arreglo = []#Creamos una lista en la cual vamos a guardar la representación en binario de las 448 caracteres
for cont in cadena_binaria:# ingresamos cada uno de los elementos del diccionario "cadena_binaria" a una nueva lista
    new_arreglo.append(cont)


longiTudPalabra = len(new_arreglo)
print(new_arreglo)# Imprimimos el nuevo arreglo

print("")
new_arreglo.append("1")# Agregamos un 1 al final del arreglo
print("Se le agrega un bit encendido al final de nuestro mensaje o palabra original")# imprimimos el len para verificar que sean 32 bit
print("Nevo Total:  ",len(new_arreglo))
'''
Creamos una función en la cual rrellenamos la lista hasta acompletar a 448 elementos 
'''

print("")
print("")
def rellenar():
    falta = len(new_arreglo)
    print("Paso completado  ")
    while falta < 448:
        new_arreglo.append("0")
        #print(falta)
        falta = falta + 1


#vamos a agregar un 1 al final del número binario que se forma con el mensaje (HOLA "EJEMPLO")

'''
En esta condicional lo que hacemos es establecer que si el arreglo tiene menos de 449 elementos llamamos 
la función rellenar, tomar en cuenta que contamos el indice 0
'''
if (len(new_arreglo) < 448):
    print("Rellenar a 448 bit")
    rellenar()

print(new_arreglo),print(""),print("")


"""
AHORA VAMOS HACER QUE LOS CARÁCTERES LLEGEN A 512
Y ADEMÁS QUE AL FINAL DE LOS 512 BIT SE REPRESENTE EN BITS EL NÚMERO DE NUESTRO MENSAJE

Es decir si nuestro mensaje es de 32 carácteres, debemos representar
el 32 usando los últimos 64 bits que nos hacen falta
"""

total = 512
print("tenemos que completar a ",total)
real = len(new_arreglo)
print(real, " ES LA CANTIDAD QUE TENEMOS AHORA")
introducir = total - real
print("PARA LLEGAR A ESA CANTIDAD DEBEMOS INTRODUCIR : ", introducir, " BIT MÁS INCLUYENDO LA LONGIDTUD DE NUESTRA PALABRA")
print(longiTudPalabra," es es el valor que debemos convertir en 64 bits")
print(""),print("")
'''
Vamos a crear una función para convertir de decimal a biarios para poder completar
a los 512 números binarios
'''

def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario

decimal = longiTudPalabra
#decimal = int(input("Ingresa un número decimal: "))
binario = decimal_a_binario(decimal)
print(f"El número {decimal} es {binario} en binario")
print(len(binario)," es la longitud del numero 32 en binario")
long = len(binario)
print(""),print("")

#VAMOS A CREAR LA PARTE QUE SE VA A ENCARGAR DE RELLNAR O COMPLETAR A 512 CARACTERES
primerRelleno = introducir - long
print("vamos a rellenar con ", primerRelleno, " bits", " más el ", binario)

#en esta variable vamos a llevar el control de cuanto ceros debemos de ingresar antes de 
# de colocar la representación de la longitud de nuestro mensaje representada en bits 
primeraFase = real + primerRelleno # AQUI TENEMOS HASTA QUE NUMERO DEBEMOS RELLENAR
print("debemos ingresar ",primerRelleno, " ceros antes de ingresar", binario)


while real < primeraFase:
    new_arreglo.append("0")
    real = real + 1

new_leng = len(new_arreglo)
print("ASI SE VEN ACOMPLETADO ")
print(new_arreglo)
print("")
print("ahora son", new_leng, " carácteres")
print("------------------------------------------------------------------------------------------------------")

segundaFase = []
cont = 0
cadena = str(binario)
print(cadena," es la representación de la longitud del mensaje origina.")

for cont in cadena:
    print(":)")
    segundaFase.append(cont)

# EN LA LISTA SEGUNDA FASE GUADAMOS LA LONGITUD DEL MENSAJE Y LO AGREGAMOS AL ARREGLO QUE GUARDA YA LOS 506 bits
new_arreglo.extend(segundaFase)
print(new_arreglo)
test=len(new_arreglo)
print(test,"----> es el total de todas nuestras palabras, usando el mensaje ingresado por el cliente: ",palabra )


'''
VAMOS A EXTRAER LOS ELEMENTOS DE LA LISTA EN GRUPOS DE 32 ELEMENTOS PARA PODER HACER LAS 16 PALABRAS
'''
contador = 0
dieciseisP = [] #Creamos una lista en la cual vamos a guardar las palabras pero ahora van a estar dentro de otra lista
# es decir van ir de 32 en 32 bits dentro de una lista y todas las listas de 32 palabras van ir dentro de una lista final. 
for i in range(0,len(new_arreglo),32):
    grupo = new_arreglo[i:i +32]
    #print("Palabra ",contador,"grupo")
    contador = contador + 1
    dieciseisP.append(grupo)
    

c = 0
for i in dieciseisP:
    print("palabra ",c,i)
    c = c + 1




