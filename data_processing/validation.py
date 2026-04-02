import pandas as pd
from dataclasses import dataclass
from typing import List

@dataclass
class Airport:
    id: int
    name: str
    abbreviation: str
    city: str
    country: str
    latitude: float
    longitude: float

@dataclass
class Airline:
    id: int
    name: str
    abbreviation: str
    country: str  

#Importing data
airport_url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat'
airlines_url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat'
planes_url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/planes.dat'
routes_url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat'
countries_url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/countries.dat'

airport_df = pd.read_csv(airport_url, header=None)
airline_df = pd.read_csv(airlines_url, header=None)
plane_df = pd.read_csv(planes_url, header=None)
routes_df = pd.read_csv(routes_url, header=None)
countries_url = pd.read_csv(countries_url, header=None)

#Converting to dataclass lists
airport_list = []
for row in airport_df.itertuples(index=False):
    airport_obj = Airport(
        id=row[0],
        name=row[1],
        abbreviation=row[4],
        city=row[2],
        country=row[3],
        latitude=row[6],
        longitude=row[7]
    )
    airport_list.append(airport_obj)

airline_list = []
for row in airline_df.itertuples(index=False):
    airline_obj = Airline(
        id=row[0],
        name=row[1],
        abbreviation=row[2],
        country=row[6]
    )
    airline_list.append(airline_obj)



#Print out the shape


