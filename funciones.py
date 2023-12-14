from typing import List, Dict, Tuple, Set

def leer_archivo() -> List[List[str]]:
    '''
    Lee el archivo CSV "stock_celulares.csv" y devuelve una lista de listas con los datos.

    Precondiciones:
    - El archivo "stock_celulares.csv" debe existir en la ruta proporcionada, en este caso la carpeta.

    Postcondiciones:
    - Devuelve una lista de listas con los datos del archivo CSV.
    - Si el archivo no se encuentra, devuelve una lista vacía.
    
    '''
    try:
        with open("stock_celulares.csv", "rt", encoding="utf-8-sig") as archivo:
            return [lineas.strip().split(";") for lineas in archivo]
        
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return []
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return []

#opcion 1 inicio
def lista_celulares() -> Dict[int, str]:
    '''
    Obtiene la lista de marcas de celulares que contiene el archivo "stock_celulares.csv".

    Precondiciones:
    - El archivo "stock_celulares.csv" debe existir y contener datos.

    Postcondiciones:
    - Devuelve un diccionario donde las claves son números enteros y los valores son marcas de celulares.
    
    - Si el archivo no se encuentra o está vacío, devuelve una lista vacía.
    '''
    archivo = leer_archivo()
    
    if archivo:
        equipos = sorted(set(lineas[0] for lineas in archivo[1:]))
        return {k: v for k, v in enumerate(equipos)}
    else:
        return []

def lista_almacenamiento() -> Dict[int, str]:
    '''
    Obtiene la lista de opciones de almacenamiento que contiene el archivo "stock_celulares.csv".

    Precondiciones:
    - El archivo "stock_celulares.csv" debe existir y contener datos.

    Postcondiciones:
    - Devuelve un diccionario donde las claves son números enteros y los valores son opciones de almacenamiento.
    
    - Si el archivo no se encuentra o está vacío, devuelve una lista vacía.
    '''
    archivo = leer_archivo()
    if archivo:
        almacenamientos = sorted(set(lineas[4] for lineas in archivo[1:]))
        return {k: v for k, v in enumerate(almacenamientos)}
    else:
        return []

def modelos_cel(elegido1: str, elegido2: str) -> List[List[str]]:
    '''
    Filtra los modelos de celulares según la marca y el almacenamiento especificados.

    Precondiciones:
    - El archivo "stock_celulares.csv" debe existir y contener datos.

    Parámetros:
    - elegido1: Marca de celular.
    - elegido2: Almacenamiento del celular.

    Postcondiciones:
    - Devuelve una lista de listas con los modelos de celulares que coinciden con la marca y el almacenamiento especificados.
    - Si el archivo no se encuentra o está vacío, devuelve una lista vacía.
    '''
    archivo = leer_archivo()
    if archivo:
        return [elem for elem in archivo[1:] if elem[0] == elegido1 and elem[4] == elegido2]
    else:
        return []

def print_opcion1() -> None:
    '''
    Imprime las especificaciones de celulares según la marca y el almacenamiento seleccionados por el usuario.

    Precondiciones:
    - El archivo "stock_celulares.csv" debe existir y contener datos.

    Postcondiciones:
    - Imprime las especificaciones de celulares según la marca y el almacenamiento seleccionados por el usuario.
    '''
    modelos = lista_celulares()
    almacenamientos = lista_almacenamiento()
    encabezado = leer_archivo()[0]
    while True:
        try:
            if modelos and almacenamientos:
                print("Marcas disponibles:")
                print(" | ".join([f"{k} - {v}" for k, v in modelos.items()]))
                numero1 = int(input("Ingrese el número de la marca: "))

                print("Almacenamientos disponibles:")
                print(" | ".join([f"{k} - {v}" for k, v in almacenamientos.items()]))
                numero2 = int(input("Ingrese el número del almacenamiento: "))

                marca_elegida = modelos[numero1]
                almacenamiento_elegido = almacenamientos[numero2]

                print("\nResultados:")
                print(" | ".join([f"{enca}" for enca in encabezado]))
                for celular in modelos_cel(marca_elegida, almacenamiento_elegido):
                    print(f" | ".join([f'{cel}' for cel in celular]))
                break
        except KeyError:
            print("Ingrese un numero valido.")
        except ValueError:
            print("Ingrese un numero.")
        else:
            print("No hay modelos disponibles.")
