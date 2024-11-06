import streamlit as st
from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD

# Configuración de la aplicación
st.title("Ejercicios de Optimización en Investigación de Operaciones")

# Selección de ejercicio
exercise = st.sidebar.selectbox(
    "Selecciona el ejercicio para resolver",
    [
        "Ejercicio 8.1 (Branch and Bound)", 
        "Ejercicio 8.2 (LP y IP)", 
        "Ejercicio 8.3 (Cut-Planes)", 
        "Ejercicio 8.4 (Gomory Cut-Planes)", 
        "Ejercicio 8.5 (Selección de Proyectos con Programación Entera Binaria)"
    ]
)

# Función para mostrar los resultados
def mostrar_resultados(prob, variables):
    result = prob.solve(PULP_CBC_CMD(msg=False))
    st.subheader("Resultados")
    if result == 1:
        st.write("Valor óptimo de la función objetivo (Z):", prob.objective.value())
        for var in variables:
            st.write(f"{var.name} = {var.value()}")
    else:
        st.error("No se encontró una solución óptima.")

# Ejercicio 8.1 - Branch and Bound
if exercise == "Ejercicio 8.1 (Branch and Bound)":
    st.header("Ejercicio 8.1 - Branch and Bound")
    prob = LpProblem("Ejercicio_8_1", LpMaximize)
    
    # Variables
    x1 = LpVariable("x1", lowBound=0, cat="Integer")
    x2 = LpVariable("x2", lowBound=0, cat="Integer")
    x3 = LpVariable("x3", lowBound=0, cat="Integer")
    
    # Función objetivo
    prob += 4 * x1 + 3 * x2 + 1 * x3, "Z"
    
    # Restricciones
    prob += 4 * x1 + 2 * x2 + x3 <= 10, "Restriccion_1"
    prob += 3 * x1 + 4 * x2 + 2 * x3 <= 14, "Restriccion_2"
    prob += 2 * x1 + x2 + 3 * x3 <= 7, "Restriccion_3"
    
    # Mostrar resultados
    mostrar_resultados(prob, [x1, x2, x3])

# Ejercicio 8.2 - Resolución LP y IP
elif exercise == "Ejercicio 8.2 (LP y IP)":
    st.header("Ejercicio 8.2 - Resolución LP y IP")
    prob = LpProblem("Ejercicio_8_2", LpMaximize)
    
    # Variables
    x1 = LpVariable("x1", lowBound=0)
    x2 = LpVariable("x2", lowBound=0)
    x3 = LpVariable("x3", lowBound=0)
    
    # Función objetivo
    prob += 4 * x1 + 3 * x2 + 1 * x3, "Z"
    
    # Restricciones
    prob += 4 * x1 + 2 * x2 + x3 <= 10, "Restriccion_1"
    prob += 3 * x1 + 4 * x2 + 2 * x3 <= 14, "Restriccion_2"
    prob += 2 * x1 + x2 + 3 * x3 <= 7, "Restriccion_3"
    
    # Resolución como LP
    st.subheader("Resolución como Problema Lineal (LP)")
    mostrar_resultados(prob, [x1, x2, x3])
    
    # Resolución como IP
    st.subheader("Resolución como Problema Entero (IP)")
    x1.cat = "Integer"
    x2.cat = "Integer"
    x3.cat = "Integer"
    mostrar_resultados(prob, [x1, x2, x3])

# Ejercicio 8.3 - Cut-Planes
elif exercise == "Ejercicio 8.3 (Cut-Planes)":
    st.header("Ejercicio 8.3 - Cut-Planes")
    prob = LpProblem("Ejercicio_8_3", LpMinimize)
    
    # Variables
    x = LpVariable("x", lowBound=0, cat="Integer")
    y = LpVariable("y", lowBound=0, cat="Integer")
    
    # Función objetivo
    prob += x - y, "C"
    
    # Restricciones
    prob += 3 * x + 4 * y <= 6, "Restriccion_1"
    prob += x - y <= 1, "Restriccion_2"
    
    # Mostrar resultados
    mostrar_resultados(prob, [x, y])
    st.info("Para implementar el método de corte iterativo Cut-Planes, se debe añadir un ciclo de cortes de Gomory, creando restricciones adicionales en cada iteración hasta encontrar una solución entera.")

