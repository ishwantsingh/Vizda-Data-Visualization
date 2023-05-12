import matplotlib.pyplot as plt
import numpy as np

from plotCurve import PlotCurve

class LineGraph(PlotCurve):


    def plot(self, x_arr, y_arr):
        
        plt.figure(figsize=(7,5))
        plt.plot(x_arr, y_arr, label="Numerical solution:\nRunge-Kutta", dashes=(3,2), color="blue", lw=3)
        # Compute dydt based on *current* state
        # dydt = self._model.rhs(t, y)

        # # Use dydt to get state at t + dt
        # ynew = y + (dydt * self._dt)
        plt.legend(loc="best", fontsize=12)
        plt.title(r"Solution to ODE: $\quad\frac{dy}{dx}=x^2$")
        plt.xlabel("x", fontsize=12)
        plt.ylabel("y", fontsize=12)
        plt.show()
        # return 

