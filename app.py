import streamlit as st

st.title(":red[Hello there]:wave:")
st.header(":yellow[I am saryu siriki]")
st.subheader("I am a highly motivated data science student with a passion for turning complex data into actionable insights. With a strong background in statistics and programming, I have developed expertise in machine learning, data mining, and data visualization. I am proficient in programming languages such as Python, R, and SQL. I am eager to apply my skills and contribute to the rapidly growing field of data science.")


btn_click = st.button("Have a great day:wink:")

if btn_click == True:
     
     st.balloons()
