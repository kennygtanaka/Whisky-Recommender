import pandas as pd
import numpy as np 
import streamlit as st 

from func import get_indexs, get_distance

whisky = pd.read_csv('whisky.csv')
whisky.columns = [c.replace(' ', '_') for c in whisky.columns]
whisky = whisky.drop(['STDEV', '#','Super_Cluster'], axis = 1)

cost = pd.get_dummies(whisky.Cost)
types = pd.get_dummies(whisky.Type)
classes = pd.get_dummies(whisky.Class)
countries = pd.get_dummies(whisky.Country)
clusters = pd.get_dummies(whisky.Cluster)

whisky =  pd.concat([whisky, cost, types, classes, countries, clusters], axis = 1)
whiskyv = whisky.drop(['Cost', 'Class', 'Cluster', 'Country',  'Type'], axis = 1)
whiskyv = whiskyv.iloc[:,np.r_[0:5, 6:52]]
whiskyv = whiskyv[whiskyv['Bourbon'] != 1]
whiskyv = whiskyv[whiskyv['Meta_Critic']!= '#REF!']
whiskyv.Meta_Critic = pd.to_numeric(whiskyv.Meta_Critic, downcast='float')



st.write("""
# Whisky Recommender

Input Favorite Whisky
""")

input = st.text_input("Favorite Whisky", "Bowmore 12")
ind = get_indexs(whiskyv, input)
whisky_list = get_distance(whiskyv, ind)
whisky_show = whisky[['Whisky', 'Cost', 'Class', 'Country', 'Type']]
whisky_final = whisky_show.iloc[whisky_list]
your_whisky = whisky_show.loc[[ind]]

st.write("""
# Favorite Whisky
""")

st.table(your_whisky.set_index('Whisky'))

st.write("""
# Similar Whiskies
""")

st.table(whisky_final.set_index('Whisky'))
