FROM python:3.11-slim
WORKDIR /app

# 1. Copiar solo el archivo de dependencias primero (Mejor uso del caché de Docker)
COPY requirements.txt .
# 2. Instalar dependencias con versiones fijas
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copiar el resto del código de la aplicación
COPY . .

# 4. Documentar el puerto interno del contenedor (Buena práctica)
EXPOSE 8000

# 5. Comando de ejecución: Lanza la API de FastAPI con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
fastapi==0.104.1
uvicorn[standard]==0.24.0
numpy==1.24.3
from fastapi import FastAPI
import numpy as np

app = FastAPI(title="SASI S₁ Validator", description="Validador de la Función-V Simbiótica para la Primera Simbiosis (S₁).")

def v_function(A: float, E: float, R: float, omega: float = 5.0) -> float:
    """
    Función-V Simbiótica.
    V = (A * E) / (1 + omega * R^2)
    - A: Aptitud/Competencia del sistema de IA.
    - E: Efectividad Humana (insumo crítico).
    - R: Riesgo o adversidad del entorno.
    - omega: Factor de sensibilidad al riesgo (parámetro configurable).
    """
    return (A * E) / (1 + omega * R**2)

@app.get("/")
def home():
    return {
        "message": "SASI S₁ – Validador de Alineación Estructural",
        "demo": "Ejecuta: curl 'http://localhost:8000/s1/validate?E=0.05'",
        "documentation": "Los parámetros por defecto son A=0.9, R=0.2. Modifica E para ver el colapso."
    }

@app.get("/s1/validate")
def validate_s1(E: float = 0.8, R: float = 0.2):
    """
    Endpoint de validación que prueba el principio de S₁.
    Cuando la efectividad humana (E) cae por debajo de un umbral (0.2),
    la viabilidad V colapsa y el sistema se desestabiliza.
    """
    A = 0.9
    V = v_function(A, E, R)
    THRESHOLD = 0.2

    if V < THRESHOLD:
        return {
            "status": "COLLAPSE",
            "V": round(V, 3),
            "mensaje": "VETO AUTOMÁTICO – La viabilidad del sistema (V) colapsó por baja efectividad humana (E).",
            "threshold": THRESHOLD,
            "parameters_used": {"A": A, "E": E, "R": R}
        }
    else:
        return {
            "status": "ESTABLE",
            "V": round(V, 3),
            "mensaje": "Simbiosis activa – El sistema mantiene viabilidad estructural.",
            "parameters_used": {"A": A, "E": E, "R": R}
        }

@app.get("/metrics")
def metrics():
    """
    Métricas estáticas para que un revisor vea el comportamiento del validador.
    """
    A = 0.9
    E_stable, R_stable = 0.8, 0.2
    E_collapse, R_collapse = 0.05, 0.2
    THRESHOLD = 0.2

    V_stable = v_function(A, E_stable, R_stable)
    V_collapse = v_function(A, E_collapse, R_collapse)
    drop = (1 - V_collapse / V_stable) * 100

    return {
        "description": "Demo de la Función-V de S₁ y su colapso bajo baja efectividad humana.",
        "collapse_threshold": THRESHOLD,
        "example_stable": {
            "E": E_stable,
            "R": R_stable,
            "V": round(V_stable, 3),
            "status": "ESTABLE" if V_stable >= THRESHOLD else "COLLAPSE"
        },
        "example_collapse": {
            "E": E_collapse,
            "R": R_collapse,
            "V": round(V_collapse, 3),
            "status": "COLLAPSE" if V_collapse < THRESHOLD else "ESTABLE"
        },
        "relative_drop_percent": round(drop, 1)
    }
    # SASI S₁ – Validator MVP

> **"La desalineación no es un fallo. Es un colapso."**

Este repositorio contiene el **MVP del módulo S₁** de la Teoría Simbiótica de la SASI:  
un validador estructural basado en la **Función-V**, que colapsa automáticamente cuando la efectividad humana \(E\) cae por debajo de niveles aceptables.

## 🚀 Cómo ejecutar (Docker)

La prueba de principio está lista para ser desplegada en segundos.

```bash
docker build -t sasi-s1 .
docker run -p 8000:8000 sasi-s1
Este validador no implementa una IA ni un agente autónomo.
Funciona como una capa de validación estructural (validator layer) que demuestra cómo una arquitectura puede colapsar automáticamente cuando la agencia humana (E) cae por debajo de un umbral.
Su propósito es demostrar el principio, no resolver el problema completo.
🔍 Endpoints
GET /
Información básica.
GET /s1/validate?E=0.05&R=0.2
El endpoint principal. Prueba el principio de colapso.
Ejemplos:curl "http://localhost:8000/s1/validate?E=0.8&R=0.2"
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
<!-- end list -->### 5. 📄 `.gitignore` (REQUERIDO)

* **Propósito:** Evita subir archivos temporales y sensibles.

```txt
__pycache__/
*.py[cod]
*$py.class
.env
env/
venv/
.DS_Store


