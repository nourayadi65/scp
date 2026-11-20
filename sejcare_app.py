import streamlit as st
import folium
from streamlit_folium import st_folium
import plotly.express as px
import pandas as pd
import base64
from pathlib import Path

BASE = Path(__file__).parent
LOGO_PATH = BASE / "SejCare_logo.png"
HERO_PATH = BASE / "sejcare_hero.png"

st.set_page_config(page_title="SejCare DSS | Sebkha Sejoumi", page_icon=":material/water:", layout="wide")

# Hero image is embedded locally so it works without an external image host.
try:
    HERO64 = base64.b64encode(HERO_PATH.read_bytes()).decode("utf-8") if HERO_PATH.exists() else ""
except Exception:
    HERO64 = ""
    HERO64 = ""
HERO_BG = f'url(data:image/png;base64,{HERO64}) center/cover' if HERO64 else 'linear-gradient(120deg,#244d35,#438f54)'

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Manrope:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap');
:root {{ --green:#276943; --deep:#183b2a; --lime:#c4d86b; --ink:#21362b; --muted:#68766d; --cream:#f4f1e8; --paper:#fffdf8; --rust:#c76d4d; }}
html, body, [class*="css"] {{ font-family:'Manrope',sans-serif; }}
.stApp {{ background:var(--cream); color:var(--ink); }}
.block-container {{ padding-top:1rem; padding-bottom:3rem; max-width:1450px; }}
h1,h2,h3 {{ font-family:'DM Serif Display',serif !important; color:var(--deep) !important; letter-spacing:-.3px; }}
h1 {{ font-size:clamp(2.1rem,4vw,3.2rem) !important; }}
[data-testid="stSidebar"] {{ background:#f8f6ef; border-right:1px solid #e4e0d4; }}
[data-testid="stSidebar"] * {{ color:#183b2a !important; }}
.top-strip {{ background:#193c2b; color:#f3f3e7; padding:10px 18px; font-family:'Space Mono',monospace; font-size:11px; letter-spacing:.2px; }}
.hero {{ overflow:hidden; border-radius:2px; min-height:470px; padding:58px 6%; display:flex; align-items:center; background-color:#214d35; background-image:linear-gradient(100deg,rgba(15,48,31,.90) 0%,rgba(20,69,43,.76) 48%,rgba(42,127,67,.40) 100%),{f'url(data:image/png;base64,{HERO64})' if HERO64 else 'linear-gradient(120deg,#244d35,#438f54)'}; background-position:center; background-size:cover; position:relative; }}
.hero:after {{ content:'SEJCARE / 01'; position:absolute; right:5%; top:7%; font-family:'Space Mono',monospace; font-size:11px; letter-spacing:2px; color:rgba(255,255,255,.7); }}
.hero-content {{ max-width:690px; color:white; position:relative; z-index:2; }}
.hero h1 {{ color:white !important; font-family:'DM Serif Display',serif !important; font-size:clamp(2.6rem,5.8vw,5rem) !important; line-height:1.02; font-weight:400; letter-spacing:-1.8px; margin-bottom:20px; }}
.hero p {{ color:#f4f4e8 !important; font-size:1rem; max-width:580px; line-height:1.8; }}
.hero-kicker,.kicker {{ text-transform:uppercase; letter-spacing:2px; font-family:'Space Mono',monospace; font-size:11px; font-weight:700; color:#b45f45; margin-bottom:12px; }}
.hero-kicker {{ color:#dce9ba; }}
.feature-card {{ background:var(--paper); border:1px solid #e5e0d5; padding:23px; min-height:195px; transition:transform .2s,border-color .2s; }}
.feature-card:hover {{ transform:translateY(-4px); border-color:#9ebd91; }}
.feature-number {{ color:#b9ce6a; font-size:36px; font-weight:700; font-family:'Space Mono',monospace; }}
.feature-card h3 {{ margin-top:8px; font-size:1.35rem; }} .feature-card p {{ color:#68766d; line-height:1.7; font-size:.9rem; }}
.story-panel {{ background:#fffdf8; border:1px solid #e5e0d5; padding:28px; margin:14px 0; }}
.story-title {{ font-family:'DM Serif Display',serif; font-size:2rem; color:#183b2a; line-height:1.15; margin:8px 0 14px; }}
.story-copy {{ color:#536258; line-height:1.85; font-size:.96rem; }}
.highlight {{ background:#e9eedb; border-left:4px solid #c4d86b; padding:18px 20px; color:#294a34; line-height:1.7; }}
.insight-card {{ background:var(--paper); border:1px solid #e5e0d5; border-top:3px solid #c4d86b; padding:20px; height:100%; }}
.insight-card h3 {{ font-size:1.3rem; line-height:1.35; margin:13px 0 8px; }} .insight-card p {{ color:#68766d; font-size:.88rem; line-height:1.7; }}
.metric-panel {{ background:var(--paper); border:1px solid #e5e0d5; padding:18px; }}
/* High-contrast metric typography: prevents pale text on cream backgrounds */
[data-testid="stMetricLabel"], [data-testid="stMetricLabel"] p, [data-testid="stMetricLabel"] div,
[data-testid="stMetricValue"], [data-testid="stMetricValue"] div,
[data-testid="stMetricDelta"], [data-testid="stMetricDelta"] div {{ color:#183b2a !important; }}
[data-testid="stMetric"] {{ background:#fffdf8; border:1px solid #e5e0d5; padding:14px 16px; }}
/* Custom SejCare leaf cursor. Keep native text selection and accessibility intact. */
html, body, [data-testid="stAppViewContainer"] {{ cursor:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3E%3Cpath d='M4 27 8 8C17 3 25 5 28 5 27 16 21 25 8 28Z' fill='%23c4d86b' stroke='%23183b2a' stroke-width='1.5'/%3E%3Cpath d='M7 25 22 10' stroke='%23183b2a' stroke-width='1.5' stroke-linecap='round'/%3E%3C/svg%3E") 4 27, auto; }} a, button, [role="button"], input, select, textarea {{ cursor:pointer; }}
.stButton button {{ border-radius:2px !important; font-weight:700 !important; }} footer {{ visibility:hidden; }}
@media(max-width:700px) {{ .hero {{ padding:35px 25px; min-height:390px; }} .hero h1 {{ font-size:2.7rem !important; }} }}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=220)
    else:
        st.markdown("# SejCare DSS")
    st.markdown("### Navigate")
    st.caption("Select a page to explore the project.")
    st.markdown("---")
    st.caption("INTEGRATED URBAN-WETLAND OBSERVATORY")
    st.caption("Sebkha Sejoumi · Tunisia")

st.markdown('<div class="top-strip">SEBKHA SEJOUMI, GREATER TUNIS &nbsp; | &nbsp; Integrated wetland monitoring &nbsp; | &nbsp; Urban resilience</div>', unsafe_allow_html=True)


# Custom vector icons used throughout the interface (no emoji glyphs).
def icon_svg(name, color="#276943"):
    drawings = {
        "map": '<path d="m3 6 6-3 6 3 6-3v15l-6 3-6-3-6 3V6Z"/><path d="M9 3v18M15 6v18"/>',
        "sliders": '<path d="M4 7h7m4 0h5M4 17h3m4 0h9"/><circle cx="13" cy="7" r="2.5"/><circle cx="9" cy="17" r="2.5"/>',
        "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    }
    body = drawings.get(name, drawings["map"])
    return f'<svg viewBox="0 0 24 24" width="38" height="38" fill="none" stroke="{color}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:8px">{body}</svg>'

# ---- Pages ----
def home():
    st.markdown("""<section class="hero"><div class="hero-content"><div class="hero-kicker">Integrated Urban-Wetland Observatory</div>
    <h1>Protecting the<br>wetland. Shaping<br>a resilient future.</h1>
    <p>Explore the environmental changes affecting Sebkha Sejoumi and discover how spatial data, water monitoring and urban planning can support better decisions.</p></div></section>""", unsafe_allow_html=True)
    st.markdown('<div class="kicker">A changing wetland</div><h2>Understanding Sebkha Sejoumi</h2>', unsafe_allow_html=True)
    st.write("SejCare DSS brings together spatial observation, environmental indicators and scenario exploration to help understand the relationship between urban growth and wetland health.")
    cols = st.columns(3)
    for col, (num, title, desc, icon_name) in zip(cols, [("01","Spatial Observatory","Explore land cover, water dynamics and environmental changes across different years.","map"),("02","Scenario Simulator","Adjust urban and wetland parameters to explore possible environmental outcomes.","sliders"),("03","Community & Policy","Understand stakeholder perspectives and planning recommendations.","users")]):
        with col: st.markdown(f'<div class="feature-card">{icon_svg(icon_name)}<div class="feature-number">{num}</div><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="story-panel"><div class="kicker">The project in a nutshell</div><div class="story-title">From observation to understanding</div><div class="story-copy">SejCare DSS is an exploratory platform that connects environmental change, urban pressure and socio-cultural context. Navigate through the pages to learn about the wetland, the challenges it faces, and the tools developed to explore them.</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Explore the website</div><h2>Go deeper into the project</h2>', unsafe_allow_html=True)
    st.markdown("Use the navigation menu on the left to open dedicated pages about the wetland, SejCare, environmental challenges, maps, scenarios and community context.")
    st.markdown('<div class="insight-card"><span class="kicker">FIELD NOTES</span><h3>A wetland within a growing city</h3><p>Sebkha Sejoumi sits at the intersection of ecological value, urban development and environmental risk. Understanding these connections is the starting point of SejCare.</p></div>', unsafe_allow_html=True)

def wetland():
    st.markdown('<div class="kicker">01 / The landscape</div>', unsafe_allow_html=True); st.title("What is Sebkhet Sejoumi?")
    st.markdown('<div class="story-panel"><div class="story-title">A wetland shaped by water, wildlife and the city</div><div class="story-copy">Sebkhet Sejoumi is a wetland located in the Greater Tunis area. It is an important habitat for waterbirds and part of a landscape increasingly influenced by urban growth. Its hydrology and ecological condition are closely connected to runoff, water inputs and land-use changes across its catchment.</div></div>', unsafe_allow_html=True)
    st.subheader("Why the wetland matters")
    a,b,c = st.columns(3)
    a.metric("Ecological role", "Bird habitat", "Wetland biodiversity")
    b.metric("Landscape", "Urban–wetland", "Shared space")
    c.metric("Management", "Catchment-scale", "Connected water system")
    st.markdown('<div class="highlight"><b>Wetlands are not empty land.</b> They provide habitat and contribute to wider environmental functions, while also requiring careful management where urban areas and water systems meet.</div>', unsafe_allow_html=True)
    st.subheader("A place of international ecological importance")
    st.write("The literature review identifies Sebkhet Sejoumi as a Ramsar Wetland of International Importance, an Important Bird Area and a Key Biodiversity Area. It is noted for its role as a wintering site for waterbirds.")
    st.caption("Background: MedWet (2020) and Ayache et al. (2006), as summarized in the project literature review.")

def about():
    st.markdown('<div class="kicker">02 / The project</div>', unsafe_allow_html=True); st.title("What is SejCare DSS?")
    st.markdown('<div class="story-panel"><div class="story-title">An integrated urban-wetland observatory and simulator</div><div class="story-copy">SejCare DSS is a decision-support project concept for Sebkha Sejoumi, Tunisia. It brings geospatial observation, environmental indicators, scenario exploration and socio-cultural context into a single platform, helping users explore the relationship between the wetland and its surrounding urban environment.</div></div>', unsafe_allow_html=True)
    st.subheader("Why does SejCare exist?")
    st.write("Environmental information can be difficult to understand when it is scattered across maps, reports, indicators and planning documents. SejCare aims to bring these perspectives together in an accessible place, supporting awareness, exploration and discussion—not replacing official measurements or professional decisions.")
    st.subheader("Our objectives")
    cols=st.columns(3)
    items=[("Observe","Explore land cover, water-related information and environmental changes."),("Explore","Use simplified scenarios to examine how selected assumptions influence outputs."),("Connect","Consider ecological needs, community concerns and planning choices together.")]
    for col,(title,desc) in zip(cols,items):
        with col: st.markdown(f'<div class="feature-card"><h3>{title}</h3><p>{desc}</p></div>',unsafe_allow_html=True)
    st.subheader("Our approach")
    st.markdown("- **Geospatial analysis:** satellite imagery, land use and land cover, and spatial change.\n- **Environmental indicators:** water-related and thermal indicators where data are available.\n- **Scenario exploration:** an interactive space to test illustrative assumptions.\n- **Socio-cultural context:** community concerns, stakeholder roles and possible planning directions.")
    st.markdown('<div class="highlight">SejCare is an exploratory decision-support concept. The simulator outputs are illustrative and are not calibrated environmental predictions.</div>', unsafe_allow_html=True)

def challenges():
    st.markdown('<div class="kicker">03 / Environmental pressures</div>', unsafe_allow_html=True); st.title("Environmental Challenges")
    st.write("Sebkha Sejoumi faces intertwined pressures related to urban growth, water management, pollution and ecological change.")
    sections=[("Urban expansion","Growth of built-up areas can consume agricultural and wetland land, increase impervious surfaces and reshape the catchment."),("Flooding & hydrology","Runoff, wastewater inputs, pumping and drainage alter the wetland’s water balance. Flood management can affect wetland dynamics too."),("Water quality","Wastewater and pollution threaten ecosystem condition and can complicate management priorities."),("Thermal vulnerability","Urban development and loss of vegetation can intensify heat exposure around the wetland, while water and green areas provide important cooling functions."),("Biodiversity","Changes in water depth, disturbance and habitat conditions affect the wetland’s value for birds and other wildlife.")]
    for i,(title,desc) in enumerate(sections,1):
        st.markdown(f'<div class="story-panel"><div class="kicker">Challenge {i:02d}</div><div class="story-title">{title}</div><div class="story-copy">{desc}</div></div>',unsafe_allow_html=True)
    st.caption("Project background references: Guelmami (2020), MedWet (2020), Ayache et al. (2006), and Ncir et al. (2024), as summarized in the team literature review.")

def observatory():
    st.markdown('<div class="kicker">04 / Geospatial exploration</div>', unsafe_allow_html=True); st.title("Spatial Observatory")
    st.write("Explore the Sebkha Sejoumi area and browse observation periods and thematic layers.")
    year=st.select_slider("Observation period",options=["1990","2005","2018","2024","2030 · Projection"],value="2024")
    layer=st.selectbox("Map theme",["Wetland & water","Land use / land cover","Temperature","Urban pressure"])
    left,right=st.columns([3,1])
    with right:
        st.markdown("### Map key"); st.markdown("<div class='legend-box'><span style='color:#3b9a59'>●</span> Lower pressure<br><span style='color:#d4a72c'>●</span> Transition zone<br><span style='color:#c75d4c'>●</span> Higher pressure</div>", unsafe_allow_html=True); st.caption("Illustrative layer key. Replace the circle overlay with validated project GIS layers when available.")
    with left:
        m=folium.Map(location=[36.8,10.1],zoom_start=12,tiles="CartoDB positron")
        folium.Circle(location=[36.8,10.1],radius=2000,color="#2ba84a",fill=True,fill_color="#2ba84a",fill_opacity=.22,popup=f"Sebkha Sejoumi · {year} · {layer}").add_to(m)
        folium.Marker([36.8,10.1],tooltip="Sebkha Sejoumi",popup="Illustrative project area").add_to(m)
        st_folium(m,width=None,height=530,returned_objects=[])
    st.info("The current map is a visual placeholder. Connect classified rasters, shapefiles or GeoJSON layers to display validated results.")

def simulator():
    st.markdown('<div class="kicker">05 / Explore possible futures</div>', unsafe_allow_html=True); st.title("Scenario Simulator")
    st.write("Change the inputs below to compare simplified urban-growth and wetland-restoration scenarios. These formulas are illustrative—not calibrated environmental predictions.")
    left,right=st.columns(2)
    with left:
        st.subheader("Scenario inputs"); urban=st.slider("Urban catchment (%)",0,100,30); wetland=st.slider("Restored / constructed wetland area (ha)",0,500,100)
    with right:
        st.subheader("Illustrative outputs · 2030"); depth=.5+(urban*.01)-(wetland*.001); salinity=35-(wetland*.05)+(urban*.1)
        st.metric("Projected water depth",f"{depth:.2f} m"); st.metric("Projected salinity",f"{salinity:.1f} PSU")
    df=pd.DataFrame({"Scenario":["Without wetlands","With wetlands"],"Relative index":[100,max(0,100-wetland*.15)]})
    fig=px.bar(df,x="Scenario",y="Relative index",color="Scenario",color_discrete_sequence=["#c76d4d","#35ae57"],title="Illustrative pollution index comparison")
    fig.update_layout(plot_bgcolor="white",paper_bgcolor="white",font_color="#24332d")
    st.plotly_chart(fig,use_container_width=True)

def community():
    st.markdown('<div class="kicker">06 / Beyond the map</div>', unsafe_allow_html=True); st.title("Community & Policy Context")
    st.write("Wetland management involves environmental priorities, community needs, urban development and public decision-making.")
    x,y=st.columns(2)
    with x: st.info("**Community perspective**\n\nFlooding, odors and mosquitoes can make the wetland feel like a daily nuisance to nearby residents.")
    with y: st.success("**Conservation perspective**\n\nThe site supports wetland biodiversity and migratory waterbirds, including flamingos, and has important ecological value.")
    st.markdown("---"); st.subheader("Stakeholder overview")
    stakeholders=pd.DataFrame({"Stakeholder":["Local residents","Municipality","Environmental NGOs","Visitors / birdwatchers"],"Influence":["Medium","High","Medium","Low"],"Interest":["High","High","High","Medium"]})
    st.dataframe(stakeholders,use_container_width=True,hide_index=True)
    st.subheader("Planning directions")
    recs=["Consider the entire catchment area—not only the wetland itself—in planning and management.","Protect wetland banks and limit construction in sensitive zones.","Improve upstream wastewater collection and water quality.","Support ecotourism, birdwatching and public awareness.","Explore nature-based approaches to mosquito management."]
    for rec in recs: st.markdown(f"- {rec}")

# Streamlit multipage navigation: each entry opens a distinct page.
pages = {
    "Discover SejCare": [
        st.Page(home, title="Home", icon=":material/home:", default=True),
        st.Page(wetland, title="The Wetland", icon=":material/water:"),
        st.Page(about, title="About SejCare", icon=":material/eco:"),
        st.Page(challenges, title="Environmental Challenges", icon=":material/warning:"),
    ],
    "Interactive Tools": [
        st.Page(observatory, title="Spatial Observatory", icon=":material/map:"),
        st.Page(simulator, title="Scenario Simulator", icon=":material/tune:"),
        st.Page(community, title="Community & Policy", icon=":material/groups:"),
    ],
}
selected_page = st.navigation(pages)
selected_page.run()
