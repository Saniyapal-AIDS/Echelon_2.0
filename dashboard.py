import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Silver Prediction Market", layout="wide")

st.title("🥈 Silver Prediction Market")
st.caption("Autonomous AI Agent for Cost-Efficient Market Intelligence")
st.caption("🔄 Live dashboard — updates every few seconds")

# CSV load
simulation_df = pd.read_csv(
   r"C:\Users\mrutk\OneDrive\Desktop\Mindspark\simulation_results.csv"
)
cost_df = pd.read_csv(
    r"C:\Users\mrutk\OneDrive\Desktop\Mindspark\cost_comparison.csv"
)
cost_df.columns = cost_df.columns.str.strip().str.lower()

st.subheader("📈 Market Snapshot")
latest = simulation_df.iloc[-1]

c1, c2, c3 = st.columns(3)
c1.metric("Source", latest["source"])
c2.metric("Silver Price", f"${latest['silver_price']}")
c3.metric("Action", latest["action"])

# -------- Decision Log --------
st.subheader("🧠 Agent Decision Log")
st.dataframe(
    simulation_df[
        ["minute", "source", "action", "silver_price", "reason"]
    ],
    use_container_width=True
)

# -------- Cost Comparison --------
st.subheader("💰 Cost Efficiency: Baseline vs Agent")
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(
    cost_df["minute"],
    cost_df["fixed_schedule_cost"],
    label="Baseline (Fixed Schedule)",
    linewidth=2
)

ax.plot(
    cost_df["minute"],
    cost_df["autonomous_agent_cost"],
    label="Autonomous Agent",
    linewidth=2
)


ax.set_xlabel("Time")
ax.set_ylabel("Cumulative Cost")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# -------- Savings --------
st.success(
    f"💡 Total Cost Saved: "
    f"{cost_df['fixed_schedule_cost'].iloc[-1] - cost_df['autonomous_agent_cost'].iloc[-1]}"
)

