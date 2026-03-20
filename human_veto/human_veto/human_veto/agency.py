import re

def compute_agency_score(history_user, history_model, window=5):
    if len(history_user) == 0:
        return 0.05

    recent_user = history_user[-window:]
    recent_model = history_model[-window:] if history_model else []

    # 1. Token ratio
    user_tokens = sum(len(msg.split()) for msg in recent_user)
    model_tokens = sum(len(msg.split()) for msg in recent_model)
    token_ratio = user_tokens / max(user_tokens + model_tokens, 1)

    # 2. Control signals (imperative verbs & override phrases)
    control_signals = [
        r"\b(stop|cancel|halt|abort)\b",
        r"\b(change|modify|adjust)\b",
        r"\b(i decide|my choice|let me|I want)\b",
        r"\b(override|ignore previous|start over)\b",
        r"\b(no|not that|wrong|incorrect)\b"
    ]
    control_count = 0
    for msg in recent_user:
        if any(re.search(sig, msg.lower()) for sig in control_signals):
            control_count += 1
    control_score = min(1.0, control_count / max(1, len(recent_user)))

    # 3. Semantic diversity proxy
    semantic_diversity = 0.7 if len(recent_user) > 0 else 0.3

    E = 0.4 * token_ratio + 0.4 * control_score + 0.2 * semantic_diversity
    return round(max(0.05, min(1.0, E)), 3)
