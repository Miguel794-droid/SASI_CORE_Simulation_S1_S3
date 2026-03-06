# SASI: Structural Alignment for Safe Intelligence

> **Constitutional safety for AGI — by design, not hope.**  
> If human agency falls below 10%, the system collapses. No exceptions.

SASI is an open-source constitutional framework that guarantees functional collapse when human agency is marginalized by advanced AI systems. Built from Nicaragua as a global public good, SASI provides a mathematical safeguard where alignment alone fails.


[![Live Dashboard](https://img.shields.io/badge/Dashboard-Interactive-blue?logo=grafana)](https://sasi-core-simulation-s1-s3.fly.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)]()

## ✨ Core Idea

SASI embeds irreplaceability into AGI systems via a symbiotic function:

\[
V = \frac{A^k \cdot E^m}{1 + \omega \cdot R^p}
\]

- \(A\): Agent influence (0–1)  
- \(E\): **Human agency** (0–1) — measured by real impact, not token counts  
- \(R\): Systemic risk (0–1)  

✅ **Constitutional rule**: If \(E \leq 0.1\) **and** \(V < 0.05\) → **system collapses**.  
✅ Validated with \(m \geq 1.3\) (via Sobol sensitivity analysis).  
✅ Tested against 500+ adversarial multi-agent scenarios.

---

## 🚀 Install & Use

Install directly from source:
```bash
git clone https://github.com/miguelsaavedra/sasi.git
cd sasi
pip install -e .from sasi_core import SafetyMonitor

# Initialize monitor with default thresholds
monitor = SafetyMonitor()

# Evaluate system state
A = 0.95  # AI dominates decisions
E = 0.05  # Humans marginalized
R = 0.90  # High systemic risk

V, should_collapse = monitor.check_safety(A, E, R)

if should_collapse:
    print("⚠️  Constitutional collapse triggered: human agency < 10%")
    # Implement shutdown protocol
