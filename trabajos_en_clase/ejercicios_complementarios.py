#1. Crea una variable llamada "numero1" y asígnale un número entero de tu elección. 
#2. No borres la variable número uno y crea una variable llamada "numero2" asignándole 
#un número decimal de tu elección. 
#3. Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2". 
#4. Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para 
#multiplicación y otra para división. Imprime estas variables.

numero1= 4
numero2= 2.5
suma= numero1 + numero2
resta= numero1 - numero2
multiplicacion= numero1 * numero2
division= numero1 / numero2

print("suma: ", suma)
print("resta: ", resta)
print("multiplicacion: ", multiplicacion)
print("division: ", division)

#5. Crea una variable llamada "nombre" y asígnale tu nombre como valor. 
#6. Crea una variable llamada "precio" y asígnale un valor decimal que represente el 
#precio de un artículo ficticio. 
#7. Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale 
#un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le 
#quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al 
#100% y el valor 0 al 0%. 
#8. Ahora, intenta calcular el precio final aplicando el descuento al precio original y 
#almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que 
#aplicar la lógica de matemáticas. 

nombre= "Amanda"
precio= 250.8
descuento= 62.7
precio_final= precio - descuento

#9. Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu 
#elección. Qué sea un string. 
#10. Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas 
#a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de 
#Python. 
#11. Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y 
#conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo 
#mismo. 

cadena= "Guarel te amo"
longitud= len(cadena)
precio= int(2.9)

#12. Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas 
#en una tercera variable llamada "nombre_completo", el nombre y el apellido con un 
#espacio entre medio. Puedes usar libremente la forma de concatenación que quieras. 
#13. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10. 
#14. Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y 
#centímetros. Por ejemplo: 1.83.  Multiplícala por 4 y luego divídela en 3. 

nombre= "Gael "
apellido= "Gonzalez"
nombre_completo= nombre+apellido 
edad= 29 + 10 - 5
altura= (1.61 * 4) / 3

#15. Crea una variable que contenga tu nombre completamente en mayúsculas. Después 
#transfórmalo todo en minúsculas con algún método o función de Python. 
#16. Por último, con la variable con el nombre en mayúsculas, aplica un método parecido 
#para que se transforme todo en minúsculas excepto la primera letra. 

nombre_mayuscula= "AMANDA"
minuscula_nombre= nombre_mayuscula.lower()
primer_letra_mayuscula= nombre_mayuscula.capitalize()
