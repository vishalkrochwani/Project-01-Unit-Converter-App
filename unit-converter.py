import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    /* General app styling */
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        max-width: 700px;
        margin: auto;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        border: none;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stSelectbox, .stNumberInput {
        background-color: white;
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #dcdcdc;
    }
    .stSelectbox label, .stNumberInput label {
        font-weight: bold;
        color: #333;
    }
    .stMarkdown h1 {
        color: #2c3e50;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .stMarkdown h3 {
        color: #34495e;
    }
    .stSuccess {
        background-color: #d4edda;
        color: #155724;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
    }
    .stError {
        background-color: #f8d7da;
        color: #721c24;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
    }
    /* Category-specific icons */
    .category-icon {
        font-size: 1.2em;
        margin-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# App title and description
st.title("🌏 Unit Converter")
st.markdown("### Convert Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result.")

# Add some spacing
st.markdown("<br>", unsafe_allow_html=True)

# Conversion logic
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
    return None

# Main container for content
with st.container():
    # Category selection
    category = st.selectbox("Select a Category", ["Length", "Weight", "Time"], help="Choose a conversion category")

    # Unit selection based on category
    if category == "Length":
        unit = st.selectbox(
            "📏 Select Conversion",
            ["Kilometers to Miles", "Miles to Kilometers"],
            help="Select the unit conversion"
        )
    elif category == "Weight":
        unit = st.selectbox(
            "⚖️ Select Conversion",
            ["Kilograms to Pounds", "Pounds to Kilograms"],
            help="Select the unit conversion"
        )
    elif category == "Time":
        unit = st.selectbox(
            "⏰ Select Conversion",
            ["Seconds to Minutes", "Minutes to Seconds", "Hours to Minutes", 
             "Minutes to Hours", "Hours to Days", "Days to Hours"],
            help="Select the unit conversion"
        )

    # Value input
    value = st.number_input(
        "Enter Value to Convert",
        min_value=0.0,
        step=0.01,
        format="%.2f",
        help="Enter the value you want to convert"
    )

    # Convert button
    if st.button("Convert"):
        if value > 0:
            converted_value = convert_units(category, value, unit)
            if converted_value is not None:
                st.success(f"Converted Value: {converted_value:.2f}")
            else:
                st.error("Conversion error. Please check your inputs.")
        else:
            st.error("Please enter a valid value greater than 0.")