from funciones import *
from input import *
from listas import *
import os

bandera = False
bandera_promedios = False

while True:
    print("1. Cargar Notas de alumnos.\n"
      "2. Mostrar estudiantes.\n"
      "3. Calcular promedio estudiantes. \n"
      "4. Mostrar los promedios de forma descendente. \n"
      "5. Materias con mayor promedio general. \n"
      "6. Buscar estudiante por legajo. \n"
      "7. Mostrar veces que se repite una calificacion. \n"
      "8. SALIR")
    opcion = get_int("Ingrese una opcion (1/8) ","ERROR, ingrese una opcion valida",1,8,5)
    match opcion:
        case 1:
            print("CARGANDO NOTAS...")
            cargar_notas(matriz_notas)
            print("NOTAS CARGADAS CON EXITO.")
            bandera = True
        case 2:
            if bandera == True:
                mostrar_estudiantes(array_nombres,matriz_notas,array_generos,array_estados,array_legajos)
            else:
                print("NO SE HAN CARGADO NOTAS TODAVIA.")
        case 3:
            if bandera == True:
                array_promedios = calcular_promedio_estudiantes(matriz_notas)
                print("PROMEDIOS CALCULADOS.")
                mostrar_promedios(array_promedios,array_nombres)
                bandera_promedios = True
            else:
                print("NO SE HAN CARGADO NOTAS TODAVIA.")
        case 4:
            if bandera_promedios == True:
                lista_ordenada = ordenar_lista(array_promedios,"DESC")
                mostrar_promedios(lista_ordenada,array_nombres)
            else:
                print("DEBE CALCULAR LOS PROMEDIOS PRIMERO")
        case 5:
            if bandera == True:
                mostrar_promedio_materias(matriz_notas)
            else:
                print("NO SE HAN CARGADO NOTAS TODAVIA.")
        case 6:
            if bandera == True:
                buscar_estudiante(array_legajos,array_nombres,matriz_notas,array_generos,array_promedios)
            else:
                print("DEBE CALCULAR LOS PROMEDIOS PRIMERO")
        case 7:
            pass
        case 8:
            break
    
    input("Presione una tecla para continuar...")
    os.system("cls")