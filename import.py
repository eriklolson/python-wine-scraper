import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
import pandas as pd


load_dotenv(find_dotenv())

# Create SQLAlchemy engine connecting to Postgres account
engine = create_engine(os.getenv('DATABASE_URI'))

# Create products table in database
with engine.connect() as connection:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS bottle(
        id SERIAL PRIMARY KEY,
        product_name text,
        year integer,
        volume numeric,
        proofs text,
        producer_name text,
        country_name text,
        region_name text,
        appellation text,
        color_name text,
        primary_grape text,
        all_grape text,
        price money,
        image text,
        description text,
        product_link text
        )
    """)

# Read the CSV file of scraped product data
csv_file = 'wine_data.csv'

# Convert CSV file to Pandas dataframe for manipulation
df = pd.read_csv(csv_file, header=0, index_col=0)

# Convert dataframe to SQL format
df.to_sql('bottle', con=engine, if_exists='replace', index_label='id')
