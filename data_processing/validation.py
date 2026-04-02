from io import IncrementalNewlineDecoder
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

@dataclass
class Plane:
    name: str
    IATA: int
    ICAO: int

@dataclass
class Country:
    name: str
    iso_code: str

@dataclass
class Route:
    airline: str
    airline_id: int
    source_airport: str
    source_airport_id: int
    destination_airport: str
    destination_aiport_id: int
    codeshare: str
    stops: int
    equipment: str

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

plane_list = []
for row in plane_df.itertuples(index=False): 
  plane_obj = Plane(
    name=row[0],
    IATA=row[1],
    ICAO=row[2]
  )
  plane_list.append(plane_obj)

country_list = []
for row in countries_url.itertuples(index=False):
  country_obj = Country(
    name=row[0],
    iso_code=row[1]
  )
  country_list.append(country_obj)

route_list = []
for row in routes_df.itertuples(index=False):
  route_obj = Route(
    airline=row[0],
    airline_id=row[1],
    source_airport=row[2],
    source_airport_id=row[3],
    destination_airport=row[4],
    destination_aiport_id=row[5],
    codeshare=row[6],
    stops=row[7],
    equipment=row[8]
  )
  route_list.append(route_obj)

#Print out the shape
print(f'Airport Size: {len(airport_list)}')
print(f'Airline Size: {len(airline_list)}')
print(f'Plane Size: {len(plane_list)}')
print(f'Country Size: {len(country_list)}')
print(f'Route Size: {len(route_list)}')

