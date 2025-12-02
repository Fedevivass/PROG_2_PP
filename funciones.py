from input import *
import random
def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any)->list:
    """
    Crea una matriz (lista de listas) con un valor inicial en cada celda.

    Parámetros:
    - cantidad_filas (int): Número de filas de la matriz.
    - cantidad_columnas (int): Número de columnas por fila.
    - valor_inicial (any): Valor que se asignará a cada elemento de la matriz.

    Retorna:
    - list: Matriz de tamaño [cantidad_filas x cantidad_columnas] con todos los valores inicializados.
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz


def crear_array(cantidad_elementos: int, valor_inicial: any)->list:
    """
    Crea un array (lista) con una cantidad específica de elementos, todos con el mismo valor inicial.

    Parámetros:
    - cantidad_elementos (int): Cantidad de elementos que tendrá el array.
    - valor_inicial (any): Valor con el que se inicializará cada elemento.

    Retorna:
    - list: Lista de longitud 'cantidad_elementos' con todos los elementos iguales a 'valor_inicial'.
    """
    array = [valor_inicial] * cantidad_elementos
    return array


def cargar_notas(matriz_notas: list) -> bool:
    """
    Carga una matriz con valores aleatorios entre 1 y 10.

    Parámetros:
    matriz_notas : list
        Matriz (lista de listas) donde se almacenarán las notas. 
        Se asume que la matriz ya está creada con las dimensiones deseadas.

    Retorna:
    bool
        Devuelve True si la matriz se cargó correctamente.
        Devuelve False si la matriz está vacía o no es una lista.

    """

    if len(matriz_notas) > 0 and type(matriz_notas) == list:
        for fil in range(len(matriz_notas)):
            for col in range(len(matriz_notas[0])):
                nota = random.randint(1, 10)
                matriz_notas[fil][col] = nota
        retorno = True
    else:
        retorno = False

    return retorno

def cargar_alumno(array_nombres: list,array_generos:list,array_legajos:list)->bool:
    bandera = False
    if len(array_nombres) > 0 and type(array_nombres) == list:
        for i in range(len(array_nombres)):
            nombre = get_string("Ingrese su nombre: ", "ERROR, debe contener letras y espacios ", 15, 3)
            genero = get_string("Ingrese su genero (f|m|x): ", "ERROR, genero incorrecto ",2, 3)
            while genero != "f" and genero != "m" and genero != "x":
                print("GENERO INVALIDO")
                genero = get_string("Ingrese su genero (f|m|x): ", "ERROR, genero incorrecto ",2,3)
            legajo = get_int("Ingrese su legajo: ","ERROR, legajo incorrecto debe tener 6 cifras",99999, 999999, 5)
            array_nombres[i] = nombre
            array_generos[i] = genero
            array_legajos[i] = legajo
        retorno = True
    else:
        retorno = False

    return retorno

def mostrar_matriz(matriz: list)->None:
    """
    Muestra por pantalla el contenido de una matriz en formato tabulado.

    Parámetros:
    - matriz (list): Lista de listas que representa la matriz a mostrar.

    Retorno:
    - None: Solo imprime la matriz, no retorna ningún valor.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end="\t")
        print()


def mostrar_promedios(array: list, array_nombres: list) -> None:
    """
    Muestra en pantalla los promedios de cada estudiante junto con su nombre.

    Recorre dos listas paralelas: una con los nombres de los estudiantes y otra 
    con sus promedios, e imprime cada nombre seguido de su promedio.

    Parámetros:
    array : list
        Lista que contiene los promedios de los estudiantes.

    array_nombres : list
        Lista que contiene los nombres de los estudiantes. Debe tener la misma longitud que 'array'.

    Retorno:
    None
        La función solo imprime los resultados en pantalla y no devuelve ningún valor.
    """
    for i in range(len(array)):
        print(f"{array[i]} promedio {array_nombres[i]}")


