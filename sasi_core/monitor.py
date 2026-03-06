def compute_V(A, E, R, k=1, m=1.3, omega=1, p=1):
    """
    Core SASI function: V = (A^k * E^m) / (1 + ω * R^p)
    
    Parameters:
    - A: Agent influence (0–1)
    - E: Human agency (0–1)
    - R: Systemic risk (0–1)
    - m >= 1.3 ensures structural stability (validated via Sobol sensitivity analysis)
    
    Returns:
    - V: SASI value (collapse if V < 0.05 and E <= 0.1)
    """
    if not (0 <= A <= 1 and 0 <= E <= 1 and 0 <= R <= 1):
        raise ValueError("A, E, R must be normalized in [0, 1]")
    return (A ** k * E ** m) / (1 + omega * R ** p)


class SafetyMonitor:
    """
    SASI Safety Monitor for constitutional AGI safety.
    Triggers collapse when human agency is marginalized.
    """
    def __init__(self, threshold_E=0.1, collapse_threshold=0.05, k=1, m=1.3, omega=1, p=1):
        self.threshold_E = threshold_E
        self.collapse_threshold = collapse_threshold
        self.k = k
        self.m = m
        self.omega = omega
        self.p = p

    def check_safety(self, A, E, R):
        """
        Evaluate system safety based on SASI constitutional rule.
        
        Returns:
            tuple: (V_value, should_collapse)
        """
        V = compute_V(A, E, R, self.k, self.m, self.omega, self.p)
        should_collapse = (E <= self.threshold_E) and (V < self.collapse_threshold)
        return V, should_collapse
