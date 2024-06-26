# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Hans Fangohr, University of Southampton, UK

def hello():
    """Print "Hello World" and return None."""
    print("Hello World")

# Main program starts here
hello()

"""

In [1]: runfile('/File/Path/hello.py', wdir=r'/File/Path')
Hello World

"""
# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Tue Jun 25 21:16:09 2024)---
import numpt as np
%clear
import numpy as np
numbers = np.array([2,3,5,7,11])
type(numbers)
np.array([[2,3,4],[5,7,11]])
pip install pandas
%clear
import pandas as pd
df = pd.read_csv("/home/elbigfut/Escritorio/porfotlio_github/dataeng_portfolio/py_eng/python-for-data-engineering-main/1. iPhone Data Analysis Project/Data")
df = pd.read_csv("/home/elbigfut/Escritorio/porfotlio_github/dataeng_portfolio/py_eng/python-for-data-engineering-main/1. iPhone Data Analysis Project/Data/apple_products.csv")
df.head
%clear
df.count()
%clear
df['Mrp'].max()
df['Mrp'].min()
df['Mrp'].max()==149900
df[df['Mrp']]==149900
df[df['Mrp']==149900]
df[df['Mrp']==39900]
df[df['Mrp']>=100000]
%clear
list(df['Product Name'])[0].upper()
list(df['Product Name'])[0].lower()
list(df['Product Name'])[51][6:15].upper().strip()
%clear
df['Model Name']= (df['Product Name'])[51][6:15].upper().strip()
df.head()
%clear
df.sort_values(by=['Star Rating'], ascending = False)
