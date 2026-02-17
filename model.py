import pulp
from data import products, profit, labor_available, material_available, labor_required, material_required

# Create the optimization problem
model = pulp.LpProblem("Production_Planning", pulp.LpMaximize)

# Decision variables
x = pulp.LpVariable.dicts("Production", products, lowBound=0, cat='Continuous')

# Objective function
model += pulp.lpSum(profit[i] * x[i] for i in products), "Total_Profit"

# Labor constraint
model += pulp.lpSum(labor_required[i] * x[i] for i in products) <= labor_available, "Labor_Constraint"

# Material constraint
model += pulp.lpSum(material_required[i] * x[i] for i in products) <= material_available, "Material_Constraint"

# Solve the model
model.solve()

# Print results
print("Status:", pulp.LpStatus[model.status])
print("Optimal Production Plan:")

for i in products:
    print(f"Product {i}: {x[i].varValue}")

print("Total Profit:", pulp.value(model.objective))

