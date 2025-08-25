#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre= input("Ingrese su nombre ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre_usuario= input("Ingrese su nombre ")
apellido_usuario= input("Ingrese su apellido ")
edad_usuario= input("Ingrese su edad ")
residencia_usuario= input("Ingrese su lugar de residencia ")
print(f"Soy {nombre_usuario} {apellido_usuario}, tengo {edad_usuario} años y vivo en {residencia_usuario}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

circulo_radio= float( input("Ingrese el radio ")) 
area= round(3.1416 * circulo_radio **2)
perimetro= round( 2* 3.1416 * circulo_radio)
print(f"El area del circulo es: {area} y el perimetro es de: {perimetro}")


#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos= float(input("Ingrese la cantidad de segundos "))
horas= round(segundos/ 3600, 2)
print (f"los {segundos} segundos equivalen a {horas} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero_a_multiplicar= int(input("Ingrese un numero entero positivo "))

num_por_0 = numero_a_multiplicar * 0
num_por_1 = numero_a_multiplicar * 1
num_por_2 = numero_a_multiplicar * 2
num_por_3 = numero_a_multiplicar * 3
num_por_4 = numero_a_multiplicar * 4
num_por_5 = numero_a_multiplicar * 5
num_por_6 = numero_a_multiplicar * 6
num_por_7 = numero_a_multiplicar * 7
num_por_8 = numero_a_multiplicar * 8
num_por_9 = numero_a_multiplicar * 9

print(f""" {numero_a_multiplicar} x 0 = {num_por_0}
  {numero_a_multiplicar} x 1 = {num_por_1}
  {numero_a_multiplicar} x 2 = {num_por_2}
  {numero_a_multiplicar} x 3 = {num_por_3}
  {numero_a_multiplicar} x 4 = {num_por_4}
  {numero_a_multiplicar} x 5 = {num_por_5}
  {numero_a_multiplicar} x 6 = {num_por_6}
  {numero_a_multiplicar} x 7 = {num_por_7}
  {numero_a_multiplicar} x 8 = {num_por_8}
  {numero_a_multiplicar} x 9 = {num_por_9} """)

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero_1= float(input("Ingrese un numero que no sea 0 "))
numero_2= float(input("Ingreses segundo numero que no sea 0"))

suma= numero_1 + numero_2
resta= numero_1 - numero_2
division= numero_1 / numero_2 
multiplicacion= numero_1 * numero_2
print(f"""
      El resultado de la suma es: {suma}
      El resultado de la resta es: {resta}
      El resultado de la division es: {division}
      El resultado de la multiplicacion es: {multiplicacion}""")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. 

peso= float(input("Ingrese su peso: "))
altura= float(input("Ingrese su altura: "))
imc= round(peso / altura **2, 2)
print(f"su IMC es de {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. 

grados_celsius= float(input("Ingrese temperatura "))
grados_fahrenheint= round((9/5) * grados_celsius + 32, 2)
print(f"{grados_celsius}°C (grados celsius) equivalen a {grados_fahrenheint}°F (grados fahrenheint)")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

nro_1= float(input("Ingrese el primer numero "))
nro_2= float(input("Ingrese el segundo numero "))
nro_3= float(input("Ingrese el tercer numero "))

suma_3_nros= nro_1 + nro_2 + nro_3
promedio= round(suma_3_nros / 3, 2)
print(f"El promedio de los numeros {nro_1}, {nro_2} y {nro_3} es de {promedio}")
