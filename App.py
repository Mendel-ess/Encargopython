import pandas as pd
from tabulate import tabulate
import csv


global df

def generar_tabla(dataframe, formato):
        global df
        if formato == "outline":
            head = list(dataframe.head())
            head.insert(0, "ID")
            print(tabulate(dataframe, head,  tablefmt=formato, showindex=True))
        else:
            print(tabulate(dataframe, dataframe.head(),  tablefmt=formato, showindex=False))
        print(dataframe.columns.tolist())
        

        

def guardar_csv():
    archivo_csv = True
    print("\nArchivo guardado correctamente...\n")

def describir_datos():
    generar_tabla(df, "simple")

def mostrar_datos():
    generar_tabla(df,"outline")

def filtrar_registros(filter):
    global df
    df = df.query(filter)
    generar_tabla(df, "outline")

def ordenar_registros(columna, forma):
    global df
    if(forma.upper() == "DESCENDENTE"):
        df.sort_values(by=[columna], inplace=True,ascending=False)
    else:
        df.sort_values(by=[columna], inplace=True)

    generar_tabla(df, "outline")
def agregar_registro(dts):
    global df
    df = df.append(dts, ignore_index=True)
    generar_tabla(df, "outline")

def modifcar_registro():
    pass
def eliminar_registro(n_index):
    global df
    df = df.drop(df.index[n_index])
    generar_tabla(df, "outline")
def exportar_csv():
    pass

def inicio():
    estado = True
    while(estado):
        print("Cual de las siguientes opciones desea realizar:\n1. Ingresar/actualizar archivo CSV")
        print("\n2. Describir datos\n3. Mostrar datos\n4. Ordenar registros\n5. Filtrar registros\n6. Agregar registros")
        print("7. Modificar registros\n8. Eliminar registros\n9. Exportar/Guardar datos\n0. Salir\n")
        opc = int(input("Ingrese su opcion a realizar: "))

        if opc == 1:
            global df
            ruta = input("Digite la ruta donde se encuentra el archivo CSV: ")
            df = pd.read_csv(ruta, delimiter=',')
            guardar_csv()
        elif opc == 2:
            describir_datos()
        elif opc == 3:
            mostrar_datos()
        elif opc == 4:
            co = input("Nombre de la columna: ")
            form  = input("Ordenara de manera Ascendente o Descendente: ")
            ordenar_registros(co, form)
        elif opc == 5:
            print("Digite la condicion para filtrar\nColumna > valor o Columna == valor o Columna < valor: ")
            col = input("Nombre de la columna: ")
            cond = input("Simbolo del condicionante (>,==,<): ")
            val = input("Valor a buscar: ")
            fil = f"{col} {cond} {val}"
            filtrar_registros(fil)
        elif opc == 6:
            pais = input("Digite el nuevo pais a agregar: ")
            ct = float(input("cantidad de cervesas tomadas: "))
            bat = float(input("Cantidad de bebidas alcoholicas tomadas: "))
            vt = float(input("Cantidad de vino tomado: "))
            ta = float(input("Total de alcohol tomado en litros: "))
            data = {'Pais': pais,'Cervesas_tomadas': ct,'Bebidas_alcoholicas_tomadas':bat,'Vino_tomado': vt,'Total_de_alcohol_puro_en_litros': ta}
            agregar_registro(data)
        elif opc == 7:
            modifcar_registro()
        elif opc == 8:
            num = int(input("Digite el indice a eleminar: "))
            eliminar_registro(num)
        elif opc == 9:
            exportar_csv()
        elif opc == 0:
            estado = False
        else:
            print("Por favor digite los numeros segun como se muestra en el menu")  

if __name__ == '__main__':
    inicio()