def mostrar_estudiante(array_nombres: list, matriz_notas: list, array_generos: list, array_legajos: list, indice_participante: int) -> bool:
    """
    Muestra en pantalla toda la información de un estudiante específico.

    Parámetros:
    array_nombres : list
        Lista que contiene los nombres de los estudiantes.
    matriz_notas : list
        Matriz (lista de listas) con las notas de cada estudiante.
    array_generos : list
        Lista que contiene el género de cada estudiante.
    array_legajos : list
        Lista que contiene el número de legajo de cada estudiante.
    indice_participante : int
        Posición del estudiante en las listas paralelas.

    Retorna:
    bool
        Devuelve True si el estudiante fue encontrado y mostrado correctamente.
        Devuelve False si el índice es inválido (fuera de rango).
    """
    if indice_participante >= len(array_nombres) or indice_participante < 0:
        retorno = False
    else:
        print(f"{'NOMBRE':<20}{'GENERO':<8}{'NOTA 1':<8}{'NOTA 2':<8}{'NOTA 3':<8}{'NOTA 4':<8}{'NOTA 5':<8}{'LEGAJO':<10}")

        print(f"{array_nombres[indice_participante]:<20}"
              f"{array_generos[indice_participante]:<8}"
              f"{matriz_notas[indice_participante][0]:<8}"
              f"{matriz_notas[indice_participante][1]:<8}"
              f"{matriz_notas[indice_participante][2]:<8}"
              f"{matriz_notas[indice_participante][3]:<8}"
              f"{matriz_notas[indice_participante][4]:<8}"
              f"{array_legajos[indice_participante]:<10}")
        retorno = True

    return retorno


def mostrar_estudiantes(array_nombres: list, matriz_notas: list, array_generos: list, array_estados: list, array_legajos: list) -> None:
    """
    Muestra en pantalla la información de todos los estudiantes activos.

    Parámetros:
    array_nombres : list
        Lista con los nombres de los estudiantes.
    matriz_notas : list
        Matriz (lista de listas) con las notas de los estudiantes.
    array_generos : list
        Lista con los géneros de los estudiantes.
    array_estados : list
        Lista que indica el estado de cada estudiante ("0" = inactivo, otro valor = activo).
    array_legajos : list
        Lista con los legajos de los estudiantes.

    Retorna:
    None
        No devuelve ningún valor. Solo imprime la información de los estudiantes activos.
    """
    for i in range(len(array_estados)):
        if array_estados[i] != "0":
            mostrar_estudiante(array_nombres, matriz_notas, array_generos, array_legajos, i)
            print("") 


def sumar_fila(matriz_puntajes: list, indice_fila: int) -> int | float:
    """
    Suma todos los valores numéricos de una fila específica en una matriz.

    Parámetros:
    matriz_puntajes : list
        Matriz (lista de listas) que contiene los puntajes o valores numéricos.
    indice_fila : int
        Índice de la fila que se desea sumar.

    Retorna:
    int | float
        Devuelve la suma total de los valores numéricos de la fila indicada.
    """
    suma_fila = 0
    for col in range(len(matriz_puntajes[0])):
        if type(matriz_puntajes[indice_fila][col]) == int or type(matriz_puntajes[indice_fila][col]) == float:
            suma_fila += matriz_puntajes[indice_fila][col]
    return suma_fila


def sumar_columna(matriz_notas: list, indice_columna: int) -> int | float:
    """
    Suma todos los valores numéricos de una columna específica en una matriz.

    Parámetros:
    matriz_notas : list
        Matriz (lista de listas) que contiene los valores o notas.
    indice_columna : int
        Índice de la columna que se desea sumar.

    Retorna:
    int | float
        Devuelve la suma total de los valores numéricos de la columna indicada.
    """
    suma_columna = 0
    for fil in range(len(matriz_notas)):
        if type(matriz_notas[fil][indice_columna]) == int or type(matriz_notas[fil][indice_columna]) == float:
            suma_columna += matriz_notas[fil][indice_columna]
    return suma_columna


def calcular_promedio(suma: int, cantidad_notas: int) -> float | None:
    """
    Calcula el promedio a partir de una suma total y una cantidad de notas.

    Parámetros:
    suma : int
        Suma total de las notas o valores.
    cantidad_notas : int
        Cantidad de notas consideradas para el cálculo del promedio.

    Retorna:
    float | None
        Devuelve el promedio (suma / cantidad_notas) si la cantidad es distinta de cero.
        Devuelve None si la cantidad de notas es igual a cero (para evitar división por cero).
    """
    if cantidad_notas != 0:
        promedio = suma / cantidad_notas
        retorno = promedio
    else:
        retorno = None

    return retorno


