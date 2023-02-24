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
st.write("TU ABOGADO DE CONFIANZA")
earnings_search = st.text_input("Ingresa lo que estas buscando y la IA relacionará tu búsqueda con artículos de la Constitución \n  que puedan ser de utilidad:")
if st.button("Buscar"):
    earnings_search_vector = get_embedding(earnings_search, engine="text-embedding-ada-002")
    earnings_df["similarities"] = earnings_df['embedding'].apply(lambda x: cosine_similarity(x, earnings_search_vector))
    k = earnings_df.sort_values("similarities", ascending=False)
    k = k[k['similarities'] >= 0.799]
    k['similarities'] = k['similarities'].apply(lambda x: '{:.0%}'.format(x))
    k = k.rename(columns={'similarities': 'correlacion de busqueda'})
    st.table(k[['CONSTITUCION', 'correlacion de busqueda']])
#only write the "CONSTITUCION" column of st.table(k.head(20)) and show it in the table  of the streamlit app
#k.head(20).to_csv("output.txt", columns=["CONSTITUCION"], index=False, header=False)   
