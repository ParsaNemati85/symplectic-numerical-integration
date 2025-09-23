import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from symplectic_numerical_integration import simpleNI
#Ensure you run pip install -e . in the root dir for testing!

def test_zero_angle():
    r"""
    Unit Test for the zero angle, all results
    should be zero, intuitively, a pendulum 
    which is moved should never experience acceleration. 
    """
    result = simpleNI.equation_of_motion(0, [0.0, 0.0], c = 0, m = 1, l = 1, g = 9.8)
    assert np.allclose(result, [0,0])

def graph_simple_case(t_domain: list[float]) -> None:
    r"""
    Unit test/demo for a simple case of the diff eq
    solver in the case of a dampened pendulum.
    :param t_domain: `t_domain` is the bounds of the time domain, in
    the form [upper, lower] where `lower` is the lower
    bound of the function and `upper` is the upper bound.
    :param disc: `disc` is the number of discretizations
    is the domain, essentially, level of detail. Super high
    values may lead to horrific optimization issues.
    """
    def kwargs_wrapper(t, y):
        return simpleNI.equation_of_motion(t, y, c = 0.4, m = 2, l = 1, g = 9.8)

    eval_interval = np.linspace(*t_domain, 10000)

    sol = solve_ivp(kwargs_wrapper, t_domain, y0=[2, 0], t_eval=eval_interval, rtol=1e-8, atol=1e-10)

    plt.plot(sol.t, sol.y[0])
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title("Particular solution")
    plt.grid(True)
    plt.show()



test_zero_angle()
graph_simple_case([10.0, 0])
print("All tests passed")
