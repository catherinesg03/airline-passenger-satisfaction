import streamlit as st
import pandas as pd
import joblib
import base64
from pathlib import Path

st.set_page_config(
    page_title="Airline Passenger Satisfaction",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- THEME / STYLING ----------
# Keep airport_background.png in the same folder as this app.py.
_bg_path = Path(__file__).with_name("airport_background.png")
_bg_data = base64.b64encode(_bg_path.read_bytes()).decode("utf-8") if _bg_path.exists() else ""
_bg_css = f'url("data:image/png;base64,{_bg_data}")' if _bg_data else "none"
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

:root {
    --navy: #10243a;
    --navy-2: #183b59;
    --blue: #268bd2;
    --sky: #dff2ff;
    --ink: #142b40;
    --muted: #64788b;
    --line: #dce7ef;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
.stApp {
    background-image:
        linear-gradient(rgba(239, 247, 253, .82), rgba(239, 247, 253, .88)),
        __BG_CSS__;
    background-size: cover;
    background-position: center center;
    background-attachment: fixed;
    background-repeat: no-repeat;
    background-color: #edf4f9;
    color: var(--ink);
}
.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer {visibility: hidden;}

.hero {
    background: linear-gradient(115deg, #10243a 0%, #183b59 58%, #247eae 100%);
    padding: 2.2rem 2.4rem;
    border-radius: 24px;
    color: white;
    margin-bottom: 1.5rem;
    box-shadow: 0 18px 45px rgba(16, 36, 58, .18);
    position: relative;
    overflow: hidden;
}
.hero:after {
    content: "✈";
    position: absolute;
    right: 5%;
    top: 2%;
    font-size: 8rem;
    opacity: .10;
    transform: rotate(-12deg);
}
.eyebrow {
    color: #a9ddff;
    font-size: .78rem;
    font-weight: 700;
    letter-spacing: .16em;
    text-transform: uppercase;
    margin-bottom: .55rem;
}
.hero h1 {
    color: white !important;
    font-family: 'Manrope', sans-serif !important;
    font-size: clamp(2rem, 4vw, 3rem) !important;
    line-height: 1.12 !important;
    margin: 0 0 .6rem 0 !important;
    font-weight: 800 !important;
}
.hero p {
    color: #d8e9f5 !important;
    font-size: 1.02rem;
    max-width: 720px;
    margin: 0;
}
.hero-foot {
    margin-top: 1.15rem;
    color: #c2e6fb;
    font-size: .82rem;
    font-weight: 600;
}
.section-card {
    background: rgba(255,255,255,.94);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 1.25rem 1.35rem .7rem 1.35rem;
    margin: 1rem 0 1.1rem 0;
    box-shadow: 0 8px 24px rgba(24, 59, 89, .055);
}
.section-heading {
    display: flex;
    align-items: center;
    gap: .7rem;
    color: var(--navy);
    font-family: 'Manrope', sans-serif;
    font-weight: 800;
    font-size: 1.18rem;
    margin-bottom: .25rem;
}
.section-sub {
    color: var(--muted);
    font-size: .88rem;
    margin: 0 0 .8rem 2.45rem;
}
.section-icon {
    display: inline-flex;
    width: 34px;
    height: 34px;
    align-items: center;
    justify-content: center;
    background: #e4f4ff;
    border-radius: 11px;
    font-size: 1.05rem;
}
div[data-testid="stForm"] {
    background: transparent;
    border: 0;
    padding: 0;
}
div[data-testid="stSelectbox"] label,
div[data-testid="stNumberInput"] label,
div[data-testid="stSlider"] label {
    color: #29445b !important;
    font-weight: 600 !important;
    font-size: .9rem !important;
}
div[data-baseweb="select"] > div,
div[data-testid="stNumberInput"] input {
    border-radius: 10px !important;
    border: 1px solid #c7d9e8 !important;
    background: #ffffff !important;
    color: #142b40 !important;
}
div[data-testid="stNumberInput"] input {
    color: #142b40 !important;
    -webkit-text-fill-color: #142b40 !important;
    font-weight: 700 !important;
}
div[data-testid="stNumberInput"] button {
    background: #e5f3fc !important;
    color: #176da8 !important;
    border: 1px solid #c7d9e8 !important;
}
div[data-testid="stNumberInput"] button:hover {
    background: #cfeaff !important;
    color: #104f7c !important;
}
div[data-baseweb="select"] * { color: #142b40 !important; }
div[data-baseweb="select"] svg { fill: #176da8 !important; }
input, textarea { color: #142b40 !important; }

div[data-testid="stSlider"] [data-baseweb="slider"] {
    padding-top: .2rem;
}
div[data-testid="stSlider"] [role="slider"] {
    background-color: #268bd2 !important;
    border-color: #268bd2 !important;
}
div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(100deg, #176da8, #268bd2) !important;
    color: white !important;
    border: 0 !important;
    border-radius: 12px !important;
    padding: .85rem 1.2rem !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    box-shadow: 0 9px 20px rgba(38,139,210,.22);
    transition: all .2s ease;
}
div[data-testid="stFormSubmitButton"] button:hover {
    transform: translateY(-1px);
    box-shadow: 0 12px 24px rgba(38,139,210,.3);
}
div[data-testid="stFormSubmitButton"] button p { color: white !important; }
div[data-testid="stAlert"] { border-radius: 14px; }
.result-card {
    background: white;
    border: 1px solid var(--line);
    border-radius: 20px;
    padding: 1.4rem 1.5rem;
    box-shadow: 0 12px 30px rgba(24, 59, 89, .08);
    margin-top: 1rem;
}
.result-label {
    color: #648096;
    text-transform: uppercase;
    letter-spacing: .12em;
    font-size: .76rem;
    font-weight: 800;
}
.result-value {
    color: var(--navy);
    font-family: 'Manrope', sans-serif;
    font-size: clamp(1.45rem, 3vw, 2rem);
    font-weight: 800;
    margin: .45rem 0 .3rem 0;
}
.result-note { color: var(--muted); font-size: .9rem; }
div[data-testid="stMetric"] {
    background: #f1f8fd;
    border: 1px solid #dcecf7;
    padding: 1rem;
    border-radius: 14px;
}
div[data-testid="stMetricLabel"] { color: #567187 !important; }
div[data-testid="stMetricValue"] { color: #145783 !important; }
.footer-note {
    text-align: center;
    color: #71879a;
    font-size: .8rem;
    margin-top: 2.2rem;
    padding-top: 1rem;
    border-top: 1px solid #dce7ef;
}
@media (max-width: 700px) {
    .block-container { padding-left: 1rem; padding-right: 1rem; }
    .hero { padding: 1.5rem; }
    .hero:after { font-size: 5rem; right: 2%; }
    .section-card { padding: 1rem .9rem .5rem .9rem; }
}


/* ---------- DROPDOWN VISIBILITY FIX ---------- */

/* Dropdown background */
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    border: 1px solid #c7d9e8 !important;
    border-radius: 10px !important;
}

/* Selected dropdown text */
div[data-testid="stSelectbox"] [role="combobox"] {
    background-color: #ffffff !important;
    color: #142b40 !important;
}

/* All text inside dropdown */
div[data-testid="stSelectbox"] [role="combobox"] * {
    color: #142b40 !important;
    -webkit-text-fill-color: #142b40 !important;
}

/* Dropdown arrow */
div[data-baseweb="select"] svg {
    fill: #176da8 !important;
    color: #176da8 !important;
}

/* Open dropdown menu */
div[data-baseweb="popover"] {
    background-color: #ffffff !important;
}

div[data-baseweb="popover"] ul {
    background-color: #ffffff !important;
}

/* Dropdown options */
div[data-baseweb="popover"] li {
    background-color: #ffffff !important;
    color: #142b40 !important;
}

/* Hover effect */
div[data-baseweb="popover"] li:hover {
    background-color: #e6f3ff !important;
    color: #142b40 !important;
}

</style>
""".replace("__BG_CSS__", _bg_css), unsafe_allow_html=True)

# ---------- LOAD TRAINED ARTIFACTS ----------
@st.cache_resource
def load_artifacts():
    return joblib.load("airline_satisfaction_model.pkl")

try:
    artifacts = load_artifacts()
    model = artifacts["model"]
    scaler = artifacts["scaler"]
    feature_columns = artifacts["feature_columns"]
    arrival_delay_median = artifacts["arrival_delay_median"]
except Exception as exc:
    st.error("The trained model files could not be loaded. Make sure airline_satisfaction_model.pkl is in the same folder as app.py.")
    st.exception(exc)
    st.stop()

# ---------- HEADER ----------
st.markdown("""
<div class="hero">
    <div class="eyebrow">Passenger experience analytics</div>
    <h1>Airline Passenger<br> Satisfaction Predictor</h1>
    <p>Explore how passenger and flight experiences influence overall satisfaction with a machine learning prediction.</p>
    <div class="hero-foot">✦ Powered by XGBoost &nbsp; • &nbsp; Test accuracy in notebook: approximately 96.31%</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="display:flex;gap:10px;flex-wrap:wrap;margin:.2rem 0 1.1rem 0;">
  <span style="background:#e3f3ff;color:#176da8;padding:7px 12px;border-radius:30px;font-size:.8rem;font-weight:700;">✈ Passenger details</span>
  <span style="background:#e3f3ff;color:#176da8;padding:7px 12px;border-radius:30px;font-size:.8rem;font-weight:700;">◷ Flight information</span>
  <span style="background:#e3f3ff;color:#176da8;padding:7px 12px;border-radius:30px;font-size:.8rem;font-weight:700;">☆ Service ratings</span>
</div>
""", unsafe_allow_html=True)

# ---------- INPUT FORM ----------
with st.form("passenger_form"):
    st.markdown("""
    <div class="section-card">
      <div class="section-heading"><span class="section-icon">👤</span> 01 &nbsp; Passenger information</div>
      <div class="section-sub">Tell us a little about the passenger and their journey.</div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        age = st.number_input("Age", min_value=7, max_value=100, value=35)
    with c2:
        customer_type = st.selectbox("Customer Type", ["First-time", "Returning"])
        travel_type = st.selectbox("Type of Travel", ["Business", "Personal"])
    with c3:
        travel_class = st.selectbox("Class", ["Business", "Economy", "Economy Plus"])
        flight_distance = st.number_input("Flight Distance (miles)", min_value=1, max_value=10000, value=850)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
      <div class="section-heading"><span class="section-icon">🛫</span> 02 &nbsp; Flight information</div>
      <div class="section-sub">Enter the departure and arrival delays in minutes.</div>
    """, unsafe_allow_html=True)

    d1, d2 = st.columns(2)
    with d1:
        departure_delay = st.number_input("Departure Delay (minutes)", min_value=0, max_value=3000, value=0)
    with d2:
        arrival_delay = st.number_input("Arrival Delay (minutes)", min_value=0, max_value=3000, value=0)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
      <div class="section-heading"><span class="section-icon">☆</span> 03 &nbsp; Passenger service ratings</div>
      <div class="section-sub">Rate each service from 0 (not applicable) to 5 (highest satisfaction).</div>
    """, unsafe_allow_html=True)

    rating_fields = [
        "Departure and Arrival Time Convenience",
        "Ease of Online Booking",
        "Check-in Service",
        "Online Boarding",
        "Gate Location",
        "On-board Service",
        "Seat Comfort",
        "Leg Room Service",
        "Cleanliness",
        "Food and Drink",
        "In-flight Service",
        "In-flight Wifi Service",
        "In-flight Entertainment",
        "Baggage Handling",
    ]
    defaults = {
        "Departure and Arrival Time Convenience": 3,
        "Ease of Online Booking": 3,
        "Check-in Service": 3,
        "Online Boarding": 3,
        "Gate Location": 3,
        "On-board Service": 4,
        "Seat Comfort": 4,
        "Leg Room Service": 4,
        "Cleanliness": 3,
        "Food and Drink": 3,
        "In-flight Service": 4,
        "In-flight Wifi Service": 3,
        "In-flight Entertainment": 4,
        "Baggage Handling": 4,
    }

    ratings = {}
    rating_cols = st.columns(2)
    for i, field in enumerate(rating_fields):
        with rating_cols[i % 2]:
            ratings[field] = st.slider(field, min_value=0, max_value=5, value=defaults[field])

    st.markdown("</div>", unsafe_allow_html=True)
    submitted = st.form_submit_button("✈  Predict Passenger Satisfaction", type="primary", use_container_width=True)

# ---------- PREDICTION ----------
if submitted:
    passenger = {
        "Gender": gender,
        "Age": age,
        "Customer Type": customer_type,
        "Type of Travel": travel_type,
        "Class": travel_class,
        "Flight Distance": flight_distance,
        "Departure Delay": departure_delay,
        "Arrival Delay": arrival_delay,
        **ratings,
    }

    input_df = pd.DataFrame([passenger])
    input_encoded = pd.get_dummies(input_df, drop_first=True)
    input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)
    input_scaled = scaler.transform(input_encoded)

    prediction = int(model.predict(input_scaled)[0])
    probabilities = model.predict_proba(input_scaled)[0]
    confidence = float(probabilities[prediction]) * 100

    st.markdown("---")
    st.markdown('<div class="section-heading"><span class="section-icon">📊</span> Your prediction</div>', unsafe_allow_html=True)

    if prediction == 1:
        result_title = "Passenger is predicted to be SATISFIED"
        result_emoji = "😊"
        result_color = "#e7f7ef"
        result_border = "#b8e5ca"
        result_text = "#176b3b"
    else:
        result_title = "Passenger is predicted to be NEUTRAL OR DISSATISFIED"
        result_emoji = "😐"
        result_color = "#fff6e5"
        result_border = "#f2d79c"
        result_text = "#80520b"

    st.markdown(f"""
    <div class="result-card" style="background:{result_color};border-color:{result_border};">
      <div class="result-label">Model outcome</div>
      <div class="result-value" style="color:{result_text};">{result_emoji} {result_title}</div>
      <div class="result-note" style="color:{result_text};">This result is generated from the passenger and flight details entered above.</div>
    </div>
    """, unsafe_allow_html=True)

    m1, m2 = st.columns([1, 2])
    with m1:
        st.metric("Prediction confidence", f"{confidence:.2f}%")
    with m2:
        st.markdown(
            f"<div style='padding:1rem 0 .3rem 0;color:#567187;font-weight:600;'>Confidence indicator</div>"
            f"<div style='height:12px;background:#dce8f0;border-radius:20px;overflow:hidden;'>"
            f"<div style='height:12px;width:{confidence:.2f}%;background:linear-gradient(90deg,#268bd2,#36b58a);border-radius:20px;'></div></div>"
            f"<div style='font-size:.8rem;color:#71879a;margin-top:8px;'>Estimated probability for the predicted class</div>",
            unsafe_allow_html=True
        )

    st.caption("Confidence is the model's predicted class probability, not a guarantee of the outcome.")

st.markdown("""
<div class="footer-note">
    Airline Passenger Satisfaction Predictor &nbsp; • &nbsp; Machine Learning Project<br>
    Predictions are estimates produced by the trained model.
</div>
""", unsafe_allow_html=True)