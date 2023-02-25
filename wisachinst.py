import openai
import pandas as pd
import numpy as np
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity

import time
import streamlit as st

openai.api_key ="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"


earnings_df = pd.read_csv('ccmitad_emb2.csv')
earnings_df['embedding'] = earnings_df['embedding'].apply(eval).apply(np.array)
earnings_df2 = pd.read_csv('ct2_emb.csv')
earnings_df2['embedding'] = earnings_df2['embedding'].apply(eval).apply(np.array)

st.header("WISACHIN")
st.markdown("""<style>
            
body {
    background-color: #000000;
}
table {
    
    
    border-collapse: collapse;
    width: 800px;
    height: 200px;
    border: 1px solid #bdc3c7;
    box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2), -1px -1px 8px rgba(0, 0, 0, 0.2);
}

tr {
    transition: all .2s ease-in;
    cursor: pointer;
}

th,
td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

#header {
    background-color: #16a085;
    color: #fff;
}

h1 {
    font-weight: 600;
    text-align: center;
    background-color: #16a085;
    color: #fff;
    padding: 10px 0px;
}

tr:hover {
    background-color: #f5f5f5;
    transform: scale(1.02);
    box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2), -1px -1px 8px rgba(0, 0, 0, 0.2);
}
tr:hover td {
  color: black;
}
tr:hover th {
  color: black;
}

@media only screen and (max-width: 768px) {
    table {
        width: 90%;
    }</style>""", unsafe_allow_html=True)
st.write("ESTA ES UNA HERRAMIENTA PARA FACILITAR EL CONOCIMIENTO DE LA LEYES. NUESTRO PRINCIPAL OBJETIVO ES SER UTILIZADO COMO UN EXPLORADOR, EN NINGUN CASO DEBE UTILIZARSE COMO REFERENCIA DIRECTA O SUPLANTACION DE LOS DOCUMENTOS LEGALES EXISTENTES, EL FIN DE ESTA HERRAMIENTA ES SER UNA GUIA PARA EL CONOCIMIENTO DE LOS DERECHOS, OBLIGACIONES Y AMPAROS QUE OTORGA LA LEY DE LA REPUBLICA DE GUATEMALA")
earnings_search = st.text_input("Ingresa lo que estas buscando y la IA relacionará tu búsqueda con artículos de la Constitución \n  que puedan ser de utilidad:")

#options = st.sidebar.multiselect("escoge documento", ["CONSTITUCION", "CODIGO DE TRABAJO"])
selected_options = set()
if st.checkbox("CONSTITUCION"):
    selected_options.add("CONSTITUCION")

if st.checkbox("CODIGO DE TRABAJO"):
    selected_options.add("CODIGO DE TRABAJO")
global gk
global gk2
gk = pd.DataFrame()
gk2 = pd.DataFrame()


if st.button("Buscar") and earnings_search != "":
    earnings_search_vector = get_embedding(earnings_search, engine="text-embedding-ada-002")
    
    
    earnings_df["similarities"] = earnings_df['embedding'].apply(lambda x: cosine_similarity(x, earnings_search_vector))
    k = earnings_df.sort_values("similarities", ascending=False)
    k = k[k['similarities'] >= 0.799]
    k['similarities'] = k['similarities'].apply(lambda x: '{:.0%}'.format(x))
    k = k.rename(columns={'similarities': 'correlacion de busqueda'})
    
    #do the same for earnings_df2
    earnings_df2["similarities"] = earnings_df2['embedding'].apply(lambda x: cosine_similarity(x, earnings_search_vector))
    k2 = earnings_df2.sort_values("similarities", ascending=False)
    k2 = k2[k2['similarities'] >= 0.799]
    k2['similarities'] = k2['similarities'].apply(lambda x: '{:.0%}'.format(x))
    k2 = k2.rename(columns={'similarities': 'correlacion de busqueda'})
    k2 = k2.rename(columns={'CT': 'CODIGO DE TRABAJO'})
    
    
    
    
    gk = k[['CONSTITUCION', 'correlacion de busqueda']]
    gk2 = k2[['CODIGO DE TRABAJO', 'correlacion de busqueda']]
    if "CONSTITUCION" in selected_options:
        st.table(gk)

    if "CODIGO DE TRABAJO" in selected_options:
        st.table(gk2)
        
    

