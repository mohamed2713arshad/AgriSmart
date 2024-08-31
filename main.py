import streamlit as st
from streamlit_option_menu import option_menu
import chatbot
import weather_forecast
import plant_diseasepredict
import govtscheme
import agri_analysis

def main():
    st.set_page_config(page_title="🌾 AgriSmartHub 🛠️", layout="wide", initial_sidebar_state="expanded")

    # Custom CSS for glassmorphism effect, font sizes, and centering content
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f0f0; /* Light background color */
            color: #000000; /* Text color */
            font-size: 18px; /* Increased font size */
        }
        .stApp {
            background: rgba(255, 255, 255, 0.95); /* Glassmorphism effect */
            border-radius: 20px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37); /* Glassmorphism shadow */
            backdrop-filter: blur(14px); /* Glassmorphism blur effect */
            border: 1px solid rgba(255, 255, 255, 0.18); /* Glassmorphism border */
            padding: 20px;
        }
        .navbar {
            display: flex;
            justify-content: center;
            background-color: #009688; /* Navbar background color */
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 10px;
            margin-bottom: 20px;
        }
        .nav-link {
            font-size: 16px; /* Reduced font size for navbar */
            text-align: center;
            margin: 0px 10px;
            padding: 10px;
            cursor: pointer;
            color: #ffffff; /* White text color */
        }
        .nav-link:hover {
            background-color: #00796b; /* Hover background color */
            border-radius: 10px;
        }
        .feature-description {
            text-align: left; /* Align feature descriptions to the left */
            margin-left: 20px; /* Add margin for better readability */
            font-size: 20px; /* Increase font size for feature descriptions */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Navbar with icons
    selected = option_menu(
        menu_title=None,  # No menu title for navbar
        options=["Home", "Chatbot", "Weather Forecast", "Plant Disease Prediction", "Government Schemes", "Agriculture Analysis"],
        icons=["house", "chat-right-text", "cloud-sun", "bug", "bank", "graph-up"],  # Bootstrap icons
        default_index=0,  # Default to the first option (Home)
        orientation="horizontal",
        styles={
            "container": {"padding": "10px", "display": "flex", "justify-content": "center"},
            "icon": {"font-size": "20px", "margin-right": "5px"},  # Reduced size for icons
            "nav-link": {"text-align": "center", "font-size": "16px"},  # Reduced font size for navbar links
            "nav-link-selected": {"background-color": "#00796b", "border-radius": "10px", "color": "#ffffff"},  # Styling for selected link
        },
    )

    if selected == "Home":
        st.markdown("""
        # Welcome to the AgriSmartHub! 🌾

        **Explore various features to help you with agricultural tasks and information.**
        """, unsafe_allow_html=True)

        # Display detailed descriptions for each feature using cards
        st.subheader("Features:")
        st.markdown("""
        - **Chatbot:** Interact with our AI-powered chatbot to get answers to your queries.
        - **Weather Forecast:** Get the latest weather forecast for your area.
        - **Plant Disease Prediction:** Identify plant diseases using machine learning.
        - **Government Schemes:** Learn about government schemes related to agriculture.
        - **Agriculture Analysis:** Analyze agricultural data for better insights.
        """, unsafe_allow_html=True)

    elif selected == "Chatbot":
        chatbot.main()

    elif selected == "Weather Forecast":
        weather_forecast.main()

    elif selected == "Plant Disease Prediction":
        plant_diseasepredict.main()

    elif selected == "Government Schemes":
        govtscheme.main()

    elif selected == "Agriculture Analysis":
        agri_analysis.main()

if __name__ == "__main__":
    main()
