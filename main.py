import re
import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup
import matplotlib
import matplotlib.pyplot as plt
import funciones

#Extracting the information from the web page.
res = requests.get("https://en.wikipedia.org/wiki/List_of_cryptocurrencies")
soup = BeautifulSoup(res.text, 'html.parser')

datos=soup.find_all('table')[0]
datos.find_all('tr')[1].find_all("td")[0]

wiki=funciones.createDF(datos)
clean_wiki = funciones.quitarBrackets(wiki)
clean_wiki=funciones.changeWiki(wiki)

#Extracting information from Kaggle
historical_data = pd.read_csv("/Users/mariaroigporta/Ironhack/Bitcoins_Scraping/INPUT/consolidated_coin_data.csv",encoding='latin1')
clean_kaggle=funciones.changeKaggle(historical_data)

#Merging both files
final_table=funciones.merging(clean_wiki, clean_kaggle)
funciones.Casting(final_table)

#Exporting the file.
final_table.to_csv("/Users/mariaroigporta/Ironhack/Bitcoins_Scraping/OUTPUT/final_table.csv")

#Graphics
funciones.graphic(final_table)

funciones.variation(final_table).plot.line()
plt.gcf().set_size_inches(10,10)
plt.show()

describeDatos=funciones.describe(final_table)

print('INFORMACION SOBRE LAS MONEDAS:')
print(describeDatos)
print('\n')
print('-------------------------------------------------------------')

print('SELECCIONA LOS DATOS QUE QUIERES VER:')
print('\n')
x = input(str('Introduce una moneda: '))
y=input(str('Introduce un año AAAA-MM-DD: '))

filter_table=funciones.descriptions(final_table, x, y)

print('-------------------------------------------------------------')
print('\n')
print(f"Características moneda {x} a fecha {y}")
print('\n')
print(filter_table)
print('\n')
print('-------------------------------------------------------------')
print('\n')
print(f'Medias Historicas de {x}')
print('\n')
print(final_table.groupby(['Currency']).get_group(x).mean())
