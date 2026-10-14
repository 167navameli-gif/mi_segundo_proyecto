import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('YARDAS_PASOS_DATOS_TICS.xlsx', index_col=0)
# df.tail()
st.title("Este es un análisis estadístico de la base de datos")
df.head()
df_centrado = df.style.set_properties(**{"text-align": "center"})
st.table(df_centrado) 

st.header("Estadística descriptiva")
st.dataframe(df.describe())

#Esto está estandarizando las columnas
df.columns = [c.lower().replace(' ', '_') for c in df.columns]
df.head()


col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    ax.boxplot(df["yardas_totales"])
    st.header("Diagrama de caja y bigotes de Yarda Totales")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    ax.boxplot(df['pases_completos'])
    st.header("Diagrama de caja y bigotes de Pases Completos")
    st.pyplot(fig)
