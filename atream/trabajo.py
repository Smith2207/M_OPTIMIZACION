import streamlit as st
from scipy.optimize import linprog

# Título de la aplicación
st.title("Resolución de Ejercicios de Programación Lineal y Entera")
st.write("Selecciona el ejercicio que deseas resolver y haz clic en el botón correspondiente para ver la solución.")

# Ejercicio 8.1 - Método de Branch and Bound
with st.expander("Ejercicio 8.1: Método de Branch and Bound"):
    st.subheader("Maximizar P(x1, x2, x3) = 4x1 + 3x2 + 3x3 sujeto a:")
    st.latex(r"""
    \begin{align*}
    4x_1 + 2x_2 + x_3 &\leq 10 \\
    3x_1 + 4x_2 + 2x_3 &\leq 14 \\
    2x_1 + x_2 + 3x_3 &\leq 7 \\
    x_1, x_2, x_3 &\geq 0, \text{ enteros}
    \end{align*}
    """)

    if st.button("Resolver Ejercicio 8.1"):
        c_8_1 = [-4, -3, -3]
        A_8_1 = [[4, 2, 1], [3, 4, 2], [2, 1, 3]]
        b_8_1 = [10, 14, 7]

        result_8_1 = linprog(c_8_1, A_ub=A_8_1, b_ub=b_8_1, bounds=(0, None), method="highs")
        st.write(f"Solución relajada: x1 = {result_8_1.x[0]:.2f}, x2 = {result_8_1.x[1]:.2f}, x3 = {result_8_1.x[2]:.2f}")
        st.write(f"Valor de la función objetivo: P = {-result_8_1.fun:.2f}")

# Ejercicio 8.2 - Resolución como un Problema de Programación Entera
with st.expander("Ejercicio 8.2: Programación Entera"):
    st.subheader("Maximizar P(x1, x2, x3) = 4x1 + 3x2 + 3x3 sujeto a:")
    st.latex(r"""
    \begin{align*}
    4x_1 + 2x_2 + x_3 &\leq 10 \\
    3x_1 + 4x_2 + 2x_3 &\leq 14 \\
    2x_1 + x_2 + 3x_3 &\leq 7 \\
    x_1, x_2, x_3 &\geq 0, \text{ enteros}
    \end{align*}
    """)

    if st.button("Resolver Ejercicio 8.2"):
        c_8_2 = [-4, -3, -3]
        A_8_2 = [[4, 2, 1], [3, 4, 2], [2, 1, 3]]
        b_8_2 = [10, 14, 7]

        result_8_2 = linprog(c_8_2, A_ub=A_8_2, b_ub=b_8_2, bounds=(0, None), method="highs")
        st.write(f"Solución del problema: x1 = {result_8_2.x[0]:.2f}, x2 = {result_8_2.x[1]:.2f}, x3 = {result_8_2.x[2]:.2f}")
        st.write(f"Valor de la función objetivo: P = {-result_8_2.fun:.2f}")

# Ejercicio 8.3 - Método de Cortes de Gomory
with st.expander("Ejercicio 8.3: Método de Cortes de Gomory"):
    st.subheader("Minimizar C(x, y) = x - y sujeto a:")
    st.latex(r"""
    \begin{align*}
    3x + 4y &\leq 6 \\
    x - y &\leq 1 \\
    x, y &\geq 0, \text{ enteros}
    \end{align*}
    """)

    if st.button("Resolver Ejercicio 8.3"):
        c_8_3 = [1, -1]
        A_8_3 = [[3, 4], [1, -1]]
        b_8_3 = [6, 1]

        result_8_3 = linprog(c_8_3, A_ub=A_8_3, b_ub=b_8_3, bounds=(0, None), method="highs")
        st.write(f"Solución relajada: x = {result_8_3.x[0]:.2f}, y = {result_8_3.x[1]:.2f}")
        st.write(f"Valor de la función objetivo: C = {result_8_3.fun:.2f}")

# Ejercicio 8.4 - Método de Cortes de Gomory
with st.expander("Ejercicio 8.4: Método de Cortes de Gomory"):
    st.subheader("Maximizar P(x1, x2, x3) = 4x1 + 3x2 + 3x3 sujeto a:")
    st.latex(r"""
    \begin{align*}
    4x_1 + 2x_2 + x_3 &\leq 10 \\
    3x_1 + 4x_2 + 2x_3 &\leq 14 \\
    2x_1 + x_2 + 3x_3 &\leq 7 \\
    x_1, x_2, x_3 &\geq 0, \text{ enteros}
    \end{align*}
    """)

    if st.button("Resolver Ejercicio 8.4"):
        c_8_4 = [-4, -3, -3]
        A_8_4 = [[4, 2, 1], [3, 4, 2], [2, 1, 3]]
        b_8_4 = [10, 14, 7]

        result_8_4 = linprog(c_8_4, A_ub=A_8_4, b_ub=b_8_4, bounds=(0, None), method="highs")
        st.write(f"Solución relajada: x1 = {result_8_4.x[0]:.2f}, x2 = {result_8_4.x[1]:.2f}, x3 = {result_8_4.x[2]:.2f}")
        st.write(f"Valor de la función objetivo: P = {-result_8_4.fun:.2f}")

# Ejercicio 8.5 - Selección de Proyectos de I+D
with st.expander("Ejercicio 8.5: Selección de Proyectos de I+D"):
    st.subheader("Maximizar el NPV sujeto a restricciones de presupuesto anual.")

    if st.button("Resolver Ejercicio 8.5"):
        npv_coefficients = [-141, -187, -121, -85, -262, -127]
        capital_requirements = [
            [75, 90, 60, 85, 100, 50],
            [25, 35, 15, 25, 30, 20],
            [20, 0, 15, 0, 20, 10],
            [15, 50, 15, 0, 20, 30],
            [10, 30, 15, 0, 20, 40]
        ]
        budgets = [250, 75, 50, 50, 50]

        result_8_5 = linprog(npv_coefficients, A_ub=capital_requirements, b_ub=budgets, bounds=(0, 1), method="highs")
        st.write("Proyectos seleccionados:")
        for i, selected in enumerate(result_8_5.x, start=1):
            st.write(f"Proyecto {i}: {'Seleccionado' if selected >= 0.5 else 'No seleccionado'}")
        st.write(f"Valor total de NPV: { -result_8_5.fun:.2f}")
