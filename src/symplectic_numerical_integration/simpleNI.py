import numpy as np
import math as m


def dampening_torque(t):
    return 0.0

def equation_of_motion(t:float, T: list[float, float], *args, **kwargs)-> list[float]:
    r"""
    `t`: time parameter.
    --------------------------------------------------------
    `Y`: the conditions of the pendulum, [theta, thetaprime], 
    equivelently, this represents the current angle of the pendulum, 
    and the angular velocity of the pendulum at any given time.
    --------------------------------------------------------
    `return` time derivative of the condition vector described above,
    we have that in the form [angular velocity, angular acceleration]
    --------------------------------------------------------
    You may spesify, the following additional arguments:
    `c` dampening constant 
    `m` mass of pendulum part
    `g` strength of gravity
    `l` pendulum length
    --------------------------------------------------------
    The general equation of motion used here is as follows:
    mL^2\theta''(t)+ c\theta'(t)+mgL\sin(\theta) = \tau_{\text{ext}}(t)
    """
    if len(args) or len(kwargs) > 4:
        raise "Too many arguments, pendulum only takes c,m,g,l"
    c,m,g,l = args

    try:

        if len(kwargs) > 0:
            c = kwargs.fromkeys('c')
            m = kwargs.fromkeys("m")
            g = kwargs.fromkeys("g")
            l = kwargs.fromkeys("l")
    except:
        raise "Something went wrong, you most likely passed a variable that is not c,l,g or m"

    curAngle = T[0]
    angularVelocity = T[1]
    dCurAngle_dt = angularVelocity
    angularAcceleration = -c/(m*l^2)*dCurAngle_dt-(g/l)*m.sin(curAngle)+1/(m*l^2)*dampening_torque(t)
    return [dCurAngle_dt, angularAcceleration]



