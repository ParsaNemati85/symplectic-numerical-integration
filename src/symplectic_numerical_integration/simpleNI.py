import numpy as np
import math as ma

def dampening_torque(t):
    return 0.0

def equation_of_motion(t:float, T: list[float, float], **kwargs)-> list[float]:
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

    .. math::
    mL^2\theta''(t)+ c\theta'(t)+mgL\sin(\theta) = \tau_{\text{ext}}(t)
    """
    if len(kwargs) > 4:
        raise "Too many arguments, pendulum only takes c,m,g,l"

    try:
        if len(kwargs) > 0:
            c = kwargs['c']
            m = kwargs["m"]
            g = kwargs["g"]
            l = kwargs["l"]
    except:
        raise "Something went wrong, you most likely passed a variable that is not c,l,g or m"

    cur_angle = T[0]
    angular_velocity = T[1]
    d_cur_angle_dt = angular_velocity
    angular_acceleration = -(c)/(m*(l^2))*d_cur_angle_dt-(g/l)*ma.sin(cur_angle)+1/(m*(l^2))*dampening_torque(t)
    return [d_cur_angle_dt, angular_acceleration]




