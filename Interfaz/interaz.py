import time  # to simulate a real time data, time loop
from DB_mangeloc.lectura import *
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import matplotlib.pyplot as plt
import streamlit as st  # 🎈 data web app development
import keyboard
import asyncio
from DB_mangeloc.insert import *
from datos import *
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

st.set_page_config(
    page_title="Control",
    page_icon="✅",
    layout="wide",
)
df2=pd.DataFrame()
st.title("Control")

# creating a single-element container
placeholder = st.empty()
save = st.checkbox('Save data')
while True:
    df=get_datos()
    if(save==True):
        copy_from_stringio(df, 'cnc')
    df['corriente'] = np.random.randint(-5, 5, df.shape[0])
    df['rpm'] = np.random.randint(-5, 5, df.shape[0])
    if(df2.size==0):
        df2=df
    else:
        dff=pd.concat([df2, df],ignore_index=True)
        df2=dff
    with placeholder.container():
        fig_col1, fig_col2, fig_col3 = st.columns(3)
        with fig_col1:
            st.markdown("### Corriente")
            df_corriente=df2["corriente"]
            fig, ax = plt.subplots()
            ax.plot(df_corriente)
            ax.set_ylim(-6, 6) 
            st.pyplot(fig)
            
        with fig_col2:
            st.markdown("### Vibración")
            df_vibracion=df2["Accel"]
            fig, ax = plt.subplots()
            ax.plot(df_vibracion)
            ax.set_ylim(-6, 6) 
            st.pyplot(fig)
            
        with fig_col3:
            st.markdown("### RPM")
            df_rpm=df2["rpm"]
            fig, ax = plt.subplots()
            ax.plot(df_rpm)
            ax.set_ylim(-6, 6) 
            st.pyplot(fig)
            
    if keyboard.is_pressed("q"):
        print("q pressed, ending loop")
        break
        






    