import re
import pandas as pd

def clean_dash(raw_texts):

    clean_texts = []
    for text in raw_texts:
        try:
            if type(text) == bytes:
                text = text.decode("utf-8")
            clean_text = text.replace("–", "-").replace("—", "-").replace("-", "-").replace("-", "-").replace("-", "-")
            clean_text2 = clean_text.replace(" - ", "-").replace(" -", "-").replace("- ", "-")
            clean_texts.append(clean_text2)
        except AttributeError:
            print("ERROR CLEANING")
            print(text)
            continue
        except UnicodeDecodeError:
            print("Unicode Error, Skip")
            continue
    new_txt = ''.join(clean_texts)
    new_txt = re.sub(' - ', '-', new_txt)
    new_txt = re.sub('- ', '-', new_txt)
    new_txt = re.sub(' -', '-', new_txt)
    return new_txt
    

def clean_del(text):
    return re.sub('del', 'de', text)


def get_day(text):
    exp = r"[0-9]{1,2}"

    match = re.search(exp, text)
    return match[0]

def get_mes(text):
    exp = r"[a-zA-Z]+"

    matches = re.findall(exp, text)
    return matches[1]

def get_yr(text):
    yr  = re.compile("[0-9]{4}")
    matches = yr.search(text)
    return matches[0]



def mes_a_num(text):

    dic_mes = {
            'enero' : 1,
            'febrero' : 2,
            'marzo' : 3,
            'abril' : 4,
            'mayo' : 5,
            'junio' : 6,
            'julio' : 7,
            'agosto' : 8,
            'septiembre' : 9, 
            'setiembre': 9,
            'octubre' : 10,
            'noviembre' : 11,
            'diciembre' : 12
        }


    mes = dic_mes[text]

    return mes



def limpia_base(df):
    
    if df.columns.nlevels >1:
        df.columns = df.columns.droplevel()
    if 'Imagen' in df.columns:
        df.drop(columns = ['Imagen'],  inplace = True)
    if 'Partido.1' in df.columns:
        df['Partido'] = df[['Partido', 'Partido.1']].fillna('').sum(axis=1)
        df.drop(columns = ['Partido.1'],  inplace = True)
    if 'Gobierno.1' in df.columns:
        df['Gobierno'] = df[['Gobierno', 'Gobierno.1']].fillna('').sum(axis=1)
        df.drop(columns = ['Gobierno.1'],  inplace = True)

    df.rename(columns = {'PCM': 'Ministro', 'Ministra': 'Ministro',
                          'Inicio': 'inicio', 'Fin': 'fin', 'Final': 'fin',
        'Período': 'Periodo', 'Gobierno': 'Presidente'}, inplace = True)

    return df


def get_fechas(df_ex, str_var):

    '''
    transforma un texto de fecha en una fecha string
    '''
    df_ex['f_' + str_var] = df_ex[str_var].apply(lambda x:  str(mes_a_num(get_mes(x))) + "/" + 
                                         get_day(x) + "/" + 
                                         get_yr(x))
    


    return df_ex 


def set_nombres(csv_file):
    nombres = pd.read_csv(csv_file, encoding = 'latin-1')
    nombres['nombre_spl'] = nombres['nombre'].str.split(' ')
    nombres['primer_nombre'] = nombres['nombre_spl'].apply(lambda x: 
        x[0].title())
    set_nombres = set(nombres['primer_nombre'])
    return set_nombres


def pertenece_nombres(x, set_hombres, set_mujeres):
    if x in set_hombres:
        return 'Hombre'
    elif x in set_mujeres:
        return 'Mujer'
    else:
        return 'no match'


