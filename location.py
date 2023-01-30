import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim

geolocator= Nominatim(user_agent='city_coordinates')

def get_city_coordinates(city):
    location=geolocator.geocode(city)
    return (location.latitude,location.longitude)

st.sidebar.title("city coordinates finder and map display")
city = st.sidebar.text_input("enter the name of a city")

if st.sidebar.button("shw on map"):
    coordinates= get_city_coordinates(city)
    st.header(city)
    st.success("coordinates of {}:{}".format(city,coordinates))
    co_dict ={"lat":[coordinates[0]],"lon":[coordinates[1]]}
    df=pd.DataFrame(co_dict)
    st.map(df)

