# import plotly.express as px
# import plotly.graph_objects as go
# import plotly.io as pio
# from matplotlib.pyplot import xlabel
#
# pio.renderers.default='browser'
#
# x = [1,2,3,4,5]
# y = [10,15,13,17,20]
#
# fig1 = px.line(x=x, y=y, title="Wykres liniowy", markers=True)
#
# # fig1.show()
#
# produkty = ["A","B","C","D"]
# wyniki = [12,19,7,15]
#
# fig2 = px.bar(
#     x=produkty,
#     y=wyniki,
#     title="Wykres slupkowy",
#     orientation="h",
# )
# # fig2.show()
# a = [1,2,3,4,5]
# b = [3,7,4,9,6]
#
# fig3= px.scatter(x=a, y=b)
# # fig3.show()
#
#
# oceny = [2,2,5,5,4,3,2,5,4,3]
# fig4 = px.histogram(x=oceny, title="Oceny", nbins=4)
# fig4.show()

#
# import plotly.graph_objs as go
# import plotly.io as pio
#
# pio.renderers.default = "browser"
#
# godziny_nauki = [1, 2, 3, 4, 5, 6, 7]
# wyniki = [40, 50, 55, 60, 70, 75, 85]
#
# fig = go.Figure(data=go.Scatter(
#     x=godziny_nauki,
#     y=wyniki,
#     mode='markers',
#     marker=dict(size=12, color='blue', opacity=0.7),
#     name='Wyniki'
# ))
#
# plotly.offline.plot(fig, filename='Wyniki')

import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "Miesiąc": ["Styczeń","Luty","Marzec","Kwiecień"],
    "Sprzedaż": [1000,1200,900,1500]
})

st.set_page_config(
    page_title="Testowy Dashboard",
    layout="wide",
)

st.title("Testowy Dashboard")

