import streamlit as st
import pandas as pd

# Add custom CSS to style the app

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Carbon Footprint Calculator")
# image = st.image("assests/bg2.png", caption="Your Image Caption", use_column_width=True)
image = st.image("assests/bg2.png", caption="Your Image Caption", use_column_width=True, output_format="auto")

# Load data from CSV file
@st.cache
def load_data():
    data = pd.read_csv('data.csv', sep=';', encoding='latin1')
    return data

data = load_data()

# User input - Select country from dropdown
selected_country = st.selectbox("Select a Country", data['Country'])

# Sliders for energy sources
coal_percent = st.slider("Coal %", 0, 100, 0)
gas_percent = st.slider("Gas %", 0, 100, 0)
oil_percent = st.slider("Oil %", 0, 100, 0)
hydro_percent = st.slider("Hydro %", 0, 100, 0)
renewable_percent = st.slider("Renewable %", 0, 100, 0)
nuclear_percent = st.slider("Nuclear %", 0, 100, 0)
custom_percent = st.slider("Custom %", 0, 100, 0)

# Calculate CO2 emissions
coal_CO2 = data[data['Country'] == selected_country]["Coal"].values[0]
gas_CO2 = data[data['Country'] == selected_country]["Gas"].values[0]
oil_CO2 = data[data['Country'] == selected_country]["Oil"].values[0]
hydro_CO2 = data[data['Country'] == selected_country]["Hydro"].values[0]
renewable_CO2 = data[data['Country'] == selected_country]["Renewable"].values[0]
nuclear_CO2 = data[data['Country'] == selected_country]["Nuclear"].values[0]
custom_CO2 = 0  # You can set the custom value

Overall_Emission = coal_percent + gas_percent + oil_percent + hydro_percent + renewable_percent + nuclear_percent + custom_percent

# Calculate CO2 emissions in tons
kgCO2_result = ((coal_percent * coal_CO2 + gas_percent * gas_CO2 + oil_percent * oil_CO2 +
                 hydro_percent * hydro_CO2 + renewable_percent * renewable_CO2 +
                 nuclear_percent * nuclear_CO2 + custom_percent * custom_CO2) / 100000)

# Calculate trees required and price required
# trees_required = kgCO2_result / 15.7
# price_required_inr = (trees_required / 10) * 83.32

st.markdown("<div class='result-section'>", unsafe_allow_html=True)
st.write("Overall Emission %:", Overall_Emission)
st.write("CO2 Emissions (tons):", round(kgCO2_result, 2), "tons of CO2")
st.markdown("</div>", unsafe_allow_html=True)
