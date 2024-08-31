import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to fetch government schemes from the URL
def fetch_govt_schemes(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        scheme_table = soup.find('table')  # Assuming the scheme information is in a table
        if scheme_table:
            schemes = []
            rows = scheme_table.find_all('tr')
            for row in rows[1:]:  # Skip the header row
                columns = row.find_all('td')
                scheme_details = [column.get_text(strip=True) for column in columns]
                schemes.append(scheme_details)
            return schemes
    return None

# Main function to run the app
def main():
    st.title("Government Schemes for Agriculture 🌾🏛️")
    st.write("This section provides information about various government schemes available for farmers.")
    
    url = "https://agriwelfare.gov.in/en/Major"  # URL of the government schemes page
    schemes = fetch_govt_schemes(url)
    
    if schemes:
        st.subheader("List of Government Schemes:")
        for scheme in schemes:
            st.write(f"**Scheme Name:** [{scheme[0]}](https://agriwelfare.gov.in/en/Major)")
            st.write(f"**Description:** {scheme[1]}")
            st.write(f"**Eligibility:** {scheme[2]}")
            st.write(f"**Benefits:** [{scheme[3]}](https://agriwelfare.gov.in/en/Major)")
            if len(scheme) > 4:
                st.write(f"**Application Process:** {scheme[4]}")
                apply_button = st.button(f"Apply for {scheme[0]}")
                if apply_button:
                    st.info(f"You clicked on 'Apply for {scheme[0]}'")
                    # Here you can add code to redirect the user to the specific application page
            st.write("---")
            
    else:
        st.error("Failed to fetch government scheme information.")

if __name__ == "__main__":
    main()