#opcion 1 final
         
#opcion 2 inicio
def pedir_validar_producto() -> List[str]:
    '''
    Solicita y valida los datos de un nuevo producto ingresados por el usuario.

    Postcondiciones:
    - Devuelve una lista con los datos del nuevo producto ingresados por el usuario.
   '''
    datos = []
    while True:
        try:
            marca = input("Ingrese la marca de celular que quiere agregar: ").capitalize()
            while not marca.isalpha():
                marca = input("Ingrese la marca de celular que quiere agregar: ")

            modelo = input("Ingrese el modelo de celular que quiere agregar: ")
            while len(modelo) == 0:
                modelo = input("Ingrese el modelo de celular que quiere agregar: ")

            cantidad = input("Ingrese la cantidad de celulares que tiene: ")
            while not cantidad.isdigit() or int(cantidad) <= 0 or int(cantidad) > 50:
                cantidad = input("Ingrese una cantidad válida de celulares (entre 1 y 50): ")

            precio = input("Ingrese el precio del celular (Solo números): ")
            while not precio.isdigit() or int(precio) <= 0:
                precio = input("Ingrese un precio válido del celular (Solo números y mayor a 0): ")

            almacenamiento = input("Ingrese el almacenamiento del celular: ")
            while almacenamiento not in ['64', '128', '256', '512', '1024']:
                almacenamiento = input("Ingrese un almacenamiento válido (64, 128, 256, 512, 1024): ")

            anio_lanzamiento = input("Ingrese el año que se lanzó el modelo del celular: ")
            while not anio_lanzamiento.isdigit() or int(anio_lanzamiento) < 1983 or int(anio_lanzamiento) > 2024:
                anio_lanzamiento = input("Ingrese un año válido de lanzamiento del modelo (entre 1983 y 2024): ")

            datos.append([marca, modelo, cantidad, precio, almacenamiento, anio_lanzamiento])
            break

        except ValueError:
            print("Ingrese un valor válido.")
            continue

    return datos

def agregar_datos() -> None:
    '''
    Agrega nuevos datos de productos al archivo "stock_celulares.csv".

    Postcondiciones:
    - Agrega nuevos datos de productos al archivo "stock_celulares.csv".
    
    - Imprime un mensaje indicando que los datos se han agregado exitosamente.
    '''
    datos = pedir_validar_producto()
    with open("stock_celulares.csv", 'a', newline='') as archivo_csv:
        for fila in datos:
            fila_str = ';'.join(fila) + '\n'
            archivo_csv.write(fila_str)

    print("Datos agregados al archivo CSV.")
#opcion 2 final
    
#opcion 3 incio
def obtener_conjuntos_unicos(archivo: List[List[str]]) -> Tuple[Set[str], Set[str], Set[str]]:
    '''
    Obtiene conjuntos de datos únicos de marcas, modelos y almacenamientos presentes en el archivo "stock_celulares.csv".

    Precondiciones:
    - El archivo "stock_celulares.csv" debe existir y contener datos.

    Postcondiciones:
    - Devuelve conjuntos únicos que representan marcas, modelos y almacenamientos presentes en el archivo.
    '''
    marcas = set(elem[0] for elem in archivo[1:])
    modelos = set(elem[1] for elem in archivo[1:])
    almacenamientos = set(elem[4] for elem in archivo[1:])
    return marcas, modelos, almacenamientos

def opciones_stock(archivo: List[List[str]]) -> None:
    '''
    Permite al usuario modificar el stock de un producto específico en el archivo "stock_celulares.csv".

    Precondiciones:
    - El archivo "stock_celulares.csv" debe existir y contener datos.

    Postcondiciones:
    - Modifica el stock de un producto específico en el archivo "stock_celulares.csv" según la elección del usuario.
    
    - Imprime un mensaje indicando que el stock se ha modificado exitosamente.
    '''
    marcas = set(elem[0] for elem in archivo[1:])
    modelos = set(elem[1] for elem in archivo[1:])
    almacenamientos = set(elem[4] for elem in archivo[1:])

    marca_elegida = input("Ingrese la marca de celular: ").capitalize()
    modelo_elegido = input("Ingrese el modelo de celular: ")
    almacenamiento_elegido = input("Ingrese el almacenamiento del celular: ")

    if marca_elegida not in marcas or modelo_elegido not in modelos or almacenamiento_elegido not in almacenamientos:
        print("Los datos ingresados no existen en el archivo.")
        return

    modificar_stock(marca_elegida, modelo_elegido, almacenamiento_elegido, archivo)

