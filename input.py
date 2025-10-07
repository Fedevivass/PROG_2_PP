def es_entero(texto:str) -> bool:
    """
    Verifica si una cadena de texto está compuesta únicamente por caracteres numéricos (dígitos).

    La función recorre la cadena desde el segundo carácter (índice 1) hasta el final, 
    y verifica que todos sean dígitos (del '0' al '9'). Si encuentra algún carácter que no sea dígito, 
    retorna False. Si todos son dígitos, retorna True.

    Nota: La función ignora el primer carácter de la cadena (índice 0) en la verificación.

    Parámetros:
    texto(str): La cadena de texto a validar.

    Retorna:
    bool: True si todos los caracteres desde el segundo en adelante son dígitos, False en caso contrario.
    """
    retorno = True
    for i in range(1, len(texto)):
        valor_ascii = ord(texto[i])
        if valor_ascii < ord("0") or valor_ascii > ord("9"):
            retorno = False
    return retorno

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    """
    Solicita al usuario que ingrese un número entero dentro de un rango específico,
    permitiendo un número limitado de reintentos en caso de error.

    La función utiliza la función `es_entero` para validar que la entrada del usuario
    sea un número entero válido (cadena compuesta solo por dígitos). Si la validación es exitosa,
    convierte la entrada a entero y verifica que esté dentro del rango [minimo, maximo].
    Si no es válido, muestra un mensaje de error y permite reintentar hasta agotar los reintentos.

    Parámetros:
    mensaje (str): Texto que se muestra para solicitar la entrada al usuario.
    mensaje_error (str): Texto que se muestra cuando la entrada es inválida o fuera del rango.
    minimo (int): Valor mínimo permitido (inclusive).
    maximo (int): Valor máximo permitido (inclusive).
    reintentos (int): Cantidad máxima de intentos permitidos para ingresar un valor válido.

    Retorna:
    int | None: El número entero validado si la entrada es correcta, o None si se agotaron los reintentos.
    """
    contador = 0
    retorno = None
    while contador < reintentos:
        numero = input(mensaje)
        if es_entero(numero):
            numero = int(numero)
            if numero >= minimo and numero <= maximo:
                retorno = numero
                break
            else:
                print(mensaje_error)
        else:
            print(mensaje_error)
        contador += 1
    return retorno

def es_string(texto:str) -> bool:
    """
    Verifica si una cadena está compuesta únicamente por letras mayúsculas o minúsculas del alfabeto inglés.

    La función recorre la cadena desde el segundo carácter (índice 1) hasta el final, 
    y verifica que cada carácter sea una letra entre 'A'-'Z' (mayúsculas) o 'a'-'z' (minúsculas).
    Si encuentra algún carácter que no cumple esta condición, retorna False.
    Si todos los caracteres son letras válidas, retorna True.

    Nota: La función ignora el primer carácter de la cadena (índice 0) en la verificación.

    Parámetros:
    texto(str): Cadena de texto a validar.

    Retorna:
    bool: True si todos los caracteres desde el segundo en adelante son letras válidas, False en caso contrario.
    """
    retorno = True
    for i in range(1,len(texto)):
        valor_ascii = ord(texto[i])
        if valor_ascii < 65 or (valor_ascii > 90 and valor_ascii < 97) or valor_ascii > 122:
            retorno = False
    return retorno

def get_string(mensaje:str, mensaje_error:str,longitud:int, reintentos:int)->str|None:
    """
    Solicita al usuario ingresar una cadena de texto que cumpla ciertas condiciones,
    con un número limitado de intentos para ingresar un valor válido.

    La función utiliza `es_string` para validar que la cadena esté compuesta solo por letras
    (mayúsculas o minúsculas, según la función `es_string` que valida desde el segundo carácter).
    Además, verifica que la longitud de la cadena sea menor que el valor especificado en `longitud`.
    Si la entrada es válida, retorna la cadena. Si no, muestra un mensaje de error y permite reintentos.

    Parámetros:
    mensaje (str): Texto que se muestra para solicitar la entrada al usuario.
    mensaje_error (str): Texto que se muestra cuando la entrada es inválida o no cumple la condición de longitud.
    longitud (int): Longitud máxima permitida para la cadena.
    reintentos (int): Cantidad máxima de intentos permitidos para ingresar un valor válido.

    Retorna:
    str | None: La cadena ingresada si es válida, o None si se agotaron los reintentos sin éxito.
    """
    retorno = None
    contador = 0
    while contador < reintentos:
        cadena = input(mensaje)
        if es_string(cadena):
            if len(cadena) < longitud:
                retorno = cadena
                contador = reintentos + 1
            else:
                print(mensaje_error)
                contador += 1
        else:
            print(mensaje_error)
            contador += 1
    
    return retorno
