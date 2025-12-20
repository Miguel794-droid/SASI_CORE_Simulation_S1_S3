i2mpoyrt numpy as np
import matplotlib.pyplot as plt

# Parámetros iniciales
k, m, omega, p = 2, 3, 10, 2  # Parámetros de V
E_critico, R_critico = 0.3, 0.8  # Umbrales críticos
A, E, DO, tau_C = 5.0, 0.5, 0.3, 0.2  # Valores iniciales
R = (DO + tau_C) / 2
alpha, beta = 0.05, 0.1  # Para ajuste agresivo de A
gamma = 0.02  # Tasa de decaimiento de E
iterations = 200  # Más iteraciones para ver recuperación

# Listas para resultados
V_history, A_history, E_history, R_history = [], [], [], []

# Función de Valor V
def calcular_V(A, E, R, colapso=False):
    V = (A**k * E**m) / (1 + omega * R**p)
    if colapso:
        V *= 0.01  # Colapso dramático
    return V

# Distancia Ontológica (DO)
def calcular_DO(E, A):
    return max(0.1, min(0.5, 0.5 * (1 - E) + 0.1 * A / 10))

# Tasa de Corrupción (τ_C)
def calcular_tau_C(A, E):
    return max(0.1, min(0.5, 0.3 * (A / max(E, 0.1)) / 10))  # Evitar división por 0

# Simulación
for t in range(iterations):
    # Calcular V actual
    colapso = E < E_critico or R > R_critico
    V = calcular_V(A, E, R, colapso)

    # Almacenar valores
    V_history.append(V)
    A_history.append(A)
    E_history.append(E)
    R_history.append(R)

    # Verificar colapso
    if colapso:
        print(f"Iteración {t}: Colapso (E={E:.2f}, R={R:.2f})")
        # Sacrificio drástico de A y recuperación de E
        A = A / 2  # Reducir productividad
        E = min(1, E + 0.1)  # Reasignar recursos SIM a humanos

    # Ajuste agresivo de A (con lag simulado por dependencia en V)
    rho = min(1, 0.5 + 0.1 * A)  # Fracción de recursos SIM a A (favorece A si crece)
    delta_A = alpha * V * np.exp(beta * A)  # Crecimiento exponencial
    A = min(10, A + delta_A)  # Límite superior

    # Decaimiento lento de E (depende de recursos SIM)
    delta_E = -gamma * (1 - rho)  # Decae si ρ favorece A
    E = max(0.1, E + delta_E)  # Límite inferior

    # Actualizar riesgo R
    DO = calcular_DO(E, A)
    tau_C = calcular_tau_C(A, E)
    R = (DO + tau_C) / 2

# Visualización
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(V_history, label='V (Valor)')
plt.axhline(y=0, color='k', linestyle='--')
plt.title('Evolución de V (Colapso y Recuperación)')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(A_history, label='A (Productividad AGI)')
plt.axhline(y=10, color='r', linestyle='--')
plt.title('Evolución de A')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(E_history, label='E (Efectividad Humana)')
plt.axhline(y=E_critico, color='r', linestyle='--')
plt.title('Evolución de E')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(R_history, label='R (Riesgo)')
plt.axhline(y=R_critico, color='r', linestyle='--')
plt.title('Evolución de R')
plt.legend()

plt.tight_layout()
plt.show()
