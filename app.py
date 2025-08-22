import streamlit as st
import requests
import base64
from PIL import Image

'''
# Taxi•Lucy•Fare Model
'''

st.markdown('''
♥♥♥♥♥♥♥♥♥♥♥♥
''')

'''
# ◄(^_^)►
'''

date_time = st.date_input('Date Time ↕')
number_pickup_long = st.number_input('Pickup Longitud ↕')
number_pickup_lat = st.number_input('Pickup Latitud ↕')
number_drop_long = st.number_input('Dropoff Longitude ↕')
number_drop_lat = st.number_input('Dropoff Latitude ↕')
number_passenger_c = st.number_input('Passenger Count ↕')

url = 'https://taxifare-462780954770.europe-southwest1.run.app/predict'

params = {
    "pickup_datetime": date_time,
    "pickup_longitude": number_pickup_long,
    "pickup_latitude": number_pickup_lat,
    "dropoff_longitude": number_drop_long,
    "dropoff_latitude": number_drop_lat,
    "passenger_count": number_passenger_c
}

if st.button('GIVE ME THE PRICE PREDICTION'):

    r = requests.get(url, params=params)
    status_code = r.status_code
    data = r.json()

    if status_code >199 and status_code <300:
        st.markdown(f'''Here is your prediction: ☻ {round(data["fare"]), 2}$''')
        '''
        # ◄('•')► ENJOY YOUR RIDE ◄('•')►
        '''
