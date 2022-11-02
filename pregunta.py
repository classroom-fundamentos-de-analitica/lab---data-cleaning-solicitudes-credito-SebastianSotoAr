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
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)

    #Limpia las filas sexo, tipo_de_emprendimiento, idea_negocio, línea_credito y barrio
    for filas in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']:
        df[filas] = df[filas].str.lower()

    return df

if __name__ == "__main__":
    #print(list(filter(lambda data: ((data != "masculino") and (data != "femenino")), clean_data().sexo.str)))
    print(clean_data().columns)
    print(clean_data().dtypes)
    print(clean_data().head())
    #for data in clean_data().monto_del_credito:
        #if ((re.match(r"\D", data))):
            #print(data)
