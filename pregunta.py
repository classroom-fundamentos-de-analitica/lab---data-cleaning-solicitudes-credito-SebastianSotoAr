"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import re
import pandas as pd


def clean_data():

    #index_col = 0 obliga a usar la primera columna como indice
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)

    #Elimina las filas con datos perdidos
    df.dropna(axis=0, inplace=True)

    #Limpia la fila monto_del_credito y la convierte en int
    df.monto_del_credito = df.monto_del_credito.str.strip("$")
    df.monto_del_credito = df.monto_del_credito.str.replace(",","")
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.monto_del_credito = df.monto_del_credito.astype(int)

    #Comvierte la fila fecha_de_beneficio
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)

    #Limpia las filas sexo, tipo_de_emprendimiento, idea_negocio, línea_credito y barrio
    for filas in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']:
        df[filas] = df[filas].str.lower()
        df[filas] = df[filas].str.replace('_', ' ')
        df[filas] = df[filas].str.replace('-', ' ')

    #Elimina los duplicados
    df.drop_duplicates(inplace=True)

    return df

if __name__ == "__main__":
    df = clean_data()
    print(df.dtypes)
    print(df.sexo.value_counts())