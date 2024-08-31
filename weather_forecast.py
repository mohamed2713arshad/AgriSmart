import streamlit as st
import requests
import matplotlib.pyplot as plt

# Function to fetch weather information
def fetch_weather(city):
    # Replace the API key and base URL with your weatherapi.com API credentials
    api_key = "6e865750f0934069aa674739240104"  # Replace with your actual API key
    base_url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1&aqi=yes&alerts=no"

    response = requests.get(base_url)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

# Function to create hourly temperature distribution bar chart
def create_temperature_bar_chart(weather_data):
    if weather_data:
        hourly_data = weather_data['forecast']['forecastday'][0]['hour']
        temperatures = [data['temp_c'] for data in hourly_data]

        hours = range(24)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(hours, temperatures, color='skyblue')
        ax.set_xlabel('Hour')
        ax.set_ylabel('Temperature (°C)')
        ax.set_title('Hourly Temperature Distribution Throughout the Day')
        ax.set_xticks(hours)
        ax.grid(True)
        st.pyplot(fig)

# Function to create humidity line chart
def create_humidity_line_chart(weather_data):
    if weather_data:
        hourly_data = weather_data['forecast']['forecastday'][0]['hour']
        humidity = [data['humidity'] for data in hourly_data]

        hours = range(24)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(hours, humidity, marker='o', color='green', linestyle='-')
        ax.set_xlabel('Hour')
        ax.set_ylabel('Humidity (%)')
        ax.set_title('Hourly Humidity Variation Throughout the Day')
        ax.set_xticks(hours)
        ax.grid(True)
        st.pyplot(fig)

# Function to create wind speed line chart
def create_wind_speed_line_chart(weather_data):
    if weather_data:
        hourly_data = weather_data['forecast']['forecastday'][0]['hour']
        wind_speed = [data['wind_kph'] for data in hourly_data]

        hours = range(24)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(hours, wind_speed, marker='o', color='blue', linestyle='-')
        ax.set_xlabel('Hour')
        ax.set_ylabel('Wind Speed (km/h)')
        ax.set_title('Hourly Wind Speed Variation Throughout the Day')
        ax.set_xticks(hours)
        ax.grid(True)
        st.pyplot(fig)

# Streamlit UI code
def main():
    st.title("🌾 Agriculture Weather App 🌦️")

    city = st.text_input("Enter city name:", "New York")

    if st.button("Get Weather Details", key="weather_button"):
        weather_data = fetch_weather(city)
        if weather_data:
            st.subheader("Weather Details")
            st.write(f"🌤️ Current Weather: {weather_data['current']['condition']['text']}")
            st.write(f"🌡️ Temperature: {weather_data['current']['temp_c']}°C")
            st.write(f"💧 Humidity: {weather_data['current']['humidity']}%")
            st.write(f"💨 Wind Speed: {weather_data['current']['wind_kph']} km/h")

            st.subheader("Hourly Temperature Distribution Throughout the Day")
            create_temperature_bar_chart(weather_data)

            st.subheader("Hourly Humidity Variation Throughout the Day")
            create_humidity_line_chart(weather_data)

            st.subheader("Hourly Wind Speed Variation Throughout the Day")
            create_wind_speed_line_chart(weather_data)
        else:
            st.error("Failed to fetch weather information")

if __name__ == "__main__":
    main()
