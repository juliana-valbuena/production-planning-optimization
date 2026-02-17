# Production Planning Optimization

## Problem Description

A manufacturing company produces multiple products using limited labor and raw material resources. The objective is to determine the optimal production quantities that maximize total profit while satisfying resource constraints.

## Mathematical Formulation

### Decision Variables

x_i = number of units produced of product i

### Objective Function

Maximize total profit:

Max Z = Σ (profit_i * x_i)

### Constraints

1. Labor capacity constraint  
2. Raw material capacity constraint  
3. Non-negativity constraints  

x_i ≥ 0

## Implementation

The model is implemented in Python using the PuLP linear programming library.

## Repository Structure

- model.py → optimization model
- data.py → input data
- requirements.txt → required Python libraries

## Author

Juliana Valbuena  
Industrial Engineering | Machine Learning Minor
