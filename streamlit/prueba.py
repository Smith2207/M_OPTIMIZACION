import streamlit as st
from scipy.optimize import linprog

st.title("Resolución de Ejercicios de Programación Lineal y Entera con Streamlit")

# --- Ejercicio 8.1 ---
st.header("Ejercicio 8.1: Método de Branch and Bound")
st.write("Maximizar P(x1, x2, x3) = 4x1 + 3x2 + 3x3 sujeto a las restricciones:")
st.latex(r"""
\begin{align*}
4x_1 + 2x_2 + x_3 &\leq 10 \\
3x_1 + 4x_2 + 2x_3 &\leq 14 \\
2x_1 + x_2 + 3x_3 &\leq 7 \\
x_1, x_2, x_3 &\geq 0, \text{ enteros}
\end{align*}
""")

if st.button("Resolver Ejercicio 8.1"):
    # Coeficientes de la función objetivo (Maximización)
    c_8_1 = [-4, -3, -3]

    # Coeficientes de las restricciones
    A_8_1 = [
        [4, 2, 1],
        [3, 4, 2],
        [2, 1, 3]
    ]
    b_8_1 = [10, 14, 7]

    # Resolver la versión relajada del problema
    result_8_1 = linprog(c_8_1, A_ub=A_8_1, b_ub=b_8_1, bounds=(0, None), method="highs")
    x_relaxed = result_8_1.x
    P_relaxed = -result_8_1.fun

    st.write("Solución relajada:")
    st.write(f"x1 = {x_relaxed[0]:.2f}, x2 = {x_relaxed[1]:.2f}, x3 = {x_relaxed[2]:.2f}")
    st.write(f"Valor de la función objetivo: P = {P_relaxed:.2f}")

# --- Ejercicio 8.2 ---
st.header("Ejercicio 8.2: Resolución como un Problema de Programación Entera")
st.write("Maximizar P(x1, x2, x3) = 4x1 + 3x2 + 3x3 sujeto a las restricciones:")
st.latex(r"""
\begin{align*}
4x_1 + 2x_2 + x_3 &\leq 10 \\
3x_1 + 4x_2 + 2x_3 &\leq 14 \\
2x_1 + x_2 + 3x_3 &\leq 7 \\
x_1, x_2, x_3 &\geq 0, \text{ enteros}
\end{align*}
""")

if st.button("Resolver Ejercicio 8.2"):
    # Coeficientes de la función objetivo (Maximización)
    c_8_2 = [-4, -3, -3]  # Definir c_8_2 de nuevo para el ejercicio 8.2

    # Coeficientes de las restricciones
    A_8_2 = [
        [4, 2, 1],
        [3, 4, 2],
        [2, 1, 3]
    ]
    b_8_2 = [10, 14, 7]

    # Resolver la versión relajada del problema como programación entera
    result_8_2 = linprog(c_8_2, A_ub=A_8_2, b_ub=b_8_2, bounds=(0, None), method="highs")
    x_int = result_8_2.x
    P_int = -result_8_2.fun

    st.write("Solución del problema de programación entera (relajado):")
    st.write(f"x1 = {x_int[0]:.2f}, x2 = {x_int[1]:.2f}, x3 = {x_int[2]:.2f}")
    st.write(f"Valor de la función objetivo: P = {P_int:.2f}")

# --- Ejercicio 8.3 ---
st.header("Ejercicio 8.3: Método de Cortes de Gomory")
st.write("Minimizar C(x, y) = x - y sujeto a las restricciones:")
st.latex(r"""
\begin{align*}
3x + 4y &\leq 6 \\
x - y &\leq 1 \\
x, y &\geq 0, \text{ enteros}
\end{align*}
""")

if st.button("Resolver Ejercicio 8.3"):
    # Coeficientes de la función objetivo para el ejercicio 8.3 (Minimización)
    c_8_3 = [1, -1]

    # Coeficientes de las restricciones
    A_8_3 = [
        [3, 4],
        [1, -1]
    ]
    b_8_3 = [6, 1]

    # Resolver la versión relajada del problema
    result_8_3 = linprog(c_8_3, A_ub=A_8_3, b_ub=b_8_3, bounds=(0, None), method="highs")
    x_relaxed_8_3 = result_8_3.x
    C_relaxed_8_3 = result_8_3.fun

    st.write("Solución relajada:")
    st.write(f"x = {x_relaxed_8_3[0]:.2f}, y = {x_relaxed_8_3[1]:.2f}")
    st.write(f"Valor de la función objetivo: C = {C_relaxed_8_3:.2f}")

# --- Ejercicio 8.4 ---
st.header("Ejercicio 8.4: Método de Cortes de Gomory")
st.write("Maximizar P(x1, x2, x3) = 4x1 + 3x2 + 3x3 sujeto a las restricciones:")
st.latex(r"""
\begin{align*}
4x_1 + 2x_2 + x_3 &\leq 10 \\
3x_1 + 4x_2 + 2x_3 &\leq 14 \\
2x_1 + x_2 + 3x_3 &\leq 7 \\
x_1, x_2, x_3 &\geq 0, \text{ enteros}
\end{align*}
""")

if st.button("Resolver Ejercicio 8.4"):
    # Coeficientes de la función objetivo
    c_8_4 = [-4, -3, -3]
    A_8_4 = [
        [4, 2, 1],
        [3, 4, 2],
        [2, 1, 3]
    ]
    b_8_4 = [10, 14, 7]

    # Resolver la versión relajada
    result_8_4 = linprog(c_8_4, A_ub=A_8_4, b_ub=b_8_4, bounds=(0, None), method="highs")
    st.write("Solución relajada del ejercicio 8.4:")
    st.write(f"x1 = {result_8_4.x[0]:.2f}, x2 = {result_8_4.x[1]:.2f}, x3 = {result_8_4.x[2]:.2f}")
    st.write(f"Valor de la función objetivo: P = {-result_8_4.fun:.2f}")

# --- Ejercicio 8.5 ---
st.header("Ejercicio 8.5: Selección de Proyectos de I+D")
st.write("Maximizar el NPV sujeto a las restricciones de presupuesto para cada año.")

if st.button("Resolver Ejercicio 8.5"):
    # Coeficientes de la función objetivo (NPV de cada proyecto)
    npv_coefficients = [-141, -187, -121, -85, -262, -127]
    capital_requirements = [
        [75, 90, 60, 85, 100, 50],
        [25, 35, 15, 25, 30, 20],
        [20, 0, 15, 0, 20, 10],
        [15, 50, 15, 0, 20, 30],
        [10, 30, 15, 0, 20, 40]
    ]
    budgets = [250, 75, 50, 50, 50]

    # Resolver el problema de selección de proyectos
    result_8_5 = linprog(npv_coefficients, A_ub=capital_requirements, b_ub=budgets, bounds=(0, 1), method="highs")
    selected_projects = result_8_5.x
    total_npv = -result_8_5.fun

    st.write("Proyectos seleccionados:")
    for i, selected in enumerate(selected_projects, start=1):
        st.write(f"Proyecto {i}: {'Seleccionado' if selected >= 0.5 else 'No seleccionado'}")

    st.write(f"*Valor total de NPV:* {total_npv:.2f}")