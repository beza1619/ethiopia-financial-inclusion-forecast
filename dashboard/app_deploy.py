import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Ethiopia FI Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title
st.title("📈 Ethiopia Financial Inclusion Forecasting System")
st.markdown("**Developed by Selam Analytics**")
st.markdown("*For: National Bank of Ethiopia, Development Finance Institutions, Mobile Money Operators*")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["📊 Overview", "📈 Forecasts", "📋 About"]
)

if page == "📊 Overview":
    st.header("📊 Dashboard Overview")
    
    # Key metrics
    st.subheader("Current Status (2024)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Account Ownership", "49.0%", "+3 pp since 2021")
    with col2:
        st.metric("Digital Payments", "35.0%", "New in 2024 survey")
    with col3:
        st.metric("Mobile Money", "9.45%", "+4.75 pp since 2021")
    
    # Key insights
    st.subheader("Key Insights")
    st.info("""
    • **P2P digital transfers have surpassed ATM cash withdrawals** (2023)
    • **Digital payments growing faster** than account ownership
    • **Gender gap**: 15 percentage points (54% male vs 39% female in 2021)
    • **Mobile money growing rapidly** (33.7% annually)
    """)

elif page == "📈 Forecasts":
    st.header("📈 2025-2027 Forecasts")
    
    # Forecast data
    forecast_data = pd.DataFrame({
        'Year': [2024, 2025, 2026, 2027],
        'Account Ownership': [49.0, 55.1, 58.6, 62.1],
        'Digital Payments': [35.0, 44.7, 54.2, 63.7],
        'Mobile Money': [9.45, 13.7, 16.5, 19.4]
    })
    
    st.subheader("Base Scenario Forecasts")
       # Forecast table using markdown (no pyarrow needed)
    st.subheader("Base Scenario Forecasts")
    st.markdown("""
    | Year | Account Ownership | Digital Payments | Mobile Money |
    |------|-------------------|------------------|--------------|
    | 2024 | 49.0% | 35.0% | 9.45% |
    | 2025 | 55.1% | 44.7% | 13.7% |
    | 2026 | 58.6% | 54.2% | 16.5% |
    | 2027 | 62.1% | 63.7% | 19.4% |
    """)
    
    # Key forecast insights
    st.subheader("Forecast Insights")
    st.success("""
    ✅ **Digital payments will surpass account ownership by 2026**
    ✅ **On track for NFIS II target** (60% by 2030)
    ✅ **Mobile money will nearly double** by 2027
    """)
    
    # Uncertainty
    st.subheader("Uncertainty Ranges (2027)")
    st.warning("""
    • Account ownership: 62.1% (±5.0 percentage points)
    • Digital payments: 63.7% (±8.7 percentage points)
    • Mobile money: 19.4% (±4.0 percentage points)
    """)

else:  # About page
    st.header("📋 About This Dashboard")
    
    st.subheader("Purpose")
    st.write("""
    This forecasting system tracks Ethiopia's digital financial transformation
    using time series methods and event impact modeling.
    """)
    
    st.subheader("Methodology")
    st.write("""
    1. **Data Collection**: Global Findex, World Bank, GSMA, operator reports
    2. **Event Modeling**: Impact estimation using historical data
    3. **Forecasting**: Trend analysis + event impacts + scenario modeling
    4. **Uncertainty Quantification**: Confidence intervals based on data quality
    """)
    
    st.subheader("Key Questions Answered")
    st.write("""
    • **What drives financial inclusion in Ethiopia?**
      Product launches (Telebirr, M-Pesa) > Infrastructure > Policy
    
    • **How do events affect inclusion outcomes?**
      Product launches have immediate impacts, policies have delayed effects
    
    • **How will inclusion look in 2025-2027?**
      Account ownership: 55-62%, Digital payments: 45-64%, Mobile money: 14-19%
    """)

# Footer
st.markdown("---")
st.markdown("*© 2026 Selam Analytics | Ethiopia Financial Inclusion Forecasting System | v1.0*")