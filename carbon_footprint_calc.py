import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of the app
st.title('Carbon Footprint Calculator')

# Sidebar for inputs
st.sidebar.header('Enter Your Usage Details')

# Defining categories of appliances and vehicles with typical emission factors (kg CO2 per unit)
# These are simplified example values and may need adjustment for accuracy
appliances = {
    'Refrigerator': 0.2,  # kg CO2 per hour of use
    'Washing Machine': 0.3,
    'Air Conditioner': 0.5,
    'Heater': 0.4
}

vehicles = {
    'Car': 0.2,  # kg CO2 per km
    'Motorbike': 0.1,
    'Bicycle': 0,  # Zero emissions for non-electric bicycle
    'Bus': 0.05  # per km as a passenger
}

# Input fields for appliance usage
appliance_usage = {}
for appliance, emission_factor in appliances.items():
    usage = st.sidebar.number_input(f'Hours/day used for {appliance}', min_value=0.0, value=0.0, step=0.1)
    appliance_usage[appliance] = usage

# Input fields for vehicle usage
vehicle_usage = {}
for vehicle, emission_factor in vehicles.items():
    usage = st.sidebar.number_input(f'Kilometers/day traveled by {vehicle}', min_value=0.0, value=0.0, step=0.1)
    vehicle_usage[vehicle] = usage

# Calculate the total carbon footprint
def calculate_footprint(appliance_usage, vehicle_usage):
    appliance_emissions = sum(hours * appliances[appliance] for appliance, hours in appliance_usage.items())
    vehicle_emissions = sum(kms * vehicles[vehicle] for vehicle, kms in vehicle_usage.items())
    total_daily_emissions = appliance_emissions + vehicle_emissions
    return total_daily_emissions * 365  # Annual emissions

# Display the results
if st.sidebar.button('Calculate Carbon Footprint'):
    total_annual_emissions = calculate_footprint(appliance_usage, vehicle_usage)
    st.write(f"Your total annual carbon footprint is approximately {total_annual_emissions:.2f} kg of CO2.")

    # Data for plotting
    data = {
        'Appliances': sum(appliance_usage[appliance] * appliances[appliance] for appliance in appliances) * 365,
        'Vehicles': sum(vehicle_usage[vehicle] * vehicles[vehicle] for vehicle in vehicles) * 365
    }
    fig, ax = plt.subplots()
    ax.bar(data.keys(), data.values(), color=['blue', 'green'])
    ax.set_ylabel('Annual CO2 Emissions (kg)')
    ax.set_title('Breakdown of CO2 Emissions')
    st.pyplot(fig)
else:
    st.write("Enter your usage details in the sidebar and press 'Calculate Carbon Footprint' to see the results.")
