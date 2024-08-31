import streamlit as st
import google.generativeai as genai
import os
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Configure Gemini API key
os.environ['API_KEY'] = "AIzaSyCpwqVPdsR4QCfp6AvR7dozl0lMpri6hSI"
genai.configure(api_key=os.environ['API_KEY'])

# Define function to interact with Gemini AI
def gemini_ai(query):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(query)
    return response.text

# Function for soil data analysis and crop recommendation
def analyze_soil_data(N, P, K, temp, humidity, ph, rainfall):
    # Set limits for soil parameters
    N_limit = 1000
    P_limit = 1000
    K_limit = 1000
    temp_limit = 100
    humidity_limit = 100
    ph_limit = 14
    rainfall_limit = 1000

    # Display set values and check limits
    st.write("### Set Soil Parameters:")
    st.write(f"- Nitrogen: {N}/{N_limit}")
    st.write(f"- Phosphorus: {P}/{P_limit}")
    st.write(f"- Potassium: {K}/{K_limit}")
    st.write(f"- Temperature: {temp}/{temp_limit}")
    st.write(f"- Humidity: {humidity}/{humidity_limit}")
    st.write(f"- pH: {ph}/{ph_limit}")
    st.write(f"- Rainfall: {rainfall}/{rainfall_limit}")

    # Dummy function for soil analysis, replace with actual logic
    soil_params = {
        "Nitrogen": N,
        "Phosphorus": P,
        "Potassium": K,
        "Temperature": temp,
        "Humidity": humidity,
        "pH": ph,
        "Rainfall": rainfall
    }

    # Bar graph for soil nutrient distribution
    fig, ax = plt.subplots()
    nutrients = ['Nitrogen', 'Phosphorus', 'Potassium']
    values = [N, P, K]
    ax.bar(nutrients, values, color=['blue', 'green', 'orange'])
    ax.set_ylabel('Nutrient Level')
    ax.set_title('Soil Nutrient Distribution')
    st.pyplot(fig)

    # Soil suitability for crop cultivation
    crop_suitability = {
        'Wheat': (N > 100) and (P > 50) and (K > 100),
        'Rice': (N > 200) and (P > 100) and (K > 150),
        'Corn': (N > 150) and (P > 80) and (K > 120)
    }

    suitable_crops = [crop for crop, suitability in crop_suitability.items() if suitability]
    if suitable_crops:
        st.write("Based on the soil analysis, the soil is suitable for cultivating the following crops:")
        for crop in suitable_crops:
            st.write(f"- {crop}")
    else:
        st.write("The soil may not be suitable for any specific crop.")

    return soil_params

def main():
    st.title("🌾 Agriculture Chatbot 🤖")

    # Sidebar section for queries
    st.sidebar.title("Queries")
    query_type = st.sidebar.radio("Select Query Type", ["Chat", "Soil Analysis"])

    if query_type == "Chat":
        queries = st.text_input("Ask your farming question:", key="query")
        chat_button = st.button("Chat", key="chat_button")

        if chat_button and queries.strip():
            response = gemini_ai(queries)
            st.write(f"💬 **Gemini AI**: {response}")

    elif query_type == "Soil Analysis":
        st.markdown("# Soil Analysis 🌱")

        # Soil data input
        N = st.slider("Nitrogen", 0, 1000, 500)
        P = st.slider("Phosphorus", 0, 1000, 500)
        K = st.slider("Potassium", 0, 1000, 500)
        temp = st.slider("Temperature", 0.0, 100.0, 25.0)
        humidity = st.slider("Humidity (%)", 0.0, 100.0, 50.0)
        ph = st.slider("pH", 0.0, 14.0, 7.0)
        rainfall = st.slider("Rainfall (mm)", 0.0, 1000.0, 500.0)

        if st.button("Analyze"):
            result = analyze_soil_data(N, P, K, temp, humidity, ph, rainfall)

if __name__ == "__main__":
    main()
