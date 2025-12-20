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
          
