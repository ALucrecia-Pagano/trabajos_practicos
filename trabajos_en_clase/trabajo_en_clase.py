#Trabajo practico en clase: me apolle mucho de internet logre comprender bastante bien
#si bien fue complejo (mucho para mi) aprendi muchos metodos para resolver!
       #VALIDACION DE FECHA#
fecha_actual= input("Ingrese la fecha en formato dia, DD/MM")
if "," in fecha_actual:
   partes_de_la_fecha= fecha_actual.split(",")
   if len(partes_de_la_fecha) == 2:
      dia_semana= partes_de_la_fecha[0].strip().lower()
      partes= partes_de_la_fecha[1].strip()
      if "/" in partes:
          partes_fecha= partes.split("/")
          if len(partes_fecha) == 2 and partes_fecha[0].isdigit() and partes_fecha[1].isdigit():
             dia= int(partes_fecha[0])
             mes= int(partes_fecha[1])
             if dia >= 1 and dia <= 31 and mes >=1 and mes <=12:
                            #-----LUNES-----#
                if dia_semana== "lunes": 
                   print("Hoy toca nive inicial")
                   examenes= input("Hubo examenes hoy? (si/no): ").strip().lower()
                   if examenes== "si":
                      aprobados= int(input("Ingrses el total de aprovados: "))
                      desaprovados= int(input("Ingrese total de desaprovados: "))
                      total= aprobados + desaprovados
                      if total >0:
                         porcentaje_aprobados= (aprobados/ total) *100 
                         print("Porcentaje de aprobados es",round(porcentaje_aprobados, 2),"%")
                      else:
                         print("No se registraron alumnos")
                                #------MARTES------#
                elif dia_semana == "martes":
                   print("Hoy toca nivel intermedio")
                   examenes= input("Hubo examenes hoy? (si/no): ").strip().lower()
                   if examenes == "si":
                      aprobados= int(input("Ingrese total de aprobados: "))
                      desaprovados= int(input("Ingrese total de desaprobados "))
                      total= aprobados + desaprovados
                      if total >0:
                         porcentaje_aprobados= (aprobados/ total) *100 
                         print("Porcentaje de aprobados es",round(porcentaje_aprobados, 2),"%")
                      else:
                         print("No se registraron alumnos")
                                  #-----MIERCOLES------#
                elif dia_semana== "miercoles":
                   print("Hoy toca nivel avanzado")
                   examenes= int(input("Hubo examen hoy?: (si/no): ")).strip().lower()
                   if examenes== "si":
                      aprobados= int(input("Ingrese total de aprobados: "))
                      desaprovados= int(input("Ingrese total de desaprobados: "))
                      total= aprobados + desaprovados
                      if total > 0:
                          porcentaje_aprobados= (aprobados/ total) *100 
                          print("Porcentaje de aprobados es",round(porcentaje_aprobados, 2),"%")
                      else:
                         print("No se registraron alumnos")
                               #-----JUEVES-----#
                elif dia_semana== "jueves":
                   print("Hoy toca cclase hablada")
                   asistencia= float(input("Ingrese el porcentaje de asistencia: "))
                   if asistencia >= 50:
                      print("Asistio la mayoria ")
                   else:
                      print("No asisti la mayoria")
                            #----- VIERNES-----#
                elif dia_semana== "viernes" :
                   print("Hoy toca ingles para viajeros")
                   if dia == 1 and (mes == 1 or mes == 7):
                      print("Comienzo nuevo ciclo")
                      alumnos= int(input("Ingrese cantidad de alumnos"))
                      arancel= float(input("Ingrese el arancel por alumno: "))
                      ingreso_total= alumnos*arancel
                      print("El ingreso total es de: $",ingreso_total)
                   else:
                      print("Dia de la semana incorrecto")
                else:
                   print("Error: dia o mes invalidos")
             else: 
                print("Error la fecha debe ser numerica DD/MM")
          else: 
             print("Error falta / en la fecha")
      else: 
         print("Error falta , entre dia y fecha")
   else: 
      print("Error, debe ser dia, DD/MM")









         
      