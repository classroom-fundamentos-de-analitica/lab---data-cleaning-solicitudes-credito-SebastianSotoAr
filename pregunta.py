"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import re
import pandas as pd


def clean_data():

    #Limpia la fila monto_del_credito y la convierte en int
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.monto_del_credito = df.monto_del_credito.str.strip("$")
    df.monto_del_credito = df.monto_del_credito.str.replace(",","")
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.monto_del_credito = df.monto_del_credito.astype(int)

    #Comvierte la fila fecha_de_beneficio
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio)

    return df

if __name__ == "__main__":
    print(clean_data().fecha_de_beneficio)