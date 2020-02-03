# Bitcoins Scraping


The main purpose of this project is to analyze the Historical Data of several Cryptocurrencies:

* Bitcoin
* Stellar
* Ether
* Ethereum
* Litecoin
* EOS
* Ripple

Furthermore, the user will be able to choose a coin and also a concrete date, with this parameters, the user will get the exact Close Prices of the selected date, the description of the coin, the prog. laguanje,  the release year, the mean of the whole period (from 2013 to 2019), among other things.

In order to do so, databases need to be cleaned. The process is described below.

## Getting Started

See deployment for notes on how to deploy the project on a live system:

1. Run the folder *funciones.py*
2. Run the folder *cleaning.py*
3. Finally, run the folder *main.py*

### Prerequisites

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



### Data from Web Scrapping (Wikipedia)

Explain what these tests test and why

### Merge both folders



## Built With

* [Wikipedia](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) - The web framework used
* [Kaggle](https://www.kaggle.com/philmohun/cryptocurrency-financial-data) - The Data set used.
