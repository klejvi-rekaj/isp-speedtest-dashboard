import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Real ISP Speedtest Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("speedtest_data.csv")

df = load_data()

st.title("📶 Real ISP Speedtest Dashboard")

df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")


st.metric("Average Download Speed (Mbps)", f"{df['download_speed_mbps'].mean():.2f}")
st.metric("Average Upload Speed (Mbps)", f"{df['upload_speed_mbps'].mean():.2f}")
st.metric("Average Ping (ms)", f"{df['ping_ms'].mean():.2f}")

st.markdown("---")


st.subheader("Download & Upload Speed Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["timestamp"], df["download_speed_mbps"], label="Download Speed (Mbps)", marker="o")
ax.plot(df["timestamp"], df["upload_speed_mbps"], label="Upload Speed (Mbps)", marker="x")
ax.set_xlabel("Time")
ax.set_ylabel("Speed (Mbps)")
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.markdown("---")


st.subheader("Ping Over Time")
fig2, ax2 = plt.subplots(figsize=(10, 3))
ax2.plot(df["timestamp"], df["ping_ms"], color="red", marker=".")
ax2.set_xlabel("Time")
ax2.set_ylabel("Ping (ms)")
ax2.grid(True)
st.pyplot(fig2)
