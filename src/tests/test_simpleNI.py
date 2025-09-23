import numpy as np
import matplotlib.pyplot as plt
import time
from symplectic_numerical_integration import simpleNI

def test_zero_angle():
    r"""
    Unit Test for the zero angle, all results
    should be zero, intuitively, a pendulum 
    which is moved should never experience acceleration. 
    """
    result = simpleNI.equation_of_motion(0, [0.0, 0.0], c = 0, m = 1, l = 1, g = 9.8)
    assert np.allclose(result, [0,0])

test_zero_angle()
print("All tests passed")
