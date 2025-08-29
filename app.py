
import streamlit as st
import pandas as pd
from scripts import npa_metrics

st.title("NPA Analysis Dashboard")

# Load data
portfolio = pd.read_csv("data/sample_portfolio.csv")
st.subheader("Portfolio Data")
st.dataframe(portfolio.head())

# Metrics
metrics = npa_metrics.calculate_npa_metrics(portfolio)
st.subheader("NPA Metrics")
st.write(metrics)
