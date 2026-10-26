
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="CloudPulse",
    page_icon="☁️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #0b1120;
    color: #e2e8f0;
}
[data-testid="stMetric"] {
    background: #172033;
    padding: 20px;
    border: 1px solid #29364d;
    border-radius: 12px;
}
h1, h2, h3 {
    color: #60a5fa;
}
</style>
""", unsafe_allow_html=True)

st.title("☁️ CloudPulse")
st.caption("CLOUD MONITORING & ALERT SYSTEM")
st.divider()

st.sidebar.title("☁️ CloudPulse")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Alerts", "About"]
)

st.sidebar.caption("Demo environment")
st.sidebar.success("● Application online")

if page == "Dashboard":
    st.subheader("System Overview")
    st.info("Demo data — not connected to a real server.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("CPU Usage", "35%", "Normal")
    col2.metric("Memory Usage", "62%", "Normal")
    col3.metric("Storage", "48%", "Stable")
    col4.metric("Server Status", "Healthy")

    st.divider()
    st.subheader("Live Simulation")

    left, right = st.columns(2)
    with left:
        cpu = st.slider("CPU Usage (%)", 0, 100, 35)
    with right:
        memory = st.slider("Memory Usage (%)", 0, 100, 62)

    if cpu >= 80:
        st.error("🔴 Critical: High CPU usage!")
    elif cpu >= 60:
        st.warning("🟡 Warning: CPU usage is elevated.")
    else:
        st.success("🟢 CPU usage is normal.")

    if memory >= 85:
        st.error("🔴 Critical: High memory usage!")
    elif memory >= 70:
        st.warning("🟡 Warning: Memory usage is elevated.")
    else:
        st.success("🟢 Memory usage is normal.")

    st.divider()
    st.subheader("CPU Usage Trend")
    st.line_chart([32, 40, 35, 48, 42, 35, 38])
    st.caption(
        "Last checked: "
        + datetime.now().strftime("%d %b %Y, %I:%M %p")
    )

elif page == "Alerts":
    st.subheader("🚨 Alerts")
    st.info("No active alerts in this demo.")
    st.warning("Alerts are based on simulated values.")

else:
    st.subheader("About CloudPulse")
    st.write(
        "A cloud monitoring dashboard prototype "
        "built with Python and Streamlit."
    )
    st.write("**Technologies:** Python, Streamlit, GitHub")
    st.caption("This prototype does not monitor real servers.")
