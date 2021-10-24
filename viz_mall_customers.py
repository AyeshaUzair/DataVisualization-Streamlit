#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 21:35:24 2021

@author: ayeshauzair
"""

import streamlit as st
import pandas as pd
# from matplotlib import pyplot as plt
import plotly_express as px
# import plotly.graph_objs as go
# import plotly.subplots as sp
# import plotly.io as pio
# pio.renderers.default='browser'

st.title("Mall Customers Data Visualization Dashboard")
st.write("Click on arrow that's on left for filters if you don't see the filters")
st.sidebar.title("Plots & Analysis")
dpdwn = st.sidebar.selectbox("Select a plot",[  "Gender Analysis",
                                                "Age Group Analysis",
                                                "Age Group vs Gender",
                                                "Annual Income vs Spending Score",
                                                "Age Group vs Annual Income",
                                                "Age Group vs Spending Score",
                                                "Age Group vs Score per $ income"
                                                ])

df = pd.read_csv("Mall_Customers.csv")
print(df.info())
print(df.describe())
df = df.rename(columns = {'Genre':'Gender'})

mean_1 = df['Annual Income (k$)'].mean()
mean_2 = df['Spending Score (1-100)'].mean()
mean_3 = df['Age'].mean()

mean_income_gender = df.groupby("Gender")["Annual Income (k$)"].mean() 
mean_spending_gender = df.groupby("Gender")["Spending Score (1-100)"].mean() 

df.loc[df["Age"]<20,"Age Group"] = "under 20"
df.loc[(df["Age"]<30)&(df["Age"]>19),"Age Group"] = "20 - 29"
df.loc[(df["Age"]<40)&(df["Age"]>29),"Age Group"] = "30 - 39"
df.loc[(df["Age"]<50)&(df["Age"]>39),"Age Group"] = "40 - 49"
df.loc[(df["Age"]<60)&(df["Age"]>49),"Age Group"] = "50 - 59"
df.loc[df["Age"]>59,"Age Group"] = "over 60"

mean_agec = pd.DataFrame(df.groupby("Age Group")["Annual Income (k$)"].mean())
mean_spend = pd.DataFrame(df.groupby("Age Group")['Spending Score (1-100)'].mean())


df["Score per $ income"] = df["Spending Score (1-100)"] / df["Annual Income (k$)"]
mean_score_income = df["Score per $ income"].mean()

# PLOTS

figure1 = px.histogram(df, x="Gender") # final

figure8 = px.histogram(df, x="Age Group") # final

figure5 = px.histogram(df,x="Age Group", color="Gender") # final

figure3 = px.histogram(df,x="Age Group", y= "Annual Income (k$)") # final
figure6 = px.pie(df, values="Annual Income (k$)", names= "Age Group") # final

figure2 = px.scatter(df,x="Annual Income (k$)", y="Spending Score (1-100)" , color="Gender")
figure10 = px.histogram(df,x="Annual Income (k$)", y="Spending Score (1-100)" , color="Age Group")

figure4 = px.histogram(df,x="Age Group", y= "Spending Score (1-100)") # final
figure9 = px.pie(df, values="Spending Score (1-100)", names= "Age Group") # final

figure7 = px.funnel(df,x="Age Group",y="Score per $ income",color="Gender")


if dpdwn == "Gender Analysis":
    st.plotly_chart(figure1)
    st.write("There are more Females in the data as compared to Males. Hence, we use *Age Group* as a hue for analysis.")

if dpdwn == "Age Group Analysis":
    st.plotly_chart(figure8)    
    
if dpdwn == "Age Group vs Gender":
    st.plotly_chart(figure5)

if dpdwn =="Annual Income vs Spending Score":
    st.plotly_chart(figure2)
    st.plotly_chart(figure10)
    
if dpdwn == "Age Group vs Annual Income":
    st.plotly_chart(figure3)
    st.plotly_chart(figure6)

if dpdwn == "Age Group vs Spending Score":
    st.plotly_chart(figure4)
    st.plotly_chart(figure9)
    
if dpdwn == "Age Group vs Score per $ income":
    st.plotly_chart(figure7)
    