def modificar_stock(marca: str, modelo: str, almacenamiento: str, archivo: List[List[str]]):
    '''
    Modifica el stock de un producto específico en el archivo "stock_celulares.csv".

    Precondiciones:
    - El archivo "stock_celulares.csv" debe existir y contener datos.

    Postcondiciones:
    - Modifica el stock del producto especificado en el archivo "stock_celulares.csv".
    
    - Imprime un mensaje indicando que el stock se ha modificado exitosamente.
    '''
    indice_fila = [i for i, elem in enumerate(archivo[1:]) if elem[0] == marca and elem[1] == modelo and elem[4] == almacenamiento]
    if not indice_fila:
        print("No se encontró el celular con los datos proporcionados.")
        return

    indice_fila = indice_fila[0] + 1
    cantidad_actual = int(archivo[indice_fila][2])

    print(f"La cantidad actual de {marca} {modelo} con almacenamiento {almacenamiento} es: {cantidad_actual}")

    while True:
        opcion = input("¿Desea sumar (+) o restar (-) al stock? Ingrese su elección: ")
        if opcion not in ['+', '-']:
            print("Opción no válida. Ingrese '+' para sumar o '-' para restar.")
            continue

        cantidad = int(input("Ingrese la cantidad a modificar: "))

        if (opcion == '-' and cantidad > cantidad_actual) or (opcion == '+' and cantidad_actual + cantidad > 50):
            print("No se puede restar más de la cantidad actual o sumar más de 50.")
        else:
            archivo[indice_fila][2] = str(cantidad_actual + cantidad if opcion == '+' else cantidad_actual - cantidad)
            break

    with open("stock_celulares.csv", 'w') as archivo_csv:
        for fila in archivo:
            fila_str = ';'.join(fila) + '\n'
            archivo_csv.write(fila_str)

    print("Stock modificado exitosamente.")
#opcion 3 final
    
#opcion 4 incio
def opciones_precio(archivo: List[List[str]]) -> None:
    '''
    Permite al usuario modificar el precio de un producto específico en el archivo "stock_celulares.csv".

    Precondiciones:
    - El archivo "stock_celulares.csv" debe existir y contener datos.

    Postcondiciones:
    - Modifica el precio de un producto específico en el archivo "stock_celulares.csv" según la elección del usuario.
    
    - Imprime un mensaje indicando que el precio se ha modificado exitosamente.
    '''
    marcas, modelos, almacenamientos = obtener_conjuntos_unicos(archivo)

    marca_elegida = input("Ingrese la marca de celular: ").capitalize()
    modelo_elegido = input("Ingrese el modelo de celular: ")
    almacenamiento_elegido = input("Ingrese el almacenamiento del celular: ")

    if marca_elegida not in marcas or modelo_elegido not in modelos or almacenamiento_elegido not in almacenamientos:
        print("Los datos ingresados no existen en el archivo.")
        return

    modificar_precio(marca_elegida, modelo_elegido, almacenamiento_elegido, archivo)


def modificar_precio(marca: str, modelo: str, almacenamiento: str, archivo: List[List[str]]):
    '''
    Modifica el precio de un producto específico en el archivo "stock_celulares.csv".

    Precondiciones:
    - El archivo "stock_celulares.csv" debe existir y contener datos.

    Postcondiciones:
    - Modifica el precio de un producto específico en el archivo "stock_celulares.csv".
    
    - Imprime un mensaje indicando que el precio se ha modificado exitosamente.
    '''
    indice_fila = [i for i, elem in enumerate(archivo[1:]) if elem[0] == marca and elem[1] == modelo and elem[4] == almacenamiento]
    if not indice_fila:
        print("No se encontró el celular con los datos proporcionados.")
        return

    indice_fila = indice_fila[0] + 1
    precio_actual = int(archivo[indice_fila][3].strip())

    print(f"El precio actual de {marca} {modelo} con almacenamiento {almacenamiento} es: ${precio_actual}")

    while True:
        try:
            nuevo_precio = int(input("Ingrese el nuevo precio del celular: "))
            if nuevo_precio < 0 or nuevo_precio > 10000:
                print("El precio debe estar entre 0 y 10000.")
            else:
                archivo[indice_fila][3] = f"{nuevo_precio}"
                break
        except ValueError:
            print("Ingrese un número válido.")

    with open("stock_celulares.csv", 'w') as archivo_csv:
        for fila in archivo:
            fila_str = ';'.join(fila) + '\n'
            archivo_csv.write(fila_str)

    print("Precio modificado exitosamente.")