# Ejercicio 8.4 - Gomory Cut-Planes
elif exercise == "Ejercicio 8.4 (Gomory Cut-Planes)":
    st.header("Ejercicio 8.4 - Gomory Cut-Planes")
    prob = LpProblem("Ejercicio_8_4", LpMaximize)
    
    # Variables
    x1 = LpVariable("x1", lowBound=0, cat="Integer")
    x2 = LpVariable("x2", lowBound=0, cat="Integer")
    x3 = LpVariable("x3", lowBound=0, cat="Integer")
    
    # Función objetivo
    prob += 4 * x1 + 3 * x2 + 1 * x3, "Z"
    
    # Restricciones
    prob += 4 * x1 + 2 * x2 + x3 <= 10, "Restriccion_1"
    prob += 3 * x1 + 4 * x2 + 2 * x3 <= 14, "Restriccion_2"
    prob += 2 * x1 + x2 + 3 * x3 <= 7, "Restriccion_3"
    
    # Mostrar resultados iniciales
    mostrar_resultados(prob, [x1, x2, x3])
    st.info("Para aplicar el método de cortes de Gomory, sería necesario agregar una serie de cortes iterativos hasta que todas las variables sean enteras.")

# Ejercicio 8.5 - Selección de Proyectos con Programación Entera Binaria
elif exercise == "Ejercicio 8.5 (Selección de Proyectos con Programación Entera Binaria)":
    st.header("Ejercicio 8.5 - Selección de Proyectos con Programación Entera Binaria")
    prob = LpProblem("Ejercicio_8_5", LpMaximize)
    
    # Datos de NPV y costos por año
    npv = [141, 187, 121, 83, 262, 127]
    year1_costs = [75, 90, 60, 30, 100, 50]
    year2_costs = [25, 25, 15, 10, 25, 20]
    year3_costs = [20, 30, 15, 5, 20, 20]
    year4_costs = [15, 10, 15, 5, 20, 10]
    year5_costs = [10, 5, 5, 5, 10, 5]
    budget_year1 = 75
    budget_year2_5 = 250
    
    # Variables binarias
    x = [LpVariable(f"x{i}", cat="Binary") for i in range(6)]
    
    # Función objetivo
    prob += lpSum(npv[i] * x[i] for i in range(6)), "Total_NPV"
    
    # Restricciones de presupuesto
    prob += lpSum(year1_costs[i] * x[i] for i in range(6)) <= budget_year1, "Budget_Year_1"
    prob += lpSum(year2_costs[i] * x[i] for i in range(6)) <= budget_year2_5, "Budget_Year_2"
    prob += lpSum(year3_costs[i] * x[i] for i in range(6)) <= budget_year2_5, "Budget_Year_3"
    prob += lpSum(year4_costs[i] * x[i] for i in range(6)) <= budget_year2_5, "Budget_Year_4"
    prob += lpSum(year5_costs[i] * x[i] for i in range(6)) <= budget_year2_5, "Budget_Year_5"
    
    # Mostrar resultados
    result = prob.solve(PULP_CBC_CMD(msg=False))
    st.subheader("Resultados")
    if result == 1:
        st.write("Valor óptimo de la función objetivo (NPV total):", prob.objective.value())
        st.write("Proyectos seleccionados:")
        for i in range(6):
            st.write(f"Proyecto {i + 1}: {'Seleccionado' if x[i].value() == 1 else 'No seleccionado'}")
    else:
        st.error("No se encontró una solución óptima.")
