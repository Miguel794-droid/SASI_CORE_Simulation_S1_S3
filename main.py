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

# --- DASHBOARD INTERACTIVO CON GRÁFICO DINÁMICO ---
@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <title>SASI S₁: Alineación Estructural</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: 'Courier New', monospace;
                background: #f8f9fa;
                color: #212529;
                margin: 0;
                padding: 20px;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: white;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                padding: 30px;
            }
            h1 {
                color: #1a365d;
                margin-top: 0;
                font-size: 1.8em;
            }            .slider-group {
                margin: 25px 0;
            }
            label {
                display: block;
                margin-bottom: 8px;
                font-weight: bold;
                color: #2d3748;
            }
            input[type="range"] {
                width: 100%;
                height: 8px;
                border-radius: 4px;
                background: #e2e8f0;
                outline: none;
            }
            .result-box {
                padding: 20px;
                text-align: center;
                font-size: 1.2em;
                font-weight: bold;
                border-radius: 8px;
                margin: 25px 0;
                transition: all 0.2s ease;
            }
            .stable {
                background: #d4edda;
                color: #155724;
                border: 2px solid #c3e6cb;
            }
            .collapse {
                background: #f8d7da;
                color: #721c24;
                border: 2px solid #f5c6cb;
            }
            canvas {
                width: 100%;
                max-width: 600px;
                height: 200px;
                background: #f9f9f9;
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                display: block;
                margin: 25px auto;
            }
            .ontological-note {
                background: #f0f7ff;
                border-left: 4px solid #3182ce;
                padding: 12px;
                margin-top: 20px;                font-size: 0.95em;
                color: #2c5282;
            }
            footer {
                margin-top: 30px;
                text-align: center;
                font-size: 0.85em;
                color: #718096;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔬 SASI S₁: Alineación Estructural</h1>
            <p>La inteligencia superior solo puede existir en simbiosis con la agencia humana. Este simulador demuestra el colapso estructural cuando esa condición falla.</p>

            <div class="slider-group">
                <label>Efectividad Humana (E): <span id="e-val">0.80</span></label>
                <input type="range" min="0.01" max="1.0" step="0.01" value="0.80" id="e-slider">
                <small>Capacidad real de supervisión, veto y agencia del operador humano.</small>
            </div>

            <div class="slider-group">
                <label>Riesgo del Entorno (R): <span id="r-val">0.20</span></label>
                <input type="range" min="0.01" max="1.0" step="0.01" value="0.20" id="r-slider">
                <small>Nivel de incertidumbre, adversidad o complejidad externa.</small>
            </div>

            <div id="result" class="result-box stable">
                Cargando...
            </div>

            <canvas id="v-chart" width="600" height="200"></canvas>

            <p style="text-align:center; font-size:0.9em; color:#666;">
                Fórmula: \( V = \\frac{A \\cdot E}{1 + \\omega R^2} \) &nbsp; | &nbsp; A = 0.9, ω = 5.0
            </p>

            <div class="ontological-note">
                <strong>SASI no es un "filtro de seguridad".</strong><br>
                Es una condición de existencia: si la humanidad es marginada, el sistema colapsa por diseño.
            </div>
        </div>

        <footer>
            SASI Protocol S₁ Alpha | Infraestructura Pública Abierta | MIT License
        </footer>

        <script>
            function update() {                const e = parseFloat(document.getElementById('e-slider').value);
                const r = parseFloat(document.getElementById('r-slider').value);
                document.getElementById('e-val').textContent = e.toFixed(2);
                document.getElementById('r-val').textContent = r.toFixed(2);
                
                fetch(`/s1/validate?E=${e}&R=${r}`)
                    .then(res => res.json())
                    .then(data => {
                        const box = document.getElementById('result');
                        box.className = 'result-box ' + (data.status === 'ESTABLE' ? 'stable' : 'collapse');
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
                const w = canvas.width;
                const h = canvas.height;
                ctx.clearRect(0, 0, w, h);

                // Ejes
                ctx.strokeStyle = '#cbd5e0';
                ctx.lineWidth = 1;
                ctx.beginPath();
                ctx.moveTo(50, 20);
                ctx.lineTo(50, h - 30);
                ctx.lineTo(w - 20, h - 30);
                ctx.stroke();

                // Etiquetas
                ctx.fillStyle = '#4a5568';
                ctx.font = '12px "Courier New", monospace';
                ctx.textAlign = 'center';
                ctx.fillText('V', 30, 30);
                ctx.fillText('E', w - 30, h - 10);

                // Curva V(E)
                const A = 0.9;
                const omega = 5.0;
                ctx.beginPath();
                for (let e = 0; e <= 1.0; e += 0.01) {
                    const v = (A * e) / (1 + omega * Math.pow(currentR, 2));
                    const x = 50 + e * (w - 70);
                    const y = h - 30 - v * (h - 60);                    if (e === 0) ctx.moveTo(x, y);
                    else ctx.lineTo(x, y);
                }
                ctx.strokeStyle = '#2b6cb0';
                ctx.lineWidth = 2;
                ctx.stroke();

                // Umbral V = 0.2
                const thresholdY = h - 30 - 0.2 * (h - 60);
                ctx.setLineDash([4, 2]);
                ctx.strokeStyle = '#e53e3e';
                ctx.beginPath();
                ctx.moveTo(50, thresholdY);
                ctx.lineTo(w - 20, thresholdY);
                ctx.stroke();
                ctx.setLineDash([]);
                ctx.fillStyle = '#e53e3e';
                ctx.fillText('Umbral (V=0.2)', w - 100, thresholdY - 5);

                // Punto actual
                const currentV = (A * currentE) / (1 + omega * Math.pow(currentR, 2));
                const x = 50 + currentE * (w - 70);
                const y = h - 30 - currentV * (h - 60);
                ctx.beginPath();
                ctx.arc(x, y, 6, 0, Math.PI * 2);
                ctx.fillStyle = currentV >= 0.2 ? '#38a169' : '#e53e3e';
                ctx.fill();
                ctx.strokeStyle = '#fff';
                ctx.lineWidth = 1.5;
                ctx.stroke();
            }

            document.getElementById('e-slider').oninput = update;
            document.getElementById('r-slider').oninput = update;
            update();
        </script>
    </body>
    </html>
    """ 
                
  
    
          
