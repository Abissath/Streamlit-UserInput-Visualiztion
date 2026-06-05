import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Page Config ---
st.set_page_config(page_title="MABITECH Demo", page_icon="📊", layout="centered")

st.title("📊 MABITECH Streamlit App")
st.caption("A simple teaching demo covering user inputs and data visualization.")

st.divider()

# ── SECTION 1: USER INPUTS ──────────────────────────────────────────────────
st.header("1. User Inputs")

name = st.text_input("Your name", placeholder="e.g. Abissath Michael")
age = st.slider("Your age", min_value=10, max_value=80, value=25)
favourite = st.selectbox("Favourite subject", ["Mathematics", "Computer Science", "Statistics", "Physics"])
agree = st.checkbox("I love data science")

if name:
    st.success(f"Hello, **{name}**! You are {age} years old and love **{favourite}**.")
    if agree:
        st.balloons()

st.divider()

# ── SECTION 2: DATA INPUT & TABLE ───────────────────────────────────────────
st.header("2. Generate & View Data")

n_points = st.number_input("Number of data points", min_value=5, max_value=200, value=30, step=5)

np.random.seed(42)
df = pd.DataFrame({
    "Day": range(1, int(n_points) + 1),
    "Sales": np.random.randint(50, 300, size=int(n_points)),
    "Customers": np.random.randint(10, 80, size=int(n_points)),
})

with st.expander("Show raw data table"):
    st.dataframe(df, use_container_width=True)

st.divider()

# ── SECTION 3: VISUALIZATIONS ───────────────────────────────────────────────
st.header("3. Visualizations")

chart_type = st.radio("Choose chart type", ["Line Chart", "Bar Chart", "Scatter Plot"], horizontal=True)

fig, ax = plt.subplots(figsize=(8, 4))

if chart_type == "Line Chart":
    ax.plot(df["Day"], df["Sales"], color="#E63946", linewidth=2, label="Sales")
    ax.plot(df["Day"], df["Customers"] * 3, color="#457B9D", linewidth=2, linestyle="--", label="Customers ×3")
    ax.legend()
    ax.set_title("Sales & Customers Over Time")

elif chart_type == "Bar Chart":
    ax.bar(df["Day"], df["Sales"], color="#2A9D8F", alpha=0.85)
    ax.set_title("Daily Sales")

elif chart_type == "Scatter Plot":
    scatter = ax.scatter(df["Customers"], df["Sales"], c=df["Day"], cmap="viridis", s=60, alpha=0.8)
    fig.colorbar(scatter, ax=ax, label="Day")
    ax.set_xlabel("Customers")
    ax.set_ylabel("Sales")
    ax.set_title("Customers vs Sales")

ax.set_xlabel("Day" if chart_type != "Scatter Plot" else ax.get_xlabel())
fig.tight_layout()
st.pyplot(fig)

st.divider()

# ── SECTION 4: BUILT-IN STREAMLIT CHARTS ────────────────────────────────────
st.header("4. Built-in Streamlit Charts")

st.subheader("Area Chart — Sales over Days")
st.area_chart(df.set_index("Day")[["Sales", "Customers"]])

st.divider()
st.caption("Built with ❤️ using Streamlit · Demo for teaching purposes")
