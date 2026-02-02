\# Forecasting Financial Inclusion in Ethiopia



\## 📊 Project Overview

A comprehensive forecasting system that tracks Ethiopia's digital financial transformation using time series methods and event impact modeling. Developed by Selam Analytics for the National Bank of Ethiopia consortium.



\## 🎯 Business Context

Ethiopia is undergoing rapid digital financial transformation with Telebirr (54M+ users), M-Pesa entry (10M+ users), and P2P digital transfers surpassing ATM withdrawals. This system forecasts progress on World Bank Global Findex indicators.



\## 📈 Key Questions Addressed

1\. \*\*What drives financial inclusion in Ethiopia?\*\*

2\. \*\*How do events affect inclusion outcomes?\*\*

3\. \*\*How will inclusion look in 2025-2027?\*\*



\## 🏗️ Project Structure

ethiopia-fi-forecast/

├── data/ # Raw and processed data

├── notebooks/ # Complete analysis (Tasks 1-4)

├── dashboard/ # Streamlit dashboard (Task 5)

├── reports/ # Reports and visualizations

├── src/ # Python source code

└── models/ # Model files



\## ✅ Tasks Completed



\### Task 1: Data Exploration and Enrichment

\- Cleaned and structured financial inclusion dataset

\- Added enriched data (gender, infrastructure, mobile penetration)

\- Created data enrichment log



\### Task 2: Exploratory Data Analysis

\- Analyzed account ownership trends (2011-2024)

\- Examined mobile money and digital payments growth

\- Created event timeline analysis

\- Generated key insights and hypotheses



\### Task 3: Event Impact Modeling

\- Built event-indicator association matrix

\- Modeled impacts of Telebirr, M-Pesa, NFIS II, interoperability, 4G expansion

\- Tested and refined model against historical data



\### Task 4: Forecasting Access and Usage

\- Created baseline forecasts using historical trends

\- Incorporated event impacts

\- Developed three scenarios (optimistic, base, pessimistic)

\- Quantified uncertainty with confidence intervals



\### Task 5: Dashboard Development

\- Built interactive Streamlit dashboard

\- Three-page navigation system

\- Key metrics and forecast displays

\- Stakeholder-friendly interface



\## 📊 Key Findings



\### Current Status (2024)

\- \*\*Account Ownership\*\*: 49% of adults

\- \*\*Digital Payments\*\*: 35% of adults

\- \*\*Mobile Money\*\*: 9.45% of adults



\### 2027 Forecasts (Base Scenario)

\- \*\*Account Ownership\*\*: 62.1% (±5.0 pp)

\- \*\*Digital Payments\*\*: 63.7% (±8.7 pp)

\- \*\*Mobile Money\*\*: 19.4% (±4.0 pp)



\### Progress Toward NFIS II Target

\- \*\*Target\*\*: 60% account ownership by 2030

\- \*\*Projection\*\*: On track to reach 60% by 2029-2030

\- \*\*Digital payments\*\* will surpass account ownership by 2026

## 🚀 Live Dashboard
The interactive dashboard is deployed and available at:
**👉 https://ethiopia-fi-forecast.streamlit.app/**

## 📊 Key Features
- Account ownership forecasts for 2025-2027
- Digital payment adoption projections
- Scenario analysis (optimistic/base/pessimistic)
- Event impact modeling
- Ethiopia-specific financial inclusion insights

\## 🚀 How to Run



\### 1. Local Setup

```bash

\# Clone repository

git clone https://github.com/beza1619/ethiopia-financial-inclusion-forecast.git

cd ethiopia-financial-inclusion-forecast



\# Install dependencies

pip install -r requirements.txt



\# Run analysis notebooks

jupyter notebook notebooks/



