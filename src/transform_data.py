import pandas as pd
import json
from pathlib import Path

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Forma de escrever o caminho do arquivo: '../data/weather_data.json'
path_name = Path(__file__).parent.parent / 'data' / 'weather_data.json'

columns_to_drop = ["sys.type", "weather", "weather_icon"]

columns_to_rename = {
    "base": "base",
    "visibility": "visibility",
    "dt": "datetime",
    "timezone": "timezone",
    "id": "city_id",
    "name": "city_name",
    "cod": "code",
    "coord.lon": "longitude",
    "coord.lat": "latitude",
    "main.temp": "temperature",
    "main.feels_like": "feels_like",
    "main.temp_min": "temp_min",
    "main.temp_max": "temp_max",
    "main.pressure": "pressure",
    "main.humidity": "humidity",
    "main.sea_level": "sea_level",
    "main.grnd_level": "grnd_level",
    "wind.speed": "wind_speed",
    "wind.deg": "wind_deg",
    "wind.gust": "wind_gust",
    "clouds.all": "clouds",
    "sys.type": "sys_type",
    "sys.id":"sys_id",
    "sys.country":"country",
    "sys.sunrise":"sunrise",
    "sys.sunset":"sunset"
}

columns_to_normalize_to_datetime = ['datetime', 'sunrise', 'sunset']

def create_dataframe(path_name:str) -> pd.DataFrame:
    logging.info("-> Criando Dataframe do Arquivo JSON...")
    path = path_name

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não Encontrado: {path}")
    
    with open(path) as f:
        data = json.load(f)

    df = pd.json_normalize(data)

    logging.info(f"\nOK - Datframe Criado com {len(df)} linha(s)")
    return df

def normalize_weather_columns(df: pd.DataFrame) -> pd.DataFrame:
    df_weather = pd.json_normalize(df['weather'].apply(lambda x: x[0]))

    df_weather = df_weather.rename(columns={
        'id': 'weather_id',
        'main': 'weather_main',
        'description': 'weather_description',
        'icon': 'weather_icon'
    })

    df = pd.concat([df, df_weather], axis=1)

    logging.info(f"\nOK - Coluna 'weather' normalizada - {len(df.columns)} colunas")

    return df

def drop_columns(df: pd.DataFrame, columns_names: list[str]) -> pd.DataFrame:
    
    logging.info(f"\nRemovendo Colunas: {columns_names}")
    
    df =df.drop(columns=columns_names)
    
    logging.info(f"\nOK - Colunas Removidas - {len(df.columns)} colunas restantes")

    return df

def rename_columns(df: pd.DataFrame, columns_names: dict[str, str]) -> pd.DataFrame:

    logging.info(f"\nRenomeando {len(columns_names)} Colunas")
    df = df.rename(columns=columns_names)
    logging.info(f"\nOK - Colunas Renomeadas")

    return df

def normalize_datetime_columns(df: pd.DataFrame, columns_names: list[str]) -> pd.DataFrame:

    logging.info(f"\nNormalizando Colunas para Datetime: {columns_names}")
    for name in columns_names:
        df[name] = pd.to_datetime(df[name], unit='s', utc=True).dt.tz_convert('America/Sao_Paulo')
        logging.info(f"\nColuna {name} normalizada!")
    logging.info(f"\nOK - Colunas convertidas para Datetime\n")
    return df

def data_transformations():
    logging.info(f"\nIniciando Transformação do DataFrame")
    df = create_dataframe(path_name)
    df = normalize_weather_columns(df)
    df = drop_columns(df, columns_to_drop)
    df = rename_columns(df, columns_to_rename)
    df = normalize_datetime_columns(df, columns_to_normalize_to_datetime)
    logging.info(f"\nTransformações Concluídas")
    return df