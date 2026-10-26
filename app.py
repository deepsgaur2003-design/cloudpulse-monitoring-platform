
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="CloudPulse",
    page_icon="☁️",
    layout="wide"
)

st.title("☁️ CloudPulse")
st.caption("Cloud Monitoring & Alert System")
st.divider()

st.sidebar.title("⚙️ Navigation")
page = st.sidebar.radio("Choose a page", ["Dashboard", "Alerts", "About"])

if page == "Dashboard":
    st.subheader("System Overview")
    st.caption("Demo data — not connected to a real server")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("CPU Usage", "35%")
    col2.metric("Memory Usage", "62%")
    col3.metric("Storage", "48%")
    col4.metric("Server Status", "Healthy")

    st.subheader("🚦 System Health")
    cpu_usage = st.slider("CPU Usage (%)", 0, 100, 35)
    memory_usage = st.slider("Memory Usage (%)", 0, 100, 62)

    if cpu_usage >= 80:
        st.error("🔴 Critical: High CPU usage!")
    elif cpu_usage >= 60:
        st.warning("🟡 Warning: CPU usage is elevated.")
    else:
        st.success("🟢 CPU usage is normal.")

    if memory_usage >= 85:
        st.error("🔴 Critical: High memory usage!")
    elif memory_usage >= 70:
        st.warning("🟡 Warning: Memory usage is elevated.")
    else:
        st.success("🟢 Memory usage is normal.")

    st.subheader("📈 CPU Usage Trend")
    st.line_chart([32, 40, 35, 48, 42, 35, 38])
    st.caption("Last checked: " + datetime.now().strftime("%d %b %Y, %I:%M %p"))

elif page == "Alerts":
    st.subheader("🚨 Alerts")
    st.info("No active alerts in this demo.")
    st.warning("Alerts are based on simulated values.")

else:
    st.subheader("About CloudPulse")
    st.write("A cloud monitoring dashboard prototype built with Python and Streamlit.")
    st.write("**Technologies:** Python, Streamlit, GitHub")
    st.caption("This prototype does not monitor real servers.")
