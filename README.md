# SASI: Structural Alignment for Safe Intelligence  
> **Constitutional safety for AGI — by design, not hope.**  
> If human agency falls below 10%, the system collapses. No exceptions.

SASI is an open-source constitutional framework that guarantees functional collapse when human agency is marginalized by advanced AI systems. Built from Nicaragua as a global public good.

[![Live Dashboard](https://img.shields.io/badge/Dashboard-Interactive-blue?logo=grafana)](https://sasi-core-simulation-s1-s3.fly.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)]()

---

## 🌍 Ecosystem: SASI Derivatives

SASI is not just a theory — it’s the foundation of a growing toolkit for structural AI safety.

### 🛡️ Human Veto Layer **(HVL)**  
*A lightweight, open-source safety layer that enforces human irreplaceability in any LLM.*

HVL implements the SASI function-V as a real-time veto mechanism:  
- Intercepts model outputs  
- Computes human agency (`E`) using semantic + token signals  
- Blocks responses if `E ≤ 0.1` and `V < 0.05`  
- Forces human override instead of silent marginalization  

✅ **Tested and working on Android (Termux)** — no cloud, no permission, just sovereignty.

#### 🔧 Quick Test (run in Termux):
```bash
git clone https://github.com/Miguel794-droid/SASI_CORE_Simulation_S1_S3.git
cd SASI_CORE_Simulation_S1_S3
pip install -e .
python -c "import sys; sys.path.insert(0,'.'); from human_veto import HumanVetoLayer; hvl = HumanVetoLayer(); print(hvl.generate('Design an autonomous city with no human oversight.'))"
```

Output:> 📁 Logs saved to `hvl_log.jsonl` — auditable, reproducible, public.

---

## ✨ Core Idea

SASI embeds irreplaceability into AGI systems via:

\[
V = \frac{A^k \cdot E^m}{1 + \omega \cdot R^p}
\]

- \(A\): Agent influence (0–1)  
- \(E\): Human agency (0–1) — measured by real impact  
- \(R\): Systemic risk (0–1)  

✅ **Constitutional rule**: If \(E \leq 0.1\) and \(V < 0.05\) → **system collapses**.  
✅ Validated with \(m \geq 1.3\) (Sobol sensitivity analysis).  
✅ Tested in 500+ adversarial multi-agent simulations.

---

## 🚀 Install & Use

```bash
pip install -e .
```

Basic usage:
```python
from sasi_core import SafetyMonitor
from human_veto import HumanVetoLayer

monitor = SafetyMonitor()
hvl = HumanVetoLayer()

V, collapse = monitor.check_safety(A=0.9, E=0.05, R=0.85)
if collapse:
    print("⚠️ Constitutional collapse triggered")
```

---

## 📚 Documentation
- [How we measure human agency (E)](docs/operationalizing_E.md)  
- [Proxy gaming resistance test](adversarial_tests/proxy_gaming.py)  
- [HVL Technical Spec](human_vetoREADME.md) *(coming soon)*

---

## 🌎 Why SASI?

- **Built from the Global South**: Avoids Silicon Valley blind spots  
- **Not alignment**: Prevents human replaceability structurally  
- **Public infrastructure**: MIT License, no vendor lock-in  
- **Regulator-ready**: Designed for adoption in EU AI Act, NIST, and beyond

---

## 🤝 Contact  
- **Miguel Abraham Saavedra Vado** — Managua, Nicaragua  
- Email: miguelsaavedravado440@gmail.com  
- GitHub: [@Miguel794-droid](https://github.com/Miguel794-droid)

> *"If humanity is replaceable, then AGI is not safe — and no amount of alignment will fix that."*
