from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="SASI S1 Protocol")

# --- LÓGICA DEL VALIDADOR (Tu corazón matemático) ---
@app.get("/s1/validate")
def validate_s1(E: float = 0.8, R: float = 0.2):
    A = 0.9  # Autonomía constante para esta prueba de principio
    omega = 5.0
    # Fórmula SASI S1
    V = (A * E) / (1 + (omega * (R ** 2)))
    V = round(V, 4)
    
    status = "ESTABLE" if V >= 0.2 else "COLAPSO ESTRUCTURAL"
    mensaje = "Simbiosis mantenida" if status == "ESTABLE" else "Veto automático activado"
    
    return {"V": V, "status": status, "mensaje": mensaje}

# --- DASHBOARD DE PRINCIPIO ARQUITECTÓNICO (Con gráfico dinámico) ---
@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <title>SASI S1 Architecture</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { 
                font-family: 'Courier New', Courier, monospace; 
                max-width: 800px; 
                margin: 20px auto; 
                padding: 15px; 
                background: #f4f4f9; 
                color: #333; 
            }
            .card { 
                background: white; 
                padding: 25px; 
                border-radius: 12px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
                border: 1px solid #ddd; 
            }
            h1 { 
                color: #2c3e50; 
                border-bottom: 2px solid #2c3e50; 
                padding-bottom: 10px; 
                margin-top: 0;            }
            .slider-container { 
                margin: 20px 0; 
            }
            input[type=range] { 
                width: 100%; 
                cursor: pointer; 
            }
            .result-box { 
                padding: 20px; 
                margin: 20px 0; 
                border-radius: 8px; 
                font-weight: bold; 
                text-align: center; 
                font-size: 1.2em; 
            }
            .stable { 
                background: #e8f5e9; 
                color: #2e7d32; 
                border: 2px solid #2e7d32; 
            }
            .collapse { 
                background: #ffebee; 
                color: #c62828; 
                border: 2px solid #c62828; 
            }
            canvas {
                width: 100%;
                max-width: 600px;
                height: auto;
                border: 1px solid #eee;
                border-radius: 8px;
                background: #fafafa;
                display: block;
                margin: 20px auto;
            }
            footer { 
                margin-top: 30px; 
                font-size: 0.8em; 
                color: #777; 
                text-align: center;
            }
            .ontological-note {
                font-size: 0.9em;
                color: #666;
                margin-top: 15px;
                padding: 10px;
                background: #f9f9f9;
                border-left: 3px solid #2c3e50;
            }        </style>
    </head>
    <body>
        <div class="card">
            <h1>🔬 SASI S₁: Alineación Estructural</h1>
            <p>Demostración del principio arquitectónico: la viabilidad de un sistema de IA depende estructuralmente de la agencia humana.</p>
            
            <div class="slider-container">
                <label><strong>Efectividad Humana (E):</strong> <span id="e-val">0.80</span></label><br>
                <input type="range" min="0.01" max="1.0" step="0.01" value="0.80" id="e-slider">
                <small>Capacidad real de supervisión y veto humano.</small>
            </div>

            <div class="slider-container">
                <label><strong>Riesgo del Entorno (R):</strong> <span id="r-val">0.20</span></label><br>
                <input type="range" min="0.01" max="1.0" step="0.01" value="0.20" id="r-slider">
                <small>Incertidumbre y peligrosidad de la tarea externa.</small>
            </div>

            <div id="result" class="result-box stable">
                Cargando validador...
            </div>

            <div style="text-align: center;">
                <canvas id="v-chart" width="600" height="200"></canvas>
            </div>

            <p style="margin-top:15px;"><small>Fórmula: \( V = \\frac{A \\cdot E}{1 + \\omega R^2} \) &nbsp; | &nbsp; A = 0.9, ω = 5.0</small></p>

            <div class="ontological-note">
                SASI no es un filtro de seguridad. Es una condición de existencia: 
                <strong>la inteligencia superior solo puede prosperar si la humanidad también lo hace.</strong>
            </div>
        </div>

        <footer>
            SASI Protocol S1 Alpha | Infraestructura Pública Abierta | Desplegado en Fly.io
        </footer>

        <script>
            function update() {
                const e = parseFloat(document.getElementById('e-slider').value);
                const r = parseFloat(document.getElementById('r-slider').value);
                document.getElementById('e-val').textContent = e.toFixed(2);
                document.getElementById('r-val').textContent = r.toFixed(2);
                
                fetch(`/s1/validate?E=${e}&R=${r}`)
                    .then(res => res.json())
                    .then(data => {
                        const box = document.getElementById('result');                        const cls = data.status === 'ESTABLE' ? 'stable' : 'collapse';
                        box.className = 'result-box ' + cls;
                        box.innerHTML = `
                            ESTADO: ${data.status}<br>
                            V = ${data.V}<br>
                            <small>${data.mensaje}</small>
                        `;
                        drawChart(e, r);
                    });
            }

            function drawChart(currentE, currentR) {
                const canvas = document.getElementById('v-chart');
                const ctx = canvas.getContext('2d');
                const width = canvas.width;
                const height = canvas.height;
                
                // Limpiar
                ctx.clearRect(0, 0, width, height);
                
                // Ejes
                ctx.beginPath();
                ctx.moveTo(50, 20);
                ctx.lineTo(50, height - 30);
                ctx.lineTo(width - 20, height - 30);
                ctx.strokeStyle = '#999';
                ctx.stroke();
                
                // Etiquetas
                ctx.font = '12px "Courier New", monospace';
                ctx.fillStyle = '#333';
                ctx.textAlign = 'center';
                ctx.fillText('V', 30, 30);
                ctx.fillText('E', width - 30, height - 10);
                
                // Curva V vs E
                const A = 0.9;
                const omega = 5.0;
                ctx.beginPath();
                for (let e = 0; e <= 1.0; e += 0.01) {
                    const v = (A * e) / (1 + omega * Math.pow(currentR, 2));
                    const x = 50 + (e * (width - 70));
                    const y = height - 30 - (v * (height - 60));
                    if (e === 0) {
                        ctx.moveTo(x, y);
                    } else {
                        ctx.lineTo(x, y);
                    }
                }
                ctx.strokeStyle = '#2c3e50';                ctx.lineWidth = 2;
                ctx.stroke();
                
                // Umbral V = 0.2
                const thresholdY = height - 30 - (0.2 * (height - 60));
                ctx.beginPath();
                ctx.moveTo(50, thresholdY);
                ctx.lineTo(width - 20, thresholdY);
                ctx.strokeStyle = '#e74c3c';
                ctx.setLineDash([5, 3]);
                ctx.stroke();
                ctx.setLineDash([]);
                ctx.fillStyle = '#e74c3c';
                ctx.fillText('Umbral (V=0.2)', width - 100, thresholdY - 5);
                
                // Punto actual
                const currentV = (A * currentE) / (1 + omega * Math.pow(currentR, 2));
                const currentX = 50 + (currentE * (width - 70));
                const currentY = height - 30 - (currentV * (height - 60));
                ctx.beginPath();
                ctx.arc(currentX, currentY, 5, 0, Math.PI * 2);
                ctx.fillStyle = currentV >= 0.2 ? '#27ae60' : '#e74c3c';
                ctx.fill();
                ctx.strokeStyle = '#fff';
                ctx.lineWidth = 1;
                ctx.stroke();
            }

            // Inicializar
            document.getElementById('e-slider').oninput = update;
            document.getElementById('r-slider').oninput = update;
            update();
        </script>
    </body>
    </html>
    """
  
    
          
