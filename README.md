# Bitcoins Scraping


The main purpose of this project is to analyze the Historical Data of several Cryptocurrencies:

* Bitcoin
* Stellar
* Ether
* Ethereum
* Litecoin
* EOS
* Ripple

Furthermore, the user will be able to choose a coin and a concrete date.
With this parameters, the user will get the exact Close Prices for this exact day, and also, the description of the coin, the corresponding  prog. languaje,  the year of the release, the mean of the whole period for the selected coin (from 2013 to 2019), Cap. Market.. among other things.

In order to do so, databases need to be cleaned. The process is described below.

## Getting Started

### Variables 

In order to extract the information, we would need to input the following parameters:

```
python3 main.py Coin Date (AAAA-MM-DD)
```
For instance:

```
python3 main.py Bitcoin 2019-12-02
```

### Files

Libraries you would need to import for this analysis:

```
import funciones
import argparse
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import re
import requests
import numpy as np
from bs4 import BeautifulSoup
```

### Data from Dataset folder

Table that contains the historical data for the mentioned cryptocurrencies.
Most of the names were changed in order to get a match with below report (Wikipedia) and extract the desired information.

### Data from Web Scrapping (Wikipedia)

Table that contains the needed information to extract the description of the coins, the prog. laguaje, the price, the cap. market, the release year,...
Most of the names were changed in order to get a match with below report (Wikipedia) and extract the desired information.
Also, the table contains some elements should be removed, such as: *'['* and *']'*

### Merge both folders

Once the two folders are cleaned, they will be merged with a function.

### How to run the folders

See deployment for notes on how to deploy the project on a live system:

1. Run the folder *funciones.py* - This part of the code will be used to store most of the functions for this analysis.
2. Run the folder *cleaning.py* - This part of the code will be used to clean all the unrelevant information and unwanted items that appears on the reports.
3. Finally, run the folder *main.py* - This part of the code will be used to select a specific parameters, which will be inputted by terminal.


## Built With

* [Wikipedia](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) - The web framework used
* [Kaggle](https://www.kaggle.com/philmohun/cryptocurrency-financial-data) - The Data set used.
