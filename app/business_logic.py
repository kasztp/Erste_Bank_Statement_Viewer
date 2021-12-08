from os import path
import pandas as pd
import tabula

basedir = path.abspath(path.dirname(__file__))


def load_csv(filename: str) -> pd.DataFrame:
    """ Read CSV dataset to pandas dataframe """
    data = pd.read_csv(basedir + '\\' + filename, encoding='latin1', sep=';')
    return data


def load_pdf(filename: str) -> pd.DataFrame:
    """ Read PDF dataset to pandas dataframe """
    tables = tabula.read_pdf(basedir + '\\' + filename, pages="all")
    merged_tables = pd.concat(tables[1:])
    merged_tables.head()
    return merged_tables


def remove_columns(dataframe: pd.DataFrame, columns: list) -> pd.DataFrame:
    """ Drop unnecessary columns from dataframe """
    data = dataframe.drop(columns=columns)
    return data


def sort_by_columns(dataframe: pd.DataFrame, columns: dict) -> pd.DataFrame:
    """ Sort dataframe based on a dict where keys are column names,
        values are booleans controlling ascending/descending order"""
    data = dataframe.sort_values(by=columns.keys(), ascending=columns.values())
    return data
