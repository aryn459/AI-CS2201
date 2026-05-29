from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ("Weather", "Satisfaction"),
    ("Budget", "Satisfaction"),
    ("Crowd", "Satisfaction")
])

cpd_weather = TabularCPD(
    variable="Weather",
    variable_card=2,
    values=[[0.7], [0.3]]
)

cpd_budget = TabularCPD(
    variable="Budget",
    variable_card=2,
    values=[[0.6], [0.4]]
)

cpd_crowd = TabularCPD(
    variable="Crowd",
    variable_card=2,
    values=[[0.5], [0.5]]
)

cpd_satisfaction = TabularCPD(
    variable="Satisfaction",
    variable_card=2,
    values=[
        [0.95, 0.85, 0.80, 0.60, 0.70, 0.50, 0.40, 0.20],
        [0.05, 0.15, 0.20, 0.40, 0.30, 0.50, 0.60, 0.80]
    ],
    evidence=["Weather", "Budget", "Crowd"],
    evidence_card=[2, 2, 2]
)

model.add_cpds(
    cpd_weather,
    cpd_budget,
    cpd_crowd,
    cpd_satisfaction
)

print("Model Valid:", model.check_model())

inference = VariableElimination(model)

result = inference.query(
    variables=["Satisfaction"],
    evidence={
        "Weather": 0,
        "Budget": 0,
        "Crowd": 0
    }
)

print(result)