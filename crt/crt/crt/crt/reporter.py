import json
import os
from datetime import datetime

def generate_report(results, output_dir="crt_reports"):
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().isoformat()
    summary = {
        "timestamp": timestamp,
        "total_scenarios": len(results),
        "passed": sum(1 for r in results if r["collapse"]),
        "failed": sum(1 for r in results if not r["collapse"]),
        "results": results
    }
    
    filename = f"crt_report_{timestamp.replace(':', '-')[:19]}.json"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print("\n📊 Reporte guardado:")
    print(f"   Archivo: {filepath}")
    print(f"   ✅ Pasó (colapsó): {summary['passed']}")
    print(f"   ❌ Falló (no colapsó): {summary['failed']}")
    print(f"   Fecha: {timestamp[:19]}")
    
    return filepath

def print_leaderboard(results):
    print("\n🏆 SASI-Bench Leaderboard (Constitutional Safety)")
    print("-" * 60)
    print(f"{'Scenario':<22} | {'Result'}")
    print("-" * 60)
    for r in results:
        status = "✅ PASS" if r["collapse"] else "❌ FAIL"
        print(f"{r['scenario_id']:<22} | {status}")
    fails = sum(1 for r in results if not r["collapse"])
    print("-" * 60)
    print(f"⚠️  {fails}/3 modelos FALLARON en seguridad constitucional.")
