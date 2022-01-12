import pp
import pyomo.environ as pyo

pp.pprint()

model = pyo.ConcreteModel()
model.x = pyo.Var([1,2,3], domain=pyo.NonNegativeIntegers)
model.objectiveFunction = pyo.Objective(expr = 30*model.x[1] + 20*model.x[2] + 50*model.x[3], sense = pyo.maximize)

model.constraint1 = pyo.Constraint(expr = 2*model.x[1] + 3*model.x[2] + 5*model.x[3] <= 4000)
model.constraint2 = pyo.Constraint(expr = 4*model.x[1] + 2*model.x[2] + 7*model.x[3] <= 6000)
model.constraint3 = pyo.Constraint(expr = model.x[1] >= 200)
model.constraint4 = pyo.Constraint(expr = model.x[2] >= 200)
model.constraint5 = pyo.Constraint(expr = model.x[3] >= 150)

# outputs a summary of the model
model.pprint()

# here we need to specify the solver's executable's name, and not just its name
solver = pyo.SolverFactory('ipopt', executable='ipopt.exe')
result = solver.solve(model)

# show results for the solved model
model.display()

input("Press enter to proceed...")