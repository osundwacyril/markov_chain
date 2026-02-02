# M/M/1 Queue Simulation Using SimPy

## 📌 Project Overview

This project implements a **Markovian queueing system (M/M/1)** using **SimPy**, a professional discrete-event simulation framework in Python.

The system models:

* Poisson arrivals (rate λ)
* Exponential service times (rate μ)
* A single server
* FIFO (First-In-First-Out) queue discipline

This simulation is based on **continuous-time Markov chains (birth–death processes)** and is suitable for **Simulation & Modeling coursework** and real-world system analysis.

---

## 🎯 Objectives

The objectives of this project are to:

* Simulate an M/M/1 queue using SimPy
* Estimate key performance measures
* Compare simulation results with theoretical Markov queue formulas
* Demonstrate practical application of Markov chains in queueing systems

---

## 🧠 Theoretical Background

An M/M/1 queue is defined as:

* **M**: Markovian (Poisson arrivals)
* **M**: Markovian (Exponential service times)
* **1**: One server

Key formulas:

Traffic intensity:
[
\rho = \frac{\lambda}{\mu}
]

Stability condition:
[
\rho < 1
]

Average time in system:
[
W = \frac{1}{\mu - \lambda}
]

Average number in system:
[
L = \frac{\rho}{1 - \rho}
]

(Little’s Law):
[
L = \lambda W
]

---

## 🛠 Requirements

* Python 3.8 or higher
* SimPy library

Install SimPy:

```bash
pip install simpy
```

---

## 📁 Project Structure

```
MARKOV_CHAIN/
│
├── mm1_queue.py        # Main simulation script
├── README.md           # Project documentation
└── requirements.txt    # (Optional) Dependencies
```

---

## ▶️ How to Run

1. Clone or download the project
2. Install dependencies
3. Run the simulation:

```bash
python mm1_queue.py
```

---

## ⚙️ Simulation Parameters

Edit these in the script:

```python
LAMBDA = 4.0   # Arrival rate (λ)
MU = 6.0       # Service rate (μ)
SIM_TIME = 10000
```

---

## 📊 Output Metrics

The simulation reports:

* Average time in system (W)
* Server utilization (ρ)
* Comparison with theoretical results

Example output:

```
---- SimPy M/M/1 Results ----
λ = 4.0, μ = 6.0
Simulated W = 0.492
Theoretical W = 0.500
Utilization ρ = 0.667
```

---

## 🔗 Markov Chain Interpretation

The system is modeled as a **birth–death continuous-time Markov chain**:

```
0 ↔ 1 ↔ 2 ↔ 3 ↔ ...
  λ   λ   λ
  μ   μ   μ
```

Where:

* Births = arrivals
* Deaths = service completions
* State = number of customers in system


---


This project is useful for:

* Simulation & Modeling coursework
* Operations Research
* Network traffic modeling
* Call center and POS system analysis
* Cloud/server capacity planning

---


