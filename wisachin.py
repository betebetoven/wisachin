import openai
import pandas as pd
import numpy as np
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity
import winsound
import time
import streamlit as st

openai.api_key ="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"


#earnings_df = pd.read_csv('ccmitad.csv')
#earnings_df['embedding'] = earnings_df['CONSTITUCION'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
#earnings_df.to_csv('ccmitad_emb.csv')
earnings_df = pd.read_csv('ct2.csv')
embeddings = []
for item in earnings_df['CT']:
    time.sleep(1)
    embedding = get_embedding(item, engine='text-embedding-ada-002')
    time.sleep(1.5)
    embeddings.append(embedding)
earnings_df['embedding'] = embeddings
earnings_df.to_csv('ct2_emb.csv')
winsound.Beep(frequency=222, duration=1000)


"""
earnings_df = pd.read_csv('ccmitad_emb2.csv')
earnings_df['embedding'] = earnings_df['embedding'].apply(eval).apply(np.array)
#
earnings_search = input("Search earnings for a sentence:")
earnings_search_vector = get_embedding(earnings_search, engine="text-embedding-ada-002")
earnings_df["similarities"] = earnings_df['embedding'].apply(lambda x: cosine_similarity(x, earnings_search_vector))
k = earnings_df.sort_values("similarities", ascending=False)
#write the first 20 items of k in a text file called "output.txt" only write the "CONSTITUCION" column
k.head(20).to_csv("output.txt", columns=["CONSTITUCION"], index=False, header=False)
#st.header("Search earnings for a sentence:")
#create streamlit app that is a search engine for the earnings transcripts with a search bar and a table of the top 20 results  sorted by cosine similarity.
#st.write("Search earnings for a sentence:")
#earnings_search = st.text_input("Search earnings for a sentence:")
#earnings_search_vector = get_embedding(earnings_search, engine="text-embedding-ada-002")
#earnings_df["similarities"] = earnings_df['embedding'].apply(lambda x: cosine_similarity(x, earnings_search_vector))
#k = earnings_df.sort_values("similarities", ascending=False)
#st.table(k.head(20))
"""

    


