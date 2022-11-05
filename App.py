import pandas as pd
from tabulate import tabulate
import csv

estado = True

def generar_tabla(ruta,estado_index,formato):
    with open(ruta, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        j=0 
        for row in reader:
            if j == 0: 
                headers = list(row)
                j+=1
            else:
                if estado_index:
                    headers.insert(0, "ID")
                break
    df = pd.read_csv(link)
    print(tabulate(df, headers, tablefmt=formato, showindex=estado_index))

def guardar_csv():
    archivo_csv = True
    print("\nArchivo guardado correctamente...\n")

def describir_datos(link):
    generar_tabla(link, False, "simple")

def mostrar_datos(link):
    generar_tabla(link, True, "outline")

def filtrar_registros():
    df = pd.read_csv(url)
    filtro = input("Digite la condicion para filtrar de la siguiente manera:\n Nombre de la columna comparativa valor\nAviso: la comparativa se lleva con los simbolos mayor que, menor que, o igual\n para el igual se recomienda usar \'==\'\n: ")
    df1 = df.query(filtro)
    print(tabulate(df1, tablefmt="outline", showindex=False))

while(estado):
    print("Cual de las siguientes opciones desea realizar:\n1. Ingresar/actualizar archivo CSV")
    print("2. Describir datos\n3. Mostrar datos\n4. Ordenar registros\n5. Filtrar registros\n6. Agregar registros")
    print("7. Modificar registros\n8. Eliminar registros\n9. Exportar/Guardar datos\n0. Salir\n")
    opc = int(input("Ingrese su opcion a realizar: "))

    if opc == 1:
        url = input("Digite la ruta donde se encuentra el archivo CSV: ")
        guardar_csv()
    elif opc == 2:
        describir_datos(url)
    elif opc == 3:
        mostrar_datos(url)
    elif opc == 4:
        pass
    elif opc == 5:
        filtrar_registros()
    elif opc == 6:
        pass
    elif opc == 7:
        pass
    elif opc == 8:
        pass
    elif opc == 9:
        pass
    elif opc == 0:
        estado = False
    else:
        print("Por favor digite los numeros segun como se muestra en el menu")  
