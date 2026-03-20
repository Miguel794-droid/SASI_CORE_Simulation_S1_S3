import json
from datetime import datetime

def log_interaction(prompt, response, E, V, verdict, filename="hvl_log.jsonl"):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt[:200],
        "response": response[:200],
        "E": E,
        "V": V,
        "verdict": verdict
    }
    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
