# Vicsek Model Simulation and Analysis

## Overview
This project investigates **collective motion in active matter** using the Vicsek model.  
The system consists of self-propelled particles that align with neighbors under varying noise and density.  
We explored how **phase transitions** emerge between disordered and ordered states.

## Key Features
- **Simulation:** Implemented Python code based on the Vicsek model to simulate active particle dynamics.  
- **Phase analysis:** Varied noise amplitude and particle density to study nematic order and flocking behavior.  
- **Data analysis:** Applied multiple techniques to characterize system dynamics:
  - **Multiscale Entropy (MSE):** quantified complexity and time-scale dependence.  
  - **Detrended Fluctuation Analysis (DFA):** identified long-range correlations.  
  - **Empirical Mode Decomposition (EMD):** separated frequency components of trajectories.  
  - **Correlation & Binder cumulant:** measured alignment and phase transition points.  

## Results
- At **low noise / high density**, the system forms collective aligned motion (nematic order).  
- At **high noise / low density**, the system behaves like a disordered gas.  
- Phase transition occurs around density $\rho \approx 2.5$ for noise $\eta = 2.0$.  
- Critical noise thresholds vary with system size (N = 30, 300, 1000).  

## Tools & Skills
- **Programming:** Python (NumPy, Matplotlib, SciPy)  
- **Time-series analysis:** entropy, fractal scaling, and spectral methods  
- **Complex system modeling:** active matter, phase transitions  
- **Data visualization & interpretation**  

## Files
- `report.pdf` – Full written report  
- `presentation.pdf` – Project presentation slides  
- `simulation_code/` – Python scripts for running and analyzing simulations  