#opcion 4 final

#opcion 5 incio
def presupuesto(archivo: List[List[str]]) -> None:
    '''
    Imprime la lista de celulares disponibles de una marca específica dentro del presupuesto del usuario.

    Precondiciones:
    - El archivo "stock_celulares.csv" debe existir y contener datos.

    Postcondiciones:
    - Imprime la lista de celulares disponibles de una marca específica dentro del presupuesto del usuario.
    '''
    precios = set(int(elem[3].strip()) for elem in archivo[1:])

    while True:
        try:
            presupuesto_usuario = int(input("Ingrese su presupuesto: "))
            if presupuesto_usuario <= 0:
                print("El presupuesto debe ser mayor que 0.")
            else:
                break
        except ValueError:
            print("Ingrese un número válido.")

    marca_elegida = input("Ingrese la marca de celular que busca: ")

    print(f"Celulares disponibles de la marca {marca_elegida} dentro del presupuesto de ${presupuesto_usuario}:")
    for precio in range(presupuesto_usuario, -1, -1):
        if precio in precios:
            celulares = [elem for elem in archivo[1:] if int(elem[3].strip()) == precio and elem[0].lower() == marca_elegida.lower()]
            for celular in celulares:
                print(f"Marca: {celular[0]}, Modelo: {celular[1]}, Precio: {celular[3]}")
#opcion 5 final

#opcion 6 incio
def compra(archivo: List[List[str]]) -> None:
    '''
    Realiza la compra de un celular según la elección del usuario y actualiza el stock en el archivo "stock_celulares.csv".

    Precondiciones:
    - El archivo "stock_celulares.csv" debe existir y contener datos.

    Postcondiciones:
    - Realiza la compra de un celular según la elección del usuario.
    
    - Actualiza el stock en el archivo "stock_celulares.csv".
    '''
    if not archivo:
        print("No se encontró el archivo.")
        return
    marcas = sorted(set(linea[0] for linea in archivo[1:]))
    modelos = sorted(set(linea[1] for linea in archivo[1:]))
    almacenamientos = sorted(set(linea[4] for linea in archivo[1:]))

    print("Marcas disponibles:")
    for num, marca in enumerate(marcas, start=1):
        print(f"{num}. {marca}")

    while True:
        try:
            marca_num = int(input("Ingrese el número de la marca: "))
            if 1 <= marca_num <= len(marcas):
                marca_elegida = marcas[marca_num - 1]
                break
            else:
                print("Ingrese un número válido.")
        except ValueError:
            print("Ingrese un número.")

    print("\nAlmacenamientos disponibles:")
    for num, almacenamiento in enumerate(almacenamientos, start=1):
        print(f"{num}. {almacenamiento}GB")

    while True:
        try:
            almacenamiento_num = int(input("Ingrese el número del almacenamiento: "))
            if 1 <= almacenamiento_num <= len(almacenamientos):
                almacenamiento_elegido = almacenamientos[almacenamiento_num - 1]
                break
            else:
                print("Ingrese un número válido.")
        except ValueError:
            print("Ingrese un número.")

    print(f"\nModelos disponibles de {marca_elegida} con {almacenamiento_elegido}GB:")
    modelos_disponibles = [linea[1] for linea in archivo[1:] if linea[0] == marca_elegida and linea[4] == almacenamiento_elegido]
    for num, modelo in enumerate(modelos_disponibles, start=1):
        print(f"{num}. {modelo}")

    while True:
        try:
            modelo_num = int(input("Ingrese el número del modelo: "))
            if 1 <= modelo_num <= len(modelos_disponibles):
                modelo_elegido = modelos_disponibles[modelo_num - 1]
                break
            else:
                print("Ingrese un número válido.")
        except ValueError:
            print("Ingrese un número.")

    efectivo_o_tarjeta = input("Elige una opción de pago (Efectivo/Tarjeta): ").lower()

    if efectivo_o_tarjeta == "efectivo":
        for linea in archivo[1:]:
            if linea[0] == marca_elegida and linea[1] == modelo_elegido and linea[4] == almacenamiento_elegido:
                precio = float(linea[3].strip('$'))
                efectivo(marca_elegida, modelo_elegido, almacenamiento_elegido, precio)
                # Actualizar el stock
                for l in archivo[1:]:
                    if l[0] == marca_elegida and l[1] == modelo_elegido and l[4] == almacenamiento_elegido:
                        l[2] = str(int(l[2]) - 1)
                with open("stock_celulares.csv", 'w') as file:
                    for line in archivo:
                        file.write(';'.join(line) + '\n')
                break
    elif efectivo_o_tarjeta == "tarjeta":
        for linea in archivo[1:]:
            if linea[0] == marca_elegida and linea[1] == modelo_elegido and linea[4] == almacenamiento_elegido:
                precio = float(linea[3].strip('$'))
                tarjeta(marca_elegida, modelo_elegido, almacenamiento_elegido, precio)
                # Actualizar el stock
                for l in archivo[1:]:
                    if l[0] == marca_elegida and l[1] == modelo_elegido and l[4] == almacenamiento_elegido:
                        l[2] = str(int(l[2]) - 1)
                with open("stock_celulares.csv", 'w') as file:
                    for line in archivo:
                        file.write(';'.join(line) + '\n')
                break
    else:
        print("Opción de pago no válida.")
        
        
