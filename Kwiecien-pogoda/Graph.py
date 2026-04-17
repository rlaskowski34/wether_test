import streamlit as st
import plotly.graph_objects as go
import pandas as pd


st.set_page_config(page_title="Analiza Środowiskowa", layout="wide")

st.divider()

st.header("Graficzna reprezentacja warunków pogodowych w słupkach", divider='red')

st.markdown("""
Poniższe wykresy przedstawiają dane pomiarowe z ostatnich godzin.
*   **Wykres 1**: Wilgotność powietrza w %
*   **Wykres 2**: Temperatura w $^\circ C$
""")

data = {
    'Godzina': ['08:00', '09:00', '10:00', '11:00', '12:00'],
    'Wilgotność': [44.6, 23.56, 12, 58, 52],
    'Temperatura': [5.7, 13.0, 45.5, 37.8, 23.0]
}
df = pd.DataFrame(data)

col1, col2 = st.columns(2)

with col1:
    st.subheader("WILGOTNOŚĆ[%]")
    fig_humid = go.Figure(data=[
        go.Bar(
            x=df['Godzina'],
            y=df['Wilgotność'],
            marker_color='royalblue',
            text=df['Wilgotność'],
            textposition='auto'
        )
    ])
    fig_humid.update_layout(height=400, margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig_humid, use_container_width=True)

with col2:
    st.subheader("Temperatura [$^\circ C$]")
    fig_temp = go.Figure(data=[
        go.Bar(
            x=df['Godzina'],
            y=df['Temperatura'],
            marker_color='lightsalmon',
            text=df['Temperatura'],
            textposition='auto'
        )
    ])
    fig_temp.update_layout(height=400, margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig_temp, use_container_width=True)

st.divider()
