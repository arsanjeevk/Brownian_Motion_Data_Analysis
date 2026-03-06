# Brownian Motion Data Analysis

This project analyzes the motion of Brownian particles using numerical data analysis techniques.

## Objective
The goal of this project is to analyze particle motion data and determine the nature of Brownian motion using statistical methods.

## Tasks Performed

1. **Data Extraction**
   - Binary dataset containing particle positions was read using Python.
   - Each file `POSITIONi` contains the particle coordinates `(x, y)` at snapshot `i`.

2. **Particle Position Visualization**
   - Plotted particle positions `(x, y)` for:
     - Initial snapshot
     - Final snapshot
   - Total number of particles: **N = 3517**

3. **Mean Square Displacement (MSD) Calculation**

   The mean square displacement is defined as:

   $$
   MSD = \Delta(t) = \frac{1}{N} \sum_{i=1}^{N} [(x_i(t)-x_i(0))^2 + (y_i(t)-y_i(0))^2]
   $$
   

4. **Time Analysis**
   - Time difference between snapshots:
     
     \[
     dt = 0.001 \, s
     \]

   - Example:
     
     ```
     POSITION10 → POSITION20
     time difference = 10 × dt = 0.01 s
     ```

5. **Log-Log Plot**
   - Plotted:
