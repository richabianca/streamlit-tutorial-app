from ctypes import c_void_p
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
 

st.title('welcome to the first penguin dataset apps')

st.write('**Starting** the *build* of `penguin` app :penguin::mag:')
st.write('Data is taken from [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/)')
st.header('Data')

df = pd.read_csv('penguins_extra.csv')
st.write('Display a sample of 20 datapoints:', df.sample(20))
species = st.selectbox('Select species', df.species.unique())
st.write(f'Displaying a subdataframe from {species}', df[df['species'] == species])

#heading over to the plotting

fig, ax = plt.subplots()
ax = sns.scatterplot(data=df, 
    x ='bill_length_mm', 
    y='flipper_length_mm', 
    hue = 'species')
st.pyplot(fig)

st.bar_chart(df.groupby('island')['species'].count())

st.map(df)

csv_var = st.sidebar.file_uploader('Upload a csv file:', type=['csv'])
if csv_var != None:
    df = pd.read_csv(csv_var)
    st.write('Uploaded file:', df)

    ##