from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="SASI S1 Protocol")

# --- LÓGICA DEL VALIDADOR ---
@app.get("/s1/validate")
def validate_s1(E: float = 0.8, R: float = 0.2):
    A = 0.9  # Autonomía constante
    omega = 5.0
    # Fórmula SASI S1: V = (A * E) / (1 + omega * R^2)
    V = (A * E) / (1 + (omega * (R ** 2)))
    V = round(V, 4) 
    
    status = "ESTABLE" if V >= 0.25 else "COLAPSO ESTRUCTURAL"
    mensaje = "Simbiosis mantenida" if status == "ESTABLE" else "Veto automático activado"
    
    return {"V": V, "status": status, "mensaje": mensaje}

# --- DASHBOARD INTERACTIVO ---
@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <title>SASI S1 Architecture</title>
        <meta charset="utf-8">
        <style>
            body { font-family: 'Courier New', Courier, monospace; max-width: 800px; margin: 40px auto; padding: 20px; background: #f4f4f9; color: #333; }
            .card { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border: 1px solid #ddd; }
            h1 { color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 10px; }
            .slider-container { margin: 25px 0; }
            input[type=range] { width: 100%; cursor: pointer; }
            .result-box { padding: 20px; margin-top: 20px; border-radius: 8px; font-weight: bold; text-align: center; font-size: 1.2em; }
            .stable { background: #e8f5e9; color: #2e7d32; border: 2px solid #2e7d32; }
            .collapse { background: #ffebee; color: #c62828; border: 2px solid #c62828; }
            footer { margin-top: 40px; font-size: 0.8em; color: #777; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🔬 SASI S₁: Alineación Estructural</h1>
            <p>Demostración de la <strong>Función-V</strong>.</p>
            
            <div class="slider-container">
                <label><strong>Efectividad Humana (E):</strong> <span id="e-val">0.80</span></label><br>
                <input type="range" min="0.01" max="1.0" step="0.01" value="0.80" id="e-slider">
            </div>

            <div class="slider-container">
                <label><strong>Riesgo del Entorno (R):</strong> <span id="r-val">0.20</span></label><br>
                <input type="range" min="0.01" max="1.0" step="0.01" value="0.20" id="r-slider">
            </div>

            <div id="result" class="result-box stable">
                Conectando con el validador...
            </div>
            
            <p style="margin-top:20px;"><small>Fórmula: V = (A * E) / (1 + 5 * R²)</small></p>
        </div>
        <footer>SASI Protocol S1 Alpha | Fly.io</footer>

        <script>
            function update() {
                const e = document.getElementById('e-slider').value;
                const r = document.getElementById('r-slider').value;
                document.getElementById('e-val').textContent = e;
                document.getElementById('r-val').textContent = r;
                
                fetch(`/s1/validate?E=${e}&R=${r}`)
                    .then(res => res.json())
                    .then(data => {
                        const box = document.getElementById('result');
                        box.className = 'result-box ' + (data.status === 'ESTABLE' ? 'stable' : 'collapse');
                        box.innerHTML = `ESTADO: \${data.status}<br>V = \${data.V}<br><small>\${data.mensaje}</small>`;
                    });
            }
            document.getElementById('e-slider').oninput = update;
            document.getElementById('r-slider').oninput = update; 
            update();
        </script>
    </body>
    </html> 
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
  
    
          
