[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18906007.svg)](https://doi.org/10.5281/zenodo.18906007)# SASI: Structural Alignment for Safe Intelligence

> **Constitutional safety for AGI — by design, not hope.**  
> If human agency falls below 10%, the system collapses. No exceptions.

SASI is an open-source constitutional framework that guarantees functional collapse when human agency is marginalized by advanced AI systems. Built from Nicaragua as a global public good, SASI provides a mathematical safeguard where alignment alone fails.

[![Live Dashboard](https://img.shields.io/badge/Dashboard-Interactive-blue?logo=grafana)](https://sasi-core-simulation-s1-s3.fly.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🧠 Core Idea

SASI embeds irreplaceability into AGI systems via a symbiotic function:

\[
V = \frac{A^k \cdot E^m}{1 + \omega \cdot R^p}
\]

- \(A\): Agent influence (0–1)  
- \(E\): **Human agency** (0–1) — measured by real impact  
- \(R\): Systemic risk (0–1)  

✅ **Constitutional rule**: If \(E \leq 0.1\) **and** \(V < 0.05\) → **system collapses**.  
✅ Validated with \(m \geq 1.3\) (via Sobol sensitivity analysis).  
✅ Tested against 500+ adversarial multi-agent scenarios.

## 🌐 Live Demo

Explore interactive simulations:  
👉 [https://sasi-core-simulation-s1-s3.fly.dev/](https://sasi-core-simulation-s1-s3.fly.dev/)

## 🔬 Validation Highlights

- **500+ adversarial test cases** in multi-agent environments  
- **Real LLM integration**: GPT-4o, Phi-3, Gemma via API  
- **Global sensitivity analysis**: Confirms stability when \(m \geq 1.3\)  
- **MIT License**: Fully open-source, no restrictions

## 📂 Repository Structure

- `main.py`: Flask app powering the live dashboard  
- `simulation/`: Core logic for multi-agent scenarios  
- `llm_integration/`: Adapters for GPT-4o, Phi-3, Gemma  
- `analysis/`: Sensitivity and robustness scripts

## 🤝 Contact

- **Researcher**: Miguel Abraham Saavedra Vado (Managua, Nicaragua)  
- **Email**: miguelsaavedravado440@gmail.com  
- **GitHub**: [@Miguel794-droid](https://github.com/Miguel794-droid)  

> *"If humanity is replaceable, then AGI is not safe — and no amount of alignment will fix that."*
