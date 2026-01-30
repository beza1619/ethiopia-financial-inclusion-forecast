import streamlit as st

st.set_page_config(
    page_title="Ethiopia FI Dashboard",
    layout="wide"
)

st.title("Ethiopia Financial Inclusion Forecasting System")
st.write("Developed by Selam Analytics")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Page",
    ["Overview", "Forecasts", "About"]
)

if page == "Overview":
    st.header("Dashboard Overview")
    st.write("Current Status (2024):")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Account Ownership", "49.0%")
    with col2:
        st.metric("Digital Payments", "35.0%")
    with col3:
        st.metric("Mobile Money", "9.45%")
    st.write("Key Insights:")
    st.write("- P2P transfers surpassed ATM withdrawals (2023)")
    st.write("- Digital payments growing faster than account ownership")
    st.write("- Gender gap: 15 pp (54% male vs 39% female in 2021)")

elif page == "Forecasts":
    st.header("2025-2027 Forecasts")
    st.write("Base Scenario Forecasts:")
    st.write("| Year | Account Ownership | Digital Payments | Mobile Money |")
    st.write("|------|-------------------|------------------|--------------|")
    st.write("| 2024 | 49.0% | 35.0% | 9.45% |")
    st.write("| 2025 | 55.1% | 44.7% | 13.7% |")
    st.write("| 2026 | 58.6% | 54.2% | 16.5% |")
    st.write("| 2027 | 62.1% | 63.7% | 19.4% |")
    st.write("")
    st.write("Key Insights:")
    st.write("- Digital payments will surpass account ownership by 2026")
    st.write("- On track for NFIS II target (60% by 2030)")
    st.write("- Mobile money will nearly double by 2027")

else:
    st.header("About This Dashboard")
    st.write("Purpose: Forecast Ethiopia's financial inclusion")
    st.write("Methodology: Trend analysis + event impacts")
    st.write("Data Sources: Global Findex, World Bank, GSMA")
    st.write("Developed for: National Bank of Ethiopia consortium")