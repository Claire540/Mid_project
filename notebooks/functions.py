import pandas as pd

def clean_numerical_columns(df: pd.DataFrame, list_of_columns: list)-> pd.DataFrame:
    """
    This function will remove unicode strings from the numerical columns and return
    the values as integers

    Inputs:
    df: Pandas DataFrame
    list_of_columns: list of cloumns to clean

    Outputs:
    Pandas dataframe cleaned.
    """
    
    df2 = df.copy()
    
    for column in list_of_columns:
        df2[column] = pd.to_numeric([ int(value.replace("\u202f","")) for value in df2[column].unique().tolist()])
        
    return df2


def replace_comma_by_dot(df: pd.DataFrame, list_of_columns: list)-> pd.DataFrame:
    """
    This function will replace the "," by "."
    the values as integers

    Inputs:
    df: Pandas DataFrame
    list_of_columns: list of cloumns to clean

    Outputs:
    Pandas dataframe cleaned.
    """
    
    df2 = df.copy()
    
    for column in list_of_columns:
        df2[column] = pd.to_numeric([ float(value.replace(",",".")) for value in df2[column].unique().tolist()])
        
    return df2


def rename_columns(df: pd.DataFrame)-> pd.DataFrame:
    """
    This function will rename some columns french names by english columns name.
    
    Inputs:
    Pandas DataFrame

    Outputs:
    Pandas dataframe renamed.
    """

    df2 = df.copy()
    
    if "code agence" in df2.columns:
        df2.rename(columns={"code agence": "code_agency", "nom du bassin": "pools_name", "moyenne 2010-2019": "mean"}, inplace=True)
    elif "Unnamed: 0" in df2.columns:
        df2.rename(columns={"Unnamed: 0": "consumers", "Moyenne 2010-2019": "mean"}, inplace=True)
    elif "Étiquettes de lignes" in df2.columns:
        df2.rename(columns={"Étiquettes de lignes": "Pollution_types", "Total général": "Total"}, inplace=True)

    return df2



    def rename_dataframe_raws(df):
        """
    This function will rename some raws french names by english raws name.
    
    Inputs:
    Pandas DataFrame

    Outputs:
    Pandas dataframe renamed.
    """
    new_titles = {
        'Eau potable': 'Drinking water',
        'Autres usages, principalement industriels': 'Industries',
        'Agriculture (irrigation)': 'Agriculture(irrigation)',
        'Refroidissement des centrales électriques': 'Cooling of nuclear power plants',
        'Alimentation des canaux (navigabilité et circu...': 'Canal supply',
        'Total hors canaux de navigation': 'Total(without Canal supply)',
        'Total y compris canaux de navigation': 'Total(with Canal supply)'
    }

    df.loc[0:7, 'consumers'] = df.loc[0:7, 'consumers'].map(new_titles)

    return df