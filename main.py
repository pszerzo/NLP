import streamlit as st
import plotly.express as px
import nltk
import glob
from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()
p = []
n = []
d = []
diary = glob.glob("diary/"+"*.txt")
diary.sort()

for file in diary:
    with open(file, "r") as content:
        text = content.read()
        scores = analyzer.polarity_scores(text)
        p.append(scores["pos"])
        n.append(scores["neg"])
        d.append(file[11:17])

st.title("Diary Tone")

st.subheader("Positivity")
figure1 = px.line(x=d, y=p, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure1)

st.subheader("Negativity")
figure2 = px.line(x=d, y=n, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure2)