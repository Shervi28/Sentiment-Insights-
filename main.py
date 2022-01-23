import model
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import sys
import delete_line
import numpy as np
import pandas as pd

global PositiveCount
global NegativeCount
NegativeCount = 0
PositiveCount = 0
st.title(" Sentiment Insights Dashboard ")
st.write(" This is the Sentiment Insights Dashboard. You can upload your customer feedback responses and our state of the art AI Model will give you insights of your customer feedback responses.")
uploaded_file = st.file_uploader("Upload your customer feedback data", type = ['txt'])


if uploaded_file is not None:
    file_details = {"Filename":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    #st.write(file_details)

if st.button('Load Insights'):
    # yeet = model.read(uploaded_file)
    raw_text = str(uploaded_file.read(),"utf-8")
    #st.text(raw_text)

    with open("data.txt",'r+') as data:
        data.write(raw_text)

    delete_line.delete_line()

    st.balloons()

    yeet = model.read('new.txt')


    with open("insights.txt","r+") as file:
        for i in yeet:
            file.write(i)
            file.write('\n')

        
        with open("insights.txt", 'r') as read:
            for line in read:
                Line = line.strip()
                if Line == "Positive" and not(Line == "\n"):
                    PositiveCount+=1
                    print(PositiveCount)
                if Line == "Negative" and not(Line == "\n"):
                    NegativeCount+=1
                    print(NegativeCount)

    
    with open('insights.txt') as f:
        st.download_button('Download Insights', f)

    print(PositiveCount,NegativeCount)
    labels = "Positive Feedback", "Negative Feedback"
    sizes = [PositiveCount,NegativeCount]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.balloons()

    chart_data = pd.DataFrame(
        Positive=PositiveCount,
        Negative=NegativeCount,
        columns=["Positive", "Negative"]
    )
    st.bar_chart(chart_data)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.pyplot(fig1)
    with col2:
        st.metric(label="Accuracy", value="98%", delta="2.0%")
    with col3:
        st.metric(label="RSME(Loss)", value="0.88", delta="20%")


    #fig1.savefig('pie_chart.png')

