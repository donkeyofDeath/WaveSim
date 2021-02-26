# Wave equation simulator

The Python code in this repository solves a 1D wave equation on a grid. 
In the future it will be updated for 2D wave equations. The topics which
will be discussed are:

- Discritization of the wave equation
- Choosing and implementation of a boundary condition
- Implementation of initial conditions
- Stability analysis
- Results
- Benchmark


## Discretizing the wave equation

The Wave equation in 1D reads
<br>
<br>
<p align="center">
<img src=/images/wave_equation.jpg>
</p>
In the next step, this partial differential equation is discretized by using a
finite difference method
<br>
<br>
<p align="center">
<img src=/images/second_derivative_approx.jpg>
</p>
The above equation is a central finite difference. Using this expression 
simplifies the wave equation to
<br>
<br>
<p align="center">
<img src=/images/discrete_wave_equation.jpg>
</p>
Now this does not look particularly simple. But setting fully discretizing 
space and time results in the following equation for updating the equation
from one time step to another
<br>
<br>
<p align="center">
<img src=/images/time_step_equation.jpg>
</p>
The above equation is visualized in the image below, where the amplitude
of the i-th point at the (j+1)-th time step is given the point at the time
step and its neighbors. Further it relies on the state of the amplitudes at
the (j-1)-ths time step.
<p align="center"> 
<img src=/images/time_step_visualization.png>
</p>
The state of N amplitudes at time step j can be imagined as a vector
<br>
<br>
<p align="center">
<img src=/images/time_step_vector.jpg>
</p>
This transforms the update equation to a linear equation involving an
update matrix T, the j-th state and the (j-1)-th state
<br>
<br>
<p align="center">
<img src=time_step_linear_equation.jpg>
</p>
The frame of zeros in the matrix T correspond to the boundary condition
which were already quitely implemented without mentioning. The disussion
regarding the boundary condition will follow now.

## Boundary condition

The 
