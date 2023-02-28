import streamlit as st
from matplotlib import image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "layoffs.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "layoffs.csv")

st.title(":red[Tech Layoffs]")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
df.dropna(inplace=True)
st.dataframe(df)


arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['total_laid_off','funds_raised'])

st.line_chart(chart_data)


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["company", "total_laid_off", "funds_raised"])

st.area_chart(chart_data)

