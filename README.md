# Vicsek Model Analysis: Complex Systems and Active Matter Simulation

A comprehensive analysis of collective behavior in active matter using the Vicsek model, investigating phase transitions from disordered to ordered motion through advanced time series analysis methods.

## Project Overview

This project explores the emergent collective behavior of self-propelled particles using the Vicsek model, a fundamental mathematical framework for understanding active matter systems. The study focuses on identifying phase transitions between disordered and nematic (ordered) states by analyzing the effects of noise amplitude and particle density on system dynamics.

## Scientific Background

The Vicsek model describes point-like self-propelled particles that:
- Move at constant velocity
- Align with neighboring particles within a given radius
- Experience directional noise during alignment

The system exhibits fascinating phase transitions:
- **Disordered phase**: Random particle motion at high noise/low density
- **Nematic phase**: Collective aligned motion at low noise/high density

## Key Features

- **Multi-scale Analysis**: Implementation of various time series analysis methods
- **Phase Transition Detection**: Identification of critical points using Binder cumulant
- **Comprehensive Visualization**: Dynamic probability density distributions and order parameter evolution
- **Parameter Space Exploration**: Systematic investigation of noise and density effects

## Analysis Methods Implemented

### 1. Multiscale Entropy (MSE) Analysis
- **Purpose**: Quantify complexity and irregularity of time series data
- **Findings**: 
  - Position data exhibits white noise characteristics (non-stationary with long-range dependencies)
  - Angular data shows 1/f noise behavior (stationary across time scales)

### 2. Detrended Fluctuation Analysis (DFA)
- **Purpose**: Detect long-range correlations and scaling properties
- **Key Results**:
  - Short-range (ln n < 2.5): Similar slopes (~0.5) across all conditions
  - Long-range (ln n > 2.5): Clear distinction between high/low density phases
  - High density systems show positive correlations (α > 0.5)
  - Low density systems exhibit uncorrelated behavior (α < 0.3)

### 3. Empirical Mode Decomposition (EMD)
- **Purpose**: Frequency domain analysis of particle dynamics
- **Insights**:
  - Low noise: Clear periodic functions with period T~2.5s
  - High noise: Multiple frequency components indicating random walks

### 4. Correlation Analysis
- **Order Parameter**: φ = (1/N)|Σᵢvᵢ|
  - φ = 0: Random motion
  - φ = 1: Perfect alignment
- **Results**: Exponential-like growth with density, plateauing at nematic order

### 5. Phase Transition Detection
- **Binder Cumulant**: G = 1 - ⟨φ⁴⟩/(3⟨φ²⟩²)
- **Critical Points Identified**:
  - Fixed noise (η = 2.0): Phase transition at density ρ ≈ 2.5
  - Variable density: Critical noise decreases with increasing particle number

## Technical Implementation

### Dependencies
```python
import numpy as np
import matplotlib.pyplot as plt
import scipy
# Additional libraries for MSE, DFA, EMD analysis
```

### Simulation Parameters
- **Box size (L)**: 10 units
- **Interaction radius (R)**: 0.5 units
- **Time step (dt)**: 0.1
- **Particle numbers**: 30, 300, 1000
- **Noise range**: 0.5 - 5.0
- **Velocity**: 1-4 units/time

### Key Equations

**Angular update**:
```
θᵢ(t + Δt) = ⟨θⱼ⟩ⱼ∈Nᵢ + ηᵢ(t)
```

**Position update**:
```
rᵢ(t + Δt) = rᵢ(t) + vΔt(cos θᵢ(t), sin θᵢ(t))
```

## Key Findings

1. **Phase Diagram**: Clear separation between ordered and disordered phases in noise-density parameter space
2. **Critical Scaling**: System size affects critical noise values (larger systems require less noise for transition)
3. **Temporal Dynamics**: Different phases exhibit distinct temporal correlation structures
4. **Universal Behavior**: Binder cumulant provides robust phase transition detection

## Applications

This analysis framework can be applied to:
- Biological systems (bacterial colonies, bird flocking, fish schooling)
- Robotic swarms
- Traffic flow modeling
- Social dynamics
- Active matter physics research

```

## Methodology

1. **Data Generation**: Python-based Vicsek model simulation
2. **Time Series Collection**: Particle positions and angles over time
3. **Statistical Analysis**: Multiple complementary analysis methods
4. **Phase Detection**: Binder cumulant and order parameter analysis
5. **Validation**: Comparison with established literature results

## References

- Vicsek, T. et al. (1995). Novel type of phase transition in a system of self-driven particles
- Simulation code adapted from: [Philip Mocz - Active Matter Python](https://github.com/pmocz/activematter-python)
- Nishiguchi, D. et al. (2017). Long-range nematic order and anomalous fluctuations in suspensions

## Academic Context

This project was completed as part of a Master's degree in Physics, focusing on complex systems and statistical mechanics. The work demonstrates proficiency in:
- Computational physics and numerical simulations
- Advanced time series analysis techniques  
- Statistical mechanics of active matter
- Scientific programming in Python
- Data visualization and interpretation
