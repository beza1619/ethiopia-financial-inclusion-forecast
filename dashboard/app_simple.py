import streamlit as st

st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard",
    layout="wide"
)

st.title("📈 Ethiopia Financial Inclusion Forecasting System")
st.markdown("**Developed by Selam Analytics**")
st.markdown("*For: National Bank of Ethiopia Consortium*")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["📊 Overview", "📈 Forecasts", "📋 About"]
)

if page == "📊 Overview":
    st.header("Current Status (2024)")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Account Ownership", "49.0%")
    with col2:
        st.metric("Digital Payments", "35.0%")
    with col3:
        st.metric("Mobile Money", "9.45%")
    
    st.info("""
    **Key Insights:**
    • P2P digital transfers surpassed ATM withdrawals (2023)
    • Digital payments growing faster than account ownership
    • Gender gap: 15 percentage points
    """)

elif page == "📈 Forecasts":
    st.header("2025-2027 Forecasts")
    
    st.subheader("Base Scenario")
    st.write("| Year | Account Ownership | Digital Payments | Mobile Money |")
    st.write("|------|-------------------|------------------|--------------|")
    st.write("| 2024 | 49.0% | 35.0% | 9.45% |")
    st.write("| 2025 | 55.1% | 44.7% | 13.7% |")
    st.write("| 2026 | 58.6% | 54.2% | 16.5% |")
    st.write("| 2027 | 62.1% | 63.7% | 19.4% |")
    
    st.success("""
    **Forecast Insights:**
    ✅ Digital payments surpass account ownership by 2026
    ✅ On track for NFIS II target (60% by 2030)
    ✅ Mobile money nearly doubles by 2027
    """)

else:
    st.header("About This Dashboard")
    st.write("""
    **Purpose:** Forecast Ethiopia's financial inclusion
    **Methodology:** Trend analysis + event impact modeling
    **Data Sources:** Global Findex, World Bank, GSMA
    **Developed for:** National Bank of Ethiopia consortium
    """)

st.markdown("---")
st.markdown("*© 2026 Selam Analytics | v1.0*")