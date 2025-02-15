import pandas as pd
import os
import glob

def extract(path:str) -> pd.DataFrame:
    '''
    Cria DataFrame a partir dos jsons do diretorio
    '''
    files = glob.glob(os.path.join(dir,'*.json'))
    dfs = [pd.read_json(file) for file in files]
    df = pd.concat(dfs, ignore_index=True)
    return df

def get_kpi_total_sales(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

def load(df:pd.DataFrame, path:str):
    df.to_csv(path + "\dados.csv")

if __name__ == '__main__':
    dir = 'data'
    df_teste = extract(dir)
    df_kpi = get_kpi_total_sales(df_teste)
    load(df_kpi, dir)
    #df_teste.info()