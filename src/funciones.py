import re
import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup
import matplotlib
import matplotlib.pyplot as plt


def createDF(table):
    
    headers = [header.text[:-1] for header in table.find_all('th')]
    data=[]
    for row in table.find_all('tr')[1:]:
        currency = {}
        for index,value in enumerate(row.find_all("td")):
            currency[headers[index]]=value.text[:-1]
        data.append(currency)
    data = pd.DataFrame(data)
    return data


def quitarBrackets(wiki):
    for columna in wiki:
        wiki[columna] = wiki[columna].str.replace(r"\[.*\]","")
    return wiki



def changeWiki(clean_wiki):    
    for i in range(len(clean_wiki)):

        diccionario = {'EOS.IO':'EOS',
                       'Bitcoin-cash':'Bitcoin Cash', 
                       'Ether or "Ethereum"':'Ethereum'
                      }
        for x,y in diccionario.items(): 
                clean_wiki['Currency'].values[i] = clean_wiki['Currency'].values[i].replace(x, y)
    return clean_wiki

def changeKaggle(historical_data):    
    for i in range(len(historical_data)):

        diccionario = {'bitcoin':'Bitcoin',
                       'bitcoin-cash':'Bitcoin Cash', 
                       'eos':'EOS',
                       'ethereum':'Ethereum',
                       'litecoin':'Litecoin',
                       'stellar':'Stellar',
                       'tether':'Tether',
                       'xrp':'Ripple'
                      }
        for x,y in diccionario.items(): 
                historical_data['Currency'].values[i] = historical_data['Currency'].values[i].replace(x, y)
    return historical_data

def merging(clean_wiki,clean_kaggle):
    result=pd.merge(clean_wiki,
                   clean_kaggle,
                   on='Currency')
    return result[['Release','Currency','Symbol','Programming language of implementation','Notes','Date','Close','Market Cap']]

def Casting(final_table):
    final_table['Close'] = final_table['Close'].str.replace(',', '').astype(float)
    final_table['Market Cap']=final_table['Market Cap'].str.replace(',', '').astype(float)
    final_table['Date']=pd.to_datetime(final_table['Date'])
    return


def graphic(final_table):
    fig,ax = plt.subplots()
    for label, grp in final_table.groupby('Currency'):
        a=grp.plot(x = 'Date', y = 'Close',ax = ax,label = label)
    plt.gcf().set_size_inches(30, 10)
    plt.show()
    return 


def variation(final_table):
    var_rate = final_table.sort_values('Date').set_index('Date').groupby('Currency').apply(lambda x: x['Close'].std())
    return var_rate.T

def describe(final_table):
    des = final_table.sort_values('Date').set_index('Date').groupby('Currency').apply(lambda x: x['Close'].describe())
    return des

def descriptions(final_table,x,y):
    filterinfDataframe = final_table[(final_table['Currency'] == x) & (final_table['Date'] == y)]
    pd.options.display.max_colwidth = 100
    return filterinfDataframe.T


