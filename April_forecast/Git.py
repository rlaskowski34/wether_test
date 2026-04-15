import pandas as pd

weather_counts = df["description"].value_counts()
st.pyplot(
    weather_counts.plot.pie(
        autopct="%1.0f%%"
    ).figure
)