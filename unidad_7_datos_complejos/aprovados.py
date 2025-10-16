#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)

parcial1 = {3, 6, 8, 9, 11, 12, 15, 18, 19, 22, 24}
parcial2 = {1, 4, 6, 8, 12,14, 15, 19, 22, 25, 26}

ambos = parcial1 & parcial2
solo_en_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_en_uno)
print("Aprobaron al menos uno:", al_menos_uno)