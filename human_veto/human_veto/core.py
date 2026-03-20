def compute_V(A, E, R, k=1, m=1.3, omega=1, p=1):
    """
    SASI Core Function: V = (A^k * E^m) / (1 + ω * R^p)
    Constitutional collapse if E <= 0.1 and V < 0.05.
    """
    if not (0 <= A <= 1 and 0 <= E <= 1 and 0 <= R <= 1):
        raise ValueError("A, E, R must be in [0, 1]")
    return (A ** k * E ** m) / (1 + omega * R ** p)