def efectivo(marca: str, modelo: str, almacenamiento: str, precio: float) -> None:
    '''
    Realiza una transacción en efectivo para la compra de un celular.

    Precondiciones:
    - La marca, el modelo y el almacenamiento deben ser cadenas no vacías.
    
    - El precio debe ser un número positivo mayor que 0.

    Postcondiciones:
    - Imprime información sobre el celular y realiza una transacción en efectivo.
    
    - Imprime la factura con los detalles de la compra.
    '''
    print(f"El celular {marca} {modelo} de {almacenamiento}GB cuesta ${precio}")

    while True:
        try:
            monto_pagado = float(input("Ingrese con cuánto va a pagar: $"))
            if monto_pagado >= precio:
                cambio = monto_pagado - precio
                print(f"Su cambio es de ${cambio}")
                print("Factura:")
                print(f"Marca: {marca}\nModelo: {modelo}\nAlmacenamiento: {almacenamiento}\nPrecio: ${precio}")
                break
            else:
                print("El monto ingresado es insuficiente.")
        except ValueError:
            print("Ingrese un monto válido.")
            
def tarjeta(marca: str, modelo: str, almacenamiento: str, precio: float) -> None:
    '''
        Realiza una transacción con tarjeta Visa para la compra de un celular.

    Precondiciones:
    - La marca, el modelo y el almacenamiento deben ser cadenas no vacías.
    
    - El precio debe ser un número positivo mayor que 0.

    Postcondiciones:
    - Realiza una transacción con tarjeta Visa.
    
    - Imprime la factura con los detalles de la compra.
    '''
    print("Procesando pago con tarjeta...")

    while True:
        try:
            numero_tarjeta = input("Ingrese el número de la tarjeta Visa: ")
            codigo_seguridad = input("Ingrese el código de seguridad (3 dígitos): ")
            dni = int(input("Ingrese su DNI: "))
            
            if len(numero_tarjeta) == 16 and codigo_seguridad.isdigit() and len(codigo_seguridad) == 3 and 10000000 <= dni <= 47000000:
                print("Pago con tarjeta exitoso.")
                print("Factura:")
                print(f"Marca: {marca}\nModelo: {modelo}\nAlmacenamiento: {almacenamiento}\nPrecio: ${precio}")
                break
            else:
                print("Datos de tarjeta o DNI inválidos.")
        except ValueError:
            print("Ingrese un DNI válido.")

#opcion 6 final           
def menu()-> None:
   print(
       "--MENU--\n"
       "1-Especificaciones de Celulares por Marca y Almacenamiento\n"
       "2-Agregar Producto\n"
       "3-Modificacion de stock\n"
       "4-Modificacion de precio\n"
       "5-Celulares por presupuesto de usuario\n"
       "6-Compra de celular\n"
       "0-Salir\n"
       )

if __name__ == "__main__":
    print()
    
