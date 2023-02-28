import streamlit as st
from matplotlib import image
import pandas as pd
import numpy as np
import plotly.express as px
import os

st.title("Dashboard - Titanic Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["survived", "sex", "alive"])

st.bar_chart(chart_data)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["survived", "sex", "alive"])

st.line_chart(chart_data)


