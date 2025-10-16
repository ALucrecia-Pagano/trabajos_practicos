#1) Dado el diccionario precios_frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
#Añadir las siguientes frutas con sus respectivos precios: Naranja = 1200, Manzana = 1500, Pera = 2300
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print("Diccionario actualizado", precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas
# Banana = 1330, Manzana = 1700, Melon = 2800.

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800


print("Diccionario actualizado", precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente 
# las frutas sin los precios.

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)






