import streamlit as st
import plotly.express as px
from backend import get_data

## Add the title and text input here...
st.title("Weather Forcast for Days Ahead....")
place = st.text_input("Region")
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of forcasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    ## get temperature data...
    filtered_data = get_data(place, days)


    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates  = [dict["dt_txt"] for dict in filtered_data]
        ## create a temperature plot
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/clouds.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        print(sky_conditions)

        st.image(image_paths, width=115)



figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)


