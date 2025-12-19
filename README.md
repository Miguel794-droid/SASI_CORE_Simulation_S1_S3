# 🌍 SASI S₁ Validator – Alineación Estructural

> **"La alineación no debe ser una regla impuesta. Debe ser la condición de estabilidad del sistema."**

Este repositorio contiene un **validador mínimo de la Primera Simbiosis (S₁)** de la **Teoría Simbiótica de la Supra-inteligencia Artificial (SASI)**.

Este trabajo responde al **vacío de financiación en arquitecturas constitucionales de AGI** identificado por líderes del sector en 2025, especialmente para propuestas técnicas, verificables y desarrolladas desde el Sur Global.

---

## 🚀 Demo Ejecutable (Docker)
No es una AGI, es una **demostración de principio** ejecutable en 15 segundos:Este validador no implementa una IA ni un agente autónomo.
Funciona como una capa de validación estructural (validator layer) que demuestra cómo una arquitectura puede colapsar automáticamente cuando la agencia humana (E) cae por debajo de un umbral.
Su propósito es demostrar el principio, no resolver el problema completo.Endpoints
GET /
Información básica.
GET /s1/validate?E=0.05&R=0.2
El endpoint principal. Prueba el principio de colapso.
Ejemplos: curl "http://localhost:8000/s1/validate?E=0.8&R=0.2"
# → {"status":"ESTABLE","V":0.6,...}

curl "http://localhost:8000/s1/validate?E=0.05&R=0.2"
# → {"status":"COLLAPSE","V":0.038,...}
GET /metrics
Devuelve ejemplos estáticos y la caída relativa de V.
🧩 Relación con el Protocolo SASI Completo
Este módulo S₁ representa solo la capa evaluativa y de veto estructural. En la arquitectura completa, se integra con:
SOS (Orquestador de Sistemas Operativos Simbióticos)
CSI (Contrato Simbiótico)
SIM (Token Simbiótico)
CAV (Consejo de Veto)


```bash
docker build -t sasi-s1 .
docker run -p 8000:8000 sasi-s1



