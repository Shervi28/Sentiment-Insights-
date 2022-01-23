import model
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

global PositiveCount
global NegativeCount
NegativeCount = 0
PositiveCount = 0
st.title(" Sentiment Insights Dashboard ")
st.write(" This is the Sentiment Insights Dashboard. You can upload your customer feedback responses and our state of the art AI Model will give you insights of your customer feedback responses.")
uploaded_file = st.file_uploader("Upload your customer feedback data")

if st.button('Load Insights'):
    yeet = model.read(uploaded_file)

    with open("insights.txt","r+") as file:
        for i in yeet:
            file.write(i)
            file.write('\n')
        
        with open("insights.txt",'r') as read:
            for line in read:
                Line = line.strip()
                if Line == "Positive":
                    PositiveCount+=1
                else:
                    NegativeCount+=1
                    
    print(PositiveCount,NegativeCount)
    labels = "Positive Feedback", "Negative Feedback"
    sizes = [PositiveCount,NegativeCount]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
    fig1.savefig('books_read.png')    


#try:
    #yeet = model.read(uploaded_file)

    #with open("insights.txt","r+") as file:
        #for i in yeet:
           # file.write(i)
            #file.write('\n')
        
       # with open("insights.txt",'r') as read:
            #for line in read:
               # Line = line.strip()
               # if Line == "Positive":
               #     PositiveCount+=1
               # else:
               #     NegativeCount+=1
                    
    #print(PositiveCount,NegativeCount)
    #labels = "Positive Feedback", "Negative Feedback"
   ## sizes = [PositiveCount,NegativeCount]

    #fig1, ax1 = plt.subplots()
    #ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
     #       shadow=True, startangle=90)
    #ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    #st.pyplot(fig1)
    #fig1.savefig('books_read.png')

#xcept:
    #st.error("Make sure to upload your cutomer Data")

#lines = ['Wow, your product is soo amazing! I want to use it again', 'I ordered just once from TerribleCo, they screwed up, never used the app again']
#with open('survey.txt', 'w') as f:
    #for i in range(50-1):
       # for line in lines:
            #f.write(line)
            #f.write('\n')


#yeet = model.read(uploaded_file)

#with open("insights.txt","r+") as file:
    #for i in yeet:
        #file.write(i)
        #file.write('\n')
    #with open("insights.txt",'r') as read:
        #PositiveCount = 0
        #NegativeCount = 0
        #for line in read:
            #Line = line.strip()
            #if Line == "Positive":
                #PositiveCount+=1
            #else:
                #NegativeCount+=1
        #print(PositiveCount,NegativeCount)

#data = [PositiveCount, NegativeCount]
#labels = ["Positive Feedback", "Negative Feedback"]

#colors = sns.color_palette('pastel')[0:5]

#fig = plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
#st.pyplot(fig)

#####
#labels = "Positive Feedback", "Negative Feedback"
#sizes = [PositiveCount,NegativeCount]

#fig1, ax1 = plt.subplots()
#ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
      #  shadow=True, startangle=90)
#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#st.pyplot(fig1)
#fig1.savefig('books_read.png')