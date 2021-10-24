#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 21:35:24 2021

@author: ayeshauzair
"""


import pandas as pd
# import pandas_profiling as pp
# from matplotlib import pyplot as plt
import plotly_express as px
# import plotly.graph_objs as go
# import plotly.subplots as sp
import streamlit as st
# import plotly.io as pio
# pio.renderers.default='browser'
# %matplotlib inline

st.title("Data Visualization Dashboard for Mall Customers")
st.write("Select filters from sidebar to view more")
st.sidebar.title("Select a Plot")
dpdwn = st.sidebar.selectbox("",[  
                                "Gender Analysis",
                                "Age Group Analysis",
                                "Age Group vs Gender Count",
                                "Annual Income vs Spending Score",
                                "Age Group vs Annual Income (k$)",
                                "Age Group vs Spending Score (1-100)",
                                "Age Group vs Sum of Annual Income (k$)"
                                ])

df = pd.read_csv("Mall_Customers.csv")
# print(df.info())
# print(df.describe())
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

figure1 = px.histogram(df, x="Gender") 

figure8 = px.histogram(df, x="Age Group") 

figure5 = px.histogram(df,x="Age Group", color="Gender") 

figure3 = px.histogram(df,x="Age Group", y= "Annual Income (k$)") 
figure6 = px.pie(df, values="Annual Income (k$)", names= "Age Group") 

figure2 = px.scatter(df,x="Annual Income (k$)", y="Spending Score (1-100)" , color="Gender")
figure10 = px.histogram(df,x="Annual Income (k$)", y="Spending Score (1-100)" , color="Age Group")

figure4 = px.scatter(df,x="Age Group", y= "Spending Score (1-100)") 
figure9 = px.pie(df, values="Spending Score (1-100)", names= "Age Group") 

qty = df.groupby(["Age Group"])["Annual Income (k$)"].sum().reset_index().sort_values(by = "Annual Income (k$)")
figure7 = px.funnel(qty,x="Age Group",y="Annual Income (k$)")

qty1 = df.groupby(["Age Group","Gender"])["Annual Income (k$)"].sum().reset_index().sort_values(by = "Annual Income (k$)")
figure12 = px.funnel(qty1,x="Age Group",y="Annual Income (k$)", color=("Gender"))


if dpdwn == "Gender Analysis":
    st.subheader("Histogram: Gender Analysis")
    st.plotly_chart(figure1)
    st.write("There are more Females in the data as compared to Males. Hence, we have created an *Age Group* category for analysis.")

if dpdwn == "Age Group Analysis":
    st.subheader("Histogram: Age Group Analysis")
    st.plotly_chart(figure8)    
    st.write("Most customers in the mall are in the age bracket of 30-39 years. The least number of the customers are children under 20 years of age.")

if dpdwn == "Age Group vs Gender Count":
    st.subheader("Histogram: Age Group vs Gender")
    st.plotly_chart(figure5)
    st.write("For each Age Group, there are more number of Females than Males.")

if dpdwn =="Annual Income vs Spending Score":
    st.subheader("Scatter Plot: Annual Income vs Spending Score (Gender wise)")
    st.plotly_chart(figure2)
    st.subheader("Histogram: Annual Income vs Spending Score (Age Group wise)")
    st.plotly_chart(figure10)
    
if dpdwn == "Age Group vs Annual Income (k$)":
    st.subheader("Pie Chart: Age Group vs Sum of Annual Income (k$)")
    st.plotly_chart(figure6)
    # st.plotly_chart(figure3)
    st.write("1. Customers in Age Group 30-39 years have the highest count, hence the highest sum of Annual Income.")
    st.write("2. Customers in Age Group under 20 years have the lowest count, hence the lowest sum of Annual Income.")
    
if dpdwn == "Age Group vs Spending Score (1-100)":
    st.subheader("Pie Chart: Age Group vs Spending Score (1-100)")
    # st.plotly_chart(figure4)
    st.plotly_chart(figure9)
    st.write("1. Customers in Age Group 30-39 years have the highest count, hence the highest sum of Spending Score.")
    st.write("2. Customers in Age Group under 20 years have the lowest count, hence the lowest sum of Spending Score.")

if dpdwn == "Age Group vs Sum of Annual Income (k$)":
    st.subheader("Funnel Plots: Age Group vs Annual Income (k$)")
    st.plotly_chart(figure7)
    st.plotly_chart(figure12)
    
    






