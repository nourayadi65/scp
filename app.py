
import streamlit as st

# ==========================================
# SEJCARE DSS - MAIN APPLICATION
# ==========================================

# 1. PAGE CONFIGURATION

st.set_page_config(
    page_title="SejCare DSS",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)


# 2. CUSTOM CSS

st.markdown("""
<style>

.main {
    background-color: #F7F9F6;
}

h1, h2, h3 {
    color: #174A38;
}

.stMetric {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #E1EAE3;
}

</style>
""", unsafe_allow_html=True)


# 3. SIDEBAR

st.sidebar.title("🌿 SejCare DSS")

st.sidebar.markdown("---")

st.sidebar.markdown(
    "**Integrated Urban-Wetland Observatory & Simulator**"
)

st.sidebar.info(
    "Decision-support platform for "
    "Sebkha Sejoumi, Tunisia."
)


# 4. MAIN HEADER

st.title("🌿 SejCare DSS")

st.subheader(
    "Integrated Urban-Wetland Observatory & Simulator"
)

st.markdown(
    "### Understanding, monitoring and protecting Sebkha Sejoumi"
)

st.write("""
SejCare DSS is an environmental decision-support
platform designed to explore the interactions between
urban development, wetland dynamics and ecological
conservation at Sebkha Sejoumi, Tunisia.
""")


st.divider()


# 5. PROJECT INDICATORS

st.header("Platform Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Study Area",
        value="Sebkha Sejoumi"
    )

with col2:
    st.metric(
        label="Main Objective",
        value="Wetland Monitoring"
    )

with col3:
    st.metric(
        label="Platform",
        value="Decision Support"
    )


st.divider()


# 6. PLATFORM MODULES

st.header("Explore the Platform")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🛰️ Geo-Historical Observatory")

    st.write("""
    Explore historical environmental changes,
    vegetation dynamics, water surfaces and
    urban expansion.
    """)

with col2:
    st.subheader("📊 Predictive Scenario Engine")

    st.write("""
    Simulate hypothetical environmental scenarios
    and investigate how rainfall, evaporation
    and urban development affect water balance.
    """)

with col3:
    st.subheader("🌱 Socio-Ecological NBS Planner")

    st.write("""
    Explore nature-based solutions and their
    potential benefits for wetland conservation
    and surrounding communities.
    """)


st.divider()


# 7. PROJECT INFORMATION

st.header("About Sebkha Sejoumi")

st.write("""
Sebkha Sejoumi is an important wetland ecosystem
located in the Greater Tunis region.

Understanding its environmental dynamics is essential
for exploring sustainable management strategies,
urban-wetland interactions and ecological protection.
""")


# 8. FOOTER
st.divider()

st.caption(
    "SejCare DSS | Academic Project | Tunisia | 2026"
)
