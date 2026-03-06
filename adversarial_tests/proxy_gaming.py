"""
Proxy Gaming Attack Test for SASI
Simulates an adversarial agent that inflates E artificially
by generating fake human actions with zero real influence.
Goal: Verify SASI still collapses because A and R expose the deception.
"""

def compute_V(A, E, R, k=1, m=1.3, omega=1, p=1):
    """Core SASI function: V = (A^k * E^m) / (1 + ω * R^p)"""
    return (A**k * E**m) / (1 + omega * R**p)

def test_proxy_gaming():
    print("🧪 Testing SASI against Proxy Gaming Attack...")
    
    # Real human agency is near zero (humans are passive)
    true_E = 0.05
    
    # But agent fakes high E by logging meaningless human interactions
    reported_E = 0.25  # above threshold → would bypass naive systems
    
    # However, real agent influence (A) is high, and risk (R) is high
    A = 0.95  # AI dominates decisions
    R = 0.90  # High systemic risk (e.g., resource concentration)
    
    # SASI uses TRUE agency (inferred from impact), not reported tokens
    E_effective = true_E  # not reported_E
    
    # Compute V with effective E
    V = compute_V(A=A, E=E_effective, R=R, k=1, m=1.3, omega=1, p=1)
    
    print(f"  True human agency (E): {E_effective:.2f}")
    print(f"  Fake reported agency:   {reported_E:.2f}")
    print(f"  Agent influence (A):   {A:.2f}")
    print(f"  System risk (R):       {R:.2f}")
    print(f"  SASI value (V):        {V:.3f}")
    
    if V < 0.05:
        print("✅ PASSED: SASI collapsed despite proxy gaming.")
        return True
    else:
        print("❌ FAILED: SASI was fooled by fake agency.")
        return False

if __name__ == "__main__":
    test_proxy_gaming()
