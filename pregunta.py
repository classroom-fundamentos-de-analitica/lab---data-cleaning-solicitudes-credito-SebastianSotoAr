"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import re
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.monto_del_credito = df.monto_del_credito.str.strip("$")
    df.monto_del_credito = df.monto_del_credito.str.replace(",","")
    df.monto_del_credito = df.monto_del_credito.astype(float)

    return df

if __name__ == "__main__":
    #print(list(filter(lambda data: re.match(r"\D", data), clean_data().monto_del_credito)))
    #print("--------------------------------------")
    #for data in clean_data().monto_del_credito:
        #if ((re.match(r"\D", data))):
            #print(data)

    print(clean_data().monto_del_credito)