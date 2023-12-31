import funciones as fn


def main() -> None:
    '''
    Función principal que ejecuta el menú para interactuar con el sistema de gestión de celulares.

    Precondiciones:
    - El archivo "funciones.py" debe existir y contener las funciones necesarias.
    
    - El archivo "stock_celulares.csv" debe existir y contener datos.

    Postcondiciones:
    - Inicia un bucle de menú que permite al usuario interactuar con el sistema hasta que elija salir.
    '''
    archivo = fn.leer_archivo()
    if archivo:
        while True:
            fn.menu()
            try:
                opcion = int(input("Elige tu opción: "))
            except ValueError:
                print("Ingrese un número válido.")
            except IndexError:
                print("La selección no es válida.")
            except Exception as e:
                print(f"Ocurrió un error: {e}")
            else:
                if opcion == 1:
                    fn.print_opcion1()
                elif opcion == 2:
                    fn.agregar_datos()
                elif opcion == 3:
                    fn.opciones_stock(archivo)
                elif opcion == 4:
                    fn.opciones_precio(archivo)
                elif opcion == 5:
                    fn.presupuesto(archivo)
                elif opcion == 6:
                    fn.compra(archivo)
                elif opcion == 0:
                    print("Ha salido con éxito.")
                    break


if __name__ == "__main__":
    main()
