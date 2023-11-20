import streamlit as st
import pandas as pd


@st.cache
def load_data():
    data = pd.read_csv('data.csv', sep=';', encoding='latin1')
    return data

data = load_data()


selected_country = st.selectbox("Select a Country", data['Country'])

col1, col2 = st.columns(2)

with col1:
    coal_percent = st.slider("Coal %", 0.0, 100.0, 0.0, key="coal_slider")
    gas_percent = st.slider("Gas %", 0.0, 100.0, 0.0, key="gas_slider")
    oil_percent = st.slider("Oil %", 0.0, 100.0, 0.0, key="oil_slider")
    hydro_percent = st.slider("Hydro %", 0.0, 100.0, 0.0, key="hydro_slider")
    renewable_percent = st.slider("Renewable %", 0.0, 100.0, 0.0, key="renewable_slider")
    nuclear_percent = st.slider("Nuclear %", 0.0, 100.0, 0.0, key="nuclear_slider")

# Manual input boxes for energy sources in the second column
with col2:
    coal_percent_manual = st.number_input("Coal % (Manual Input)", 0.0, 100.0, 0.0, format="%.2f", key="coal_manual")
    gas_percent_manual = st.number_input("Gas % (Manual Input)", 0.0, 100.0, 0.0, format="%.2f", key="gas_manual")
    oil_percent_manual = st.number_input("Oil % (Manual Input)", 0.0, 100.0, 0.0, format="%.2f", key="oil_manual")
    hydro_percent_manual = st.number_input("Hydro % (Manual Input)", 0.0, 100.0, 0.0, format="%.2f", key="hydro_manual")
    renewable_percent_manual = st.number_input("Renewable % (Manual Input)", 0.0, 100.0, 0.0, format="%.2f", key="renewable_manual")
    nuclear_percent_manual = st.number_input("Nuclear % (Manual Input)", 0.0, 100.0, 0.0, format="%.2f", key="nuclear_manual")

# Bidirectional synchronization button
sync_button = st.button("Sync Values")

# Function to synchronize values bidirectionally
def sync_values():
    global coal_percent, gas_percent, oil_percent, hydro_percent, renewable_percent, nuclear_percent
    global coal_percent_manual, gas_percent_manual, oil_percent_manual, hydro_percent_manual, renewable_percent_manual, nuclear_percent_manual
    
    coal_percent = coal_percent_manual
    gas_percent = gas_percent_manual
    oil_percent = oil_percent_manual
    hydro_percent = hydro_percent_manual
    renewable_percent = renewable_percent_manual
    nuclear_percent = nuclear_percent_manual
    
    coal_percent_manual = coal_percent
    gas_percent_manual = gas_percent
    oil_percent_manual = oil_percent
    hydro_percent_manual = hydro_percent
    renewable_percent_manual = renewable_percent
    nuclear_percent_manual = nuclear_percent

if sync_button:
    sync_values()

coal_percent_total = coal_percent + coal_percent_manual
gas_percent_total = gas_percent + gas_percent_manual
oil_percent_total = oil_percent + oil_percent_manual
hydro_percent_total = hydro_percent + hydro_percent_manual
renewable_percent_total = renewable_percent + renewable_percent_manual
nuclear_percent_total = nuclear_percent + nuclear_percent_manual

Overall_Emission = (coal_percent_total + gas_percent_total + oil_percent_total +
                   hydro_percent_total + renewable_percent_total + nuclear_percent_total)

coal_CO2 = data[data['Country'] == selected_country]["Coal"].values[0]
gas_CO2 = data[data['Country'] == selected_country]["Gas"].values[0]
oil_CO2 = data[data['Country'] == selected_country]["Oil"].values[0]
hydro_CO2 = data[data['Country'] == selected_country]["Hydro"].values[0]
renewable_CO2 = data[data['Country'] == selected_country]["Renewable"].values[0]
nuclear_CO2 = data[data['Country'] == selected_country]["Nuclear"].values[0]

kgCO2_result = ((coal_percent_total * coal_CO2 + gas_percent_total * gas_CO2 + oil_percent_total * oil_CO2 +
                 hydro_percent_total * hydro_CO2 + renewable_percent_total * renewable_CO2 +
                 nuclear_percent_total * nuclear_CO2) / 100000)

# Calculate trees required and price required
# trees_required = kgCO2_result / 15.7
# price_required_inr = (trees_required / 10) * 83.32

st.markdown("<div class='result-section'>", unsafe_allow_html=True)
st.write("Overall Emission %:", Overall_Emission)
st.write("CO2 Emissions (tons):", round(kgCO2_result, 2), "tons of CO2")
st.markdown("</div>", unsafe_allow_html=True)
