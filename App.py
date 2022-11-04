import csv

estado = True

def guardar_csv():
    archivo_csv = True
    print("Archivo guardado correctamente...")

def describir_datos(link):
    with open(link, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print(row)

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
        pass
    elif opc == 4:
        pass
    elif opc == 5:
        pass
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
