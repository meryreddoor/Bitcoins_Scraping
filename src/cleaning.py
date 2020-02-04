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
historical_data = pd.read_csv("INPUT/consolidated_coin_data.csv",encoding='latin1')
clean_kaggle=funciones.changeKaggle(historical_data)

#Merging both files
final_table=funciones.merging(clean_wiki, clean_kaggle)
funciones.Casting(final_table)

#Exporting the file.
final_table.to_csv("OUTPUT/final_table.csv")
