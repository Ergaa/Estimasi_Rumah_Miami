import pickle
import streamlit as st

model = pickle.load(open('estimasi_rumah.sav', 'rb'))

st.title('Estimasi Harga Rumah')

#LATITUDE, LONGITUDE, PARCELNO, LND_SQFOOT, TOT_LVG_AREA, SPEC_FEAT_VAL, RAIL_DIST, OCEAN_DIST, WATER_DIST, CNTR_DIST, SUBCNTR_DI, HWY_DIST, age, month_sold, structure_quality
LATITUDE = st.number_input('Input Garis Lintang')
LONGITUDE = st.number_input('Input Garis Bujur')
PARCELNO = st.number_input('Input Nomer Rumah')
LND_SQFOOT = st.number_input('Input  luas tanah (sqft)')
TOT_LVG_AREA = st.number_input('Input luas lantai (sqft)')
SPEC_FEAT_VAL = st.number_input('nilai fitur khusus (misalnya, kolam renang) ($)')
RAIL_DIST = st.number_input('Input jarak ke jalur rel terdekat (indikator kebisingan) (ft)')
OCEAN_DIST = st.number_input('Input jarak ke laut (ft)')
WATER_DIST = st.number_input('Input jarak ke badan air terdekat (ft)')
CNTR_DIST = st.number_input('Input jarak ke distrik pusat bisnis Miami (ft)')
SUBCNTR_DI = st.number_input('Input jarak ke subpusat terdekat (ft)')
HWY_DIST = st.number_input('Input jarak ke jalan raya terdekat (indikator kebisingan) (ft)')
age = st.number_input('Input umur Rumah')
month_sold = st.number_input('Input bulan penjualan')
structure_quality = st.number_input('Input Kualitas Rumah')

predict = ''

if st.button('Estimasikan'):
    predict = model.predict(
        [[LATITUDE, LONGITUDE, PARCELNO, LND_SQFOOT, TOT_LVG_AREA, SPEC_FEAT_VAL, RAIL_DIST, OCEAN_DIST, WATER_DIST, CNTR_DIST, SUBCNTR_DI, HWY_DIST, age, month_sold, structure_quality]]
    )
    st.write ('Estimasi Harga Rumah USD: ', predict, 'USD')
    st.write ('Estimasi Harga Rumah IDR : ', predict*14679,60, 'IDR')