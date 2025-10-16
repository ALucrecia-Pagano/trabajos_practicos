#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ('Lunes', '9:00'): 'Reunión con equipo',
    ('Jueves', '14:00'): 'Clase de programación',
    ('Viernes', '18:00'): 'Gimnasio'
}

dia = input("Ingrese el dia ")
hora = input("Ingrese la hora (formato HH:MM): ")

evento = agenda.get((dia, hora), "No hay eventos en ese horario.")
print(evento)