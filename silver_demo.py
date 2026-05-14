import pandas as pd
import matplotlib.pyplot as plt  # pyright: ignore[reportMissingImports]

# -----------------------------
# SILVER MARKET DATA SOURCES
# -----------------------------
sources = [
    {
        "Source": "LBMA Spot Price",
        "Freshness": 0.8,
        "ChangeRate": 0.2,
        "Cost": 4,
        "Utility": 0.45
    },
    {
        "Source": "News Sentiment",
        "Freshness": 0.9,
        "ChangeRate": 0.7,
        "Cost": 6,
        "Utility": 0.75
    },
    {
        "Source": "Futures Volume",
        "Freshness": 0.6,
        "ChangeRate": 0.4,
        "Cost": 3,
        "Utility": 0.50
    },
    {
        "Source": "Social Media Buzz",
        "Freshness": 0.5,
        "ChangeRate": 0.6,
        "Cost": 2,
        "Utility": 0.55
    }
]

df_sources = pd.DataFrame(sources)

print("\nSILVER MARKET DATA SOURCES")
print(df_sources)

# -----------------------------
# AGENT DECISION (SIMULATED)
# -----------------------------
selected_sources = [
    {"Source": "News Sentiment", "Cost": 6, "Utility": 0.75},
    {"Source": "Social Media Buzz", "Cost": 2, "Utility": 0.55}
]

budget_limit = 10
budget_used = 8

df_selected = pd.DataFrame(selected_sources)

print("\nAGENT SELECTED SOURCES")
print(df_selected)
print(f"\nBudget Limit: {budget_limit}")
print(f"Budget Used: {budget_used}")

# -----------------------------
# BASELINE vs AGENT GRAPH
# -----------------------------
time_steps = [0, 1, 2, 3, 4, 5]

baseline_cost = [0, 6, 12, 18, 24, 30]
agent_cost = [0, 6, 8, 10, 10, 12]

plt.figure(figsize=(8, 5))
plt.plot(time_steps, baseline_cost, label="Baseline (Fixed Collection)", linewidth=2)
plt.plot(time_steps, agent_cost, label="Agent (Utility-Based)", linewidth=2)

plt.xlabel("Time")
plt.ylabel("Cumulative Cost")
plt.title("Silver Prediction Market: Baseline vs Smart Agent")
plt.legend()
plt.grid(True)
plt.show()


