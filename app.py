import streamlit as st

# Custom CSS for Full Background, Buttons & Styling
st.markdown(
    """
<style>
    /* Make the entire app background white */
    .stApp {
        background: white !important;
        color: black !important;
    }


    /* Unit Converter Box */
    .converter-box {
        background: rgba(255, 255, 255, 0.3); /* Light glass effect */
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(20px);
        box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
        width: 60%;
        margin: auto;
    }

    /* Title Styling */
    h1 {
        text-align: center;
        font-size: 2.5em;
        color: white;
        font-weight: bold;
    }

    /* Button Styling */
    .stButton>button {
        background: linear-gradient(135deg, #e52e71, #ff8a00);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px 25px;
        border: none;
        transition: 0.3s;
    }

    /* Button Hover Effect */
    .stButton>button:hover {
        background: linear-gradient(135deg, #ff8a00, #e52e71);
        transform: scale(1.05);
    }

    /* Button Click Effect */
    .stButton>button:active {
        background: #ff4b4b;
        color: black;
    }

    /* Inputs Styling */
    .stSelectbox, .stNumberInput {
        border-radius: 8px;
        padding: 8px;
        background: rgba(255, 255, 255, 0.2);
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<h1 style="margin-bottom: 0;">🧮 Unit Converter</h1>
<h3 style="margin-top: 0;">Effortlessly convert units with accuracy and ease! ⚡</h3>
""", unsafe_allow_html=True)

# Unit Converter Section
st.markdown('<div class="converter-box">', unsafe_allow_html=True)

# Category Selection
category = st.selectbox("Choose a category", [
    "Length", "Weight", "Temperature", "Time", "Speed", "Area", "Volume", "Digital Storage"
])

# Define units
units = {
    "Length": ["Meters", "Kilometers", "Miles", "Yards", "Feet", "Inches"],
    "Weight": ["Grams", "Kilograms", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["Seconds", "Minutes", "Hours", "Days"],
    "Speed": ["Meters per second", "Kilometers per hour", "Miles per hour"],
    "Area": ["Square meters", "Square kilometers", "Hectares", "Acres", "Square miles"],
    "Volume": ["Liters", "Milliliters", "Cubic meters", "Gallons", "Cubic inches"],
    "Digital Storage": ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"]
}

from_unit = st.selectbox("From Unit", units[category])
to_unit = st.selectbox("To Unit", units[category])
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

# Conversion Function
def convert_units(value, from_unit, to_unit, category):
    conversions = {
        "Length": {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701},
        "Weight": {"Grams": 1, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274},
        "Temperature": {"Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15},
        "Time": {"Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400},
        "Speed": {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694},
        "Area": {"Square meters": 1, "Square kilometers": 0.000001, "Hectares": 0.0001, "Acres": 0.000247105, "Square miles": 3.861e-7},
        "Volume": {"Liters": 1, "Milliliters": 1000, "Cubic meters": 0.001, "Gallons": 0.264172, "Cubic inches": 61.0237},
        "Digital Storage": {"Bytes": 1, "Kilobytes": 0.001, "Megabytes": 1e-6, "Gigabytes": 1e-9, "Terabytes": 1e-12}
    }
    
    if category == "Temperature":
        return conversions[category][to_unit](value) if from_unit == "Celsius" else value
    else:
        return value * (conversions[category][to_unit] / conversions[category][from_unit])

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")

st.markdown('</div>', unsafe_allow_html=True)  # Close converter box
