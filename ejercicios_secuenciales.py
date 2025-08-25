#Calculadora de propinas en un restaurante 
#Un restaurante quiere ayudar a sus clientes a calcular cuánto dejar de propina según el 
#monto de la cuenta. 
#El programa debe: 
#✓ Pedir al usuario el monto total de la cuenta. 
#✓ Calcular la propina sugerida al 10%. 
#✓ Calcular la propina sugerida al 15%. 
#✓ Calcular el total a pagar en ambos casos (cuenta + propina). 
#✓ Mostrar todos los resultados en pantalla. 
#Ejemplo de ejecución 
#Ingrese el monto de la cuenta: 3500 
#Propina sugerida (10%): 350.0 
#Total a pagar (10%): 3850.0 
#Propina sugerida (15%): 525.0 
#Total a pagar (15%): 4025.0 

total_cuenta= float(input("Ingrese el total de su cuenta: "))
prop_10= total_cuenta *0.10
prop_15= total_cuenta* 0.15
print(f"""Propina sugerida (10%): {prop_10} 
          Total a pagar (10%) {total_cuenta + prop_10}
          Propina sugerida (15%): {prop_15}
          Total a pagar (15%): {total_cuenta + prop_15}""")