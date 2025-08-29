import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scripts import npa_metrics, report_pdf

st.set_page_config(page_title="NPA Analysis Dashboard", layout="wide")
st.title("📊 NPA Analysis Dashboard")

# Load Data
portfolio = pd.read_csv("data/sample_portfolio.csv")

# --- Summary Metrics ---
metrics = npa_metrics.calculate_npa_metrics(portfolio)
col1, col2, col3 = st.columns(3)
col1.metric("Total Loans (₹)", f"{metrics['Total Loans']:,}")
col2.metric("NPA Loans (₹)", f"{metrics['NPA Loans']:,}")
col3.metric("GNPA Ratio", f"{metrics['GNPA Ratio']*100:.2f}%")

st.markdown("---")

# --- Loan Status Distribution ---
st.subheader("Loan Status Distribution")
status_counts = portfolio["Status"].value_counts()
fig, ax = plt.subplots()
status_counts.plot(kind="bar", ax=ax)
ax.set_ylabel("Count")
ax.set_title("Loan Status Distribution")
st.pyplot(fig)

st.markdown("---")

# --- Portfolio Data ---
st.subheader("Portfolio Details")
st.dataframe(portfolio)

# --- Generate PDF Report ---
st.markdown("### Generate PDF Report")
if st.button("Create Report"):
    report_pdf.build_pdf("data/sample_portfolio.csv", "outputs/NPA_Report.pdf")
    st.success("PDF Report Generated in outputs/NPA_Report.pdf")
