
import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents
import re


def get_wiki_table(url, x):
    table_class = "wikitable sortable jquery-tablesorter"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tbl = soup.findAll('table',{'class':"wikitable"})
    len_tbl = len(tbl)
    print(len_tbl)
    if x == 1:
        tbl_ = tbl[len_tbl - 1]
        df = get_df_from_soup(tbl_)
    else: 
        tbl1 = tbl[len_tbl - 1]
        tbl2 = tbl[len_tbl - 2]
        df1 = get_df_from_soup(tbl1)
        df2 = get_df_from_soup(tbl2)
        df = pd.concat([df2, df1])
        df.reset_index(drop=True, inplace=True)
        
    return df
    
def get_df_from_soup(tbl):
    df = pd.read_html(str(tbl))
    df=pd.DataFrame(df[0])
    
    return df