import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from random import uniform

def unicycle_spline(t0, tf, obs):
  # UNICYCLE_SPLINE returns a spline object representing a path from
  # (y(t0),z(t0)) = (0,0) to (y(t0),z(t0)) = (10,0) that avoids a circular
  # obstacle, such that d\dt y(t) > 0
  #   @param t0 - initial time
  #   @param tf - final time
  #
  #   @return y_spline - spline object for desired y trajectory
  #   @return z_spline - spline object for desired z trajectory
  y0 = 0;
  z0 = 0;

  yf = 10;
  zf = 0;

  y_max = 0
  z_max = 0

  # TODO: design the spline here  
  """ Params """

  dt = 1
  ti = 1

  clearance = 1

  t = np.linspace(0, int(tf), num=int(tf/dt))
  y = np.zeros(int(tf/dt))
  z = np.zeros(int(tf/dt))
  i = 1

  for ti in range(int(tf)-1):
    if i > 0:
        y[i] = y[i-1]
        z[i] = z[i-1]

    y_max = ti+dt
    y_min_s = obs.y - obs.radius - clearance*dt
    y_max_s = obs.y + obs.radius + clearance*dt
    z_min_s = obs.z - obs.radius - dt
    z_max_s = obs.z + obs.radius + dt

    if (y_max > y_min_s and y_max < y_max_s and z_max > z_min_s and z_max < z_max_s) :

        if (ti+dt) < ti:
            y_max = y_min_s
 
        if obs.z > 0:
            z_max = z[i] + z_min_s
            z[i] = z_max

        else:
            z_max = z[i] + z_max_s
            z[i] = z_max

    y[i] = y[i] + dt
    i=i+1

  z[-1],y[-1] = 0,10

  y_spline = CubicSpline(t, y);
  z_spline = CubicSpline(t, z);

  return y_spline, z_spline
