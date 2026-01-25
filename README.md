# Link of dashboard(Agent)
https://agent-viz-builder.preview.emergentagent.com/


# Smart Silver Monitor

##  Overview

Smart Silver Monitor is a **cost-aware autonomous monitoring prototype** that demonstrates how an intelligent agent can **decide when data is worth collecting** instead of blindly polling at fixed intervals.

The system operates on a simulated silver market and shows how **selective data collection** can significantly reduce costs **without missing critical market anomalies**.

---

##  Problem Statement

Most monitoring systems continuously collect data at fixed intervals, even when there is little or no meaningful change.
This leads to:

* Unnecessary API costs
* Wasted computational resources
* Information overload

**The core problem:**
 *How can we monitor a dynamic system efficiently without wasting resources on unnecessary data collection?*

---

##  Solution

We built an **autonomous agent** that:

* Monitors market volatility
* Evaluates expected information gain vs cost
* Collects data only when it is valuable
* Overrides cost limits during critical anomalies

The agent remains **IDLE** (sleep mode) during stable periods and becomes **ACTIVE** only when significant changes are detected.

---

##  How the Agent Works (High Level)

1. A simulated silver market generates price and volatility data
2. The agent evaluates each time step
3. If volatility is low → agent SKIPS data collection
4. If volatility spikes → agent COLLECTS data (anomaly detected)
5. All decisions and costs are logged
6. A dashboard visualizes behavior and savings

---

## Project Structure

```
smart-silver-monitor/
│
├── dashboard/
│   └── dashboard.py            # Streamlit dashboard for visualization
│
├── data/
│   ├── silver_market_data.csv  # Simulated silver market prices & volatility
│   ├── simulation_results.csv  # Agent decisions, actions, and reasoning
│   └── cost_comparison.csv     # Baseline vs agent cost over time
│
├── agent_logic/
│   └── agent_design.md         # Explanation of agent decision logic
│
└── README.md                   # Project documentation
```

---

## Data Files Description

* **silver_market_data.csv**
  Simulated market environment containing silver prices and volatility.

* **simulation_results.csv**
  Logs every agent decision (COLLECT / SKIP / OVERRIDE) along with reasons.

* **cost_comparison.csv**
  Compares the cost of a fixed data collection schedule vs the autonomous agent.

---

## 📈 Key Visualizations

* Silver market price trend
* Agent decision behavior
* Cost comparison between baseline and agent

These visualizations clearly demonstrate **cost savings and intelligent behavior**.

---

##  How to Run the Dashboard

### Prerequisites

* Python 3.x
* Streamlit
* Pandas

### Steps

```bash
pip install streamlit pandas
streamlit run dashboard/dashboard.py
```

The dashboard will open at:

```
http://localhost:8501
```

---

##  Real-World Applications

This approach can be applied to:

* Financial market monitoring
* Cloud infrastructure monitoring
* IoT and sensor networks
* Social media trend detection
* Any system where data collection has a cost

---

##  Prototype Note

This project is a **prototype** built for experimentation and demonstration.
The market data is simulated, and CSV files are used for simplicity.
In production, these would be replaced with real-time APIs and databases.

---

## Team Contribution

* **Agent Logic:** Decision-making and anomaly detection
* **Simulation:** Synthetic market and cost modeling
* **Dashboard:** Visualization and explanation layer

---