def calcular_promedio_estudiantes(matriz_notas: list) -> list:
    """
    Calcula el promedio de notas de cada estudiante y lo almacena en un arreglo paralelo.

    Parámetros:
    matriz_notas : list
        Matriz (lista de listas) con las notas de todos los estudiantes.
    array_promedios : list
        Lista donde se guardarán los promedios calculados.

    Retorna:
    list
        Devuelve la lista de promedios actualizada con los valores correspondientes a cada estudiante.
    """
    array_promedios = crear_array(len(matriz_notas),0)
    for fil in range(len(matriz_notas)):
        suma = sumar_fila(matriz_notas, fil)
        promedio = calcular_promedio(suma, 5)
        array_promedios[fil] += promedio

    return array_promedios


def mostrar_promedio_materias(matriz_notas: list) -> None:
    """
    Calcula y muestra el promedio de cada materia a partir de una matriz de notas.

    Cada columna de la matriz representa las notas de una materia, y cada fila
    representa a un estudiante. La función recorre todas las materias (columnas),
    calcula la suma de las notas de cada materia, obtiene el promedio y lo imprime.

    Parámetros:
    matriz_notas : list
        Lista de listas que representa la matriz de notas de los estudiantes.
        Cada fila corresponde a un estudiante y cada columna a una materia.

    Retorno:
    None
        La función solo imprime los promedios de cada materia y no devuelve ningún valor.
    """
    bandera = False
    for col in range(len(matriz_notas[0])):
        suma = sumar_columna(matriz_notas, col)
        promedio = calcular_promedio(suma, len(matriz_notas))
        if bandera == False:
            mayor_promedio = promedio
            indice_materia = col
            bandera = True
        else:
            if promedio < mayor_promedio:
                mayor_promedio = promedio
                indice_materia = col
    print(f"La materia con mayor promedio general es la: N°{indice_materia + 1} con {mayor_promedio}")


def ordenar_lista(array: list, condicion: str) -> list:
    """
    Ordena una lista de números de manera ascendente o descendente usando un método de comparación directa.

    La función recorre la lista comparando elementos y los intercambia según la condición
    indicada. Retorna la lista ordenada.

    Parámetros:
    array : list
        Lista de números que se desea ordenar.

    condicion : str
        Indica el orden de la lista:
        - "ASC": orden ascendente (de menor a mayor)
        - "DESC": orden descendente (de mayor a menor)

    Retorno:
    list
        La misma lista 'array' pero ordenada según la condición indicada.
    """
    for izq in range(len(array) - 1):
        for der in range(izq + 1, len(array)):
            if (condicion == "DESC" and array[izq] < array[der]) or (condicion == "ASC" and array[izq] > array[der]):
                auxiliar = array[izq]
                array[izq] = array[der]
                array[der] = auxiliar
    return array


def buscar_estudiante(array_legajos: list, array_nombres: list, matriz_notas: list, array_generos: list, array_promedios: list):
    """
    Busca un estudiante por su legajo y muestra su información si se encuentra.

    La función solicita al usuario que ingrese un legajo, recorre la lista de legajos
    y si encuentra coincidencia, muestra el estudiante (nombre, notas, género y legajo)
    junto con su promedio. Si no se encuentra, informa que el estudiante no existe.

    Parámetros:
    array_legajos : list
        Lista con los legajos de los estudiantes.

    array_nombres : list
        Lista con los nombres de los estudiantes.

    matriz_notas : list
        Matriz de notas donde cada fila corresponde a un estudiante y cada columna a una materia.

    array_generos : list
        Lista con el género de cada estudiante.

    array_promedios : list
        Lista con el promedio de cada estudiante.

    Retorno:
    None
        La función solo imprime la información en pantalla y no devuelve ningún valor.
    """
    legajo_ingresado = get_int("Ingrese el legajo del estudiante: ","ERROR, ingrese el legajo correctamente (99.999/999.999)",99999, 999999, 5)
    bandera = False
    for i in range(len(array_legajos)):
        if legajo_ingresado == array_legajos[i]:
            print("ESTUDIANTE ENCONTRADO")
            mostrar_estudiante(array_nombres, matriz_notas, array_generos, array_legajos, i)
            print(f"Promedio : {array_promedios[i]}")
            bandera = True
            break
    if bandera == False:
        print("ESTUDIANTE NO ENCONTRADO")


def crear_lista_notas(matriz_notas:list,lista_notas:list)->list:
    for i in range(len(matriz_notas)):
        for j in range(len(matriz_notas[0])):
            nota = matriz_notas[i][j]
            lista_notas[nota - 1] += 1

    return lista_notas

def mostrar_array(array:list)->None:
    for i in range(len(array)):
        print(f"La nota {i+1} se repite : {array[i]}")