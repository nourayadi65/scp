
import streamlit as st
import pandas as pd
import plotly.express as px

from modules.simulation import run_scenario


st.set_page_config(
    page_title="Predictive Scenario",
    page_icon="🌊",
    layout="wide"
)

st.title("🌊 Predictive Scenario Engine")

st.write(
    "Explore how different environmental conditions "
    "affect the water balance of Sebkha Sejoumi."
)

st.info(
    "The current model is a conceptual scenario simulator. "
    "Input values are illustrative, not measured environmental data."
)

st.sidebar.header("Scenario Parameters")

initial_water = st.sidebar.slider(
    "Initial Water Volume",
    min_value=0,
    max_value=5000,
    value=1000,
    step=100
)

rainfall = st.sidebar.slider(
    "Rainfall",
    min_value=0,
    max_value=500,
    value=100,
    step=10
)

inflow = st.sidebar.slider(
    "Water Inflow",
    min_value=0,
    max_value=500,
    value=50,
    step=10
)

evaporation = st.sidebar.slider(
    "Evaporation",
    min_value=0,
    max_value=500,
    value=80,
    step=10
)

outflow = st.sidebar.slider(
    "Water Outflow",
    min_value=0,
    max_value=500,
    value=20,
    step=10
)

results = run_scenario(
    initial_water=initial_water,
    rainfall=rainfall,
    inflow=inflow,
    evaporation=evaporation,
    outflow=outflow
)

st.subheader("Simulation Results")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Initial Water",
    f"{results['initial_water']}"
)

col2.metric(
    "Water Change",
    f"{results['water_change']:+}"
)

col3.metric(
    "Final Water",
    f"{results['final_water']}"
)

if results["water_deficit"] > 0:
    st.warning(
        f"Water deficit: {results['water_deficit']}"
    )
else:
    st.success("No water deficit in this scenario.")

st.subheader("Water Balance Breakdown")

chart_data = pd.DataFrame({
    "Component": [
        "Rainfall",
        "Inflow",
        "Evaporation",
        "Outflow"
    ],
    "Volume": [
        rainfall,
        inflow,
        -evaporation,
        -outflow
    ]
})

fig = px.bar(
    chart_data,
    x="Component",
    y="Volume",
    color="Volume",
    title="Contribution of Each Water-Balance Component"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Scenario Interpretation")

if results["water_change"] > 0:
    st.write(
        "Water volume increases under the selected conditions."
    )
elif results["water_change"] < 0:
    st.write(
        "Water volume decreases under the selected conditions."
    )
else:
    st.write(
        "The water balance is stable under the selected conditions."
    )
