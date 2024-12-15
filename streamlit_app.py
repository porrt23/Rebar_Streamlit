import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

"""
# Welcome to Streamlit!
This is a test.

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))

# Create a figure and a set of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Plot the first graph
x = 0
y = 0
axs[x, y].plot([1, 2, 3], [4, 5, 6])
axs[x,y].set_title('Sine Function')
axs[x,y].set_xlabel('x')
axs[x,y].set_ylabel('y')

# Plot the second graph
x = 1
y = 0
axs[x,y].plot([7, 8, 9], [10, 11, 12])
axs[x,y].set_title('Cosine Function')
axs[x,y].set_xlabel('x')
axs[x,y].set_ylabel('y')

x = 0
y = 1
axs[x,y].plot([1, 2, 3], [4, 5, 6])
axs[x,y].set_title('Sine Function')
axs[x,y].set_xlabel('x')
axs[x,y].set_ylabel('y')

x = 1
y = 1
axs[x,y].plot([7, 8, 9], [10, 11, 12])
axs[x,y].set_title('Cosine Function')
axs[x,y].set_xlabel('x')
axs[x,y].set_ylabel('y')

# Display the figure in Streamlit
st.pyplot(fig)
