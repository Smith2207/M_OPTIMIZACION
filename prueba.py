import streamlit as st
import pulp
import graphviz
import time
from typing import Tuple, Dict
import pandas as pd

def resolver_optimizacion(tipo_problema: str = 'Entero', tolerancia: float = 0.1) -> Tuple[pulp.LpProblem, Dict, float]:
    # Registrar tiempo inicial
    tiempo_inicio = time.time()
    
    # Crear el modelo
    prob = pulp.LpProblem("Ejercicio_8_1_2", pulp.LpMaximize)
    
    # Definir variables según el tipo de problema
    if tipo_problema == 'Entero':
        x1 = pulp.LpVariable("x1", lowBound=0, cat='Integer')
        x2 = pulp.LpVariable("x2", lowBound=0, cat='Integer')
        x3 = pulp.LpVariable("x3", lowBound=0, cat='Integer')
    else:  # Relajación LP
        x1 = pulp.LpVariable("x1", lowBound=0)
        x2 = pulp.LpVariable("x2", lowBound=0)
        x3 = pulp.LpVariable("x3", lowBound=0)
    
    # Definir función objetivo
    prob += 4*x1 + 3*x2 + 3*x3
    
    # Definir restricciones
    prob += 4*x1 + 2*x2 + x3 <= 10, "Restricción 1"
    prob += 3*x1 + 4*x2 + 2*x3 <= 14, "Restricción 2"
    prob += x1 + 3*x2 + 3*x3 <= 7, "Restricción 3"
    
    # Configurar tolerancia del solver si se especifica
    if tolerancia != 0.1:
        prob.solver = pulp.PULP_CBC_CMD(mip_rel_gap=tolerancia/100)
    
    # Resolver el problema
    prob.solve()
    
    # Calcular tiempo de solución
    tiempo_solucion = time.time() - tiempo_inicio
    
    # Recopilar resultados
    resultados = {
        'x1': pulp.value(x1),
        'x2': pulp.value(x2),
        'x3': pulp.value(x3),
        'objetivo': pulp.value(prob.objective),
        'estado': pulp.LpStatus[prob.status]
    }
    
    return prob, resultados, tiempo_solucion

def crear_arbol_decision():
    dot = graphviz.Digraph()
    dot.attr(rankdir='TB')
    
    # Agregar nodos
    dot.node('A', 'Raíz\nRamificación en x₁')
    dot.node('B', 'x₁ ≤ 2')
    dot.node('C', 'x₁ > 2')
    dot.node('D', 'Ramificación en x₂')
    dot.node('E', 'No Factible')
    dot.node('F', 'Solución Encontrada\nx₁=2, x₂=1, x₃=0')
    
    # Agregar conexiones
    dot.edge('A', 'B', 'rama izquierda')
    dot.edge('A', 'C', 'rama derecha')
    dot.edge('B', 'D')
    dot.edge('C', 'E')
    dot.edge('D', 'F')
    
    return dot

def main():
    st.title("Ejercicios 8.1 y 8.2 - Solucionador| PLM")
    
    st.markdown("""
    ### Formulación del Problema:
    Maximizar P(x₁, x₂, x₃) = 4x₁ + 3x₂ + 3x₃
    
    Sujeto a:
    - 4x₁ + 2x₂ + x₃ ≤ 10
    - 3x₁ + 4x₂ + 2x₃ ≤ 14
    - x₁ + 3x₂ + 3x₃ ≤ 7
    
    Donde x₁, x₂, x₃ son enteros no negativos
    """)
    
    st.header("Ejercicio 8.1 - Programación Lineal Entera")
    if st.button("Resolver PLM"):
        prob, resultados, tiempo_plm = resolver_optimizacion('Entero')
        
        st.write("### Resultados:")
        st.write(f"Estado: {resultados['estado']}")
        st.write(f"x₁ = {resultados['x1']:.4f}")
        st.write(f"x₂ = {resultados['x2']:.4f}")
        st.write(f"x₃ = {resultados['x3']:.4f}")
        st.write(f"Valor Objetivo = {resultados['objetivo']:.4f}")
        st.write(f"Tiempo de Solución: {tiempo_plm:.4f} segundos")
        
        st.write("### Árbol de Decisión")
        dot = crear_arbol_decision()
        st.graphviz_chart(dot)
    
    st.header("Ejercicio 8.2 - Análisis Comparativo")
    
    if st.button("Ejecutar Análisis Comparativo"):
        # Lista para almacenar resultados
        lista_resultados = []
        
        # 1. Resolver como relajación LP
        _, resultados_lp, tiempo_lp = resolver_optimizacion('LP')
        lista_resultados.append({
            'Tipo': 'Relajación LP',
            'Tiempo': tiempo_lp,
            'Objetivo': resultados_lp['objetivo'],
            'x₁': resultados_lp['x1'],
            'x₂': resultados_lp['x2'],
            'x₃': resultados_lp['x3']
        })
        
        # 2. Resolver como PLM con tolerancia predeterminada
        _, resultados_plm, tiempo_plm = resolver_optimizacion('Entero')
        lista_resultados.append({
            'Tipo': 'PLM (tolerancia 0.1%)',
            'Tiempo': tiempo_plm,
            'Objetivo': resultados_plm['objetivo'],
            'x₁': resultados_plm['x1'],
            'x₂': resultados_plm['x2'],
            'x₃': resultados_plm['x3']
        })
        
        # 3. Resolver como PLM con tolerancia más ajustada
        _, resultados_ajustados, tiempo_ajustado = resolver_optimizacion('Entero', tolerancia=0.01)
        lista_resultados.append({
            'Tipo': 'PLM (tolerancia 0.01%)',
            'Tiempo': tiempo_ajustado,
            'Objetivo': resultados_ajustados['objetivo'],
            'x₁': resultados_ajustados['x1'],
            'x₂': resultados_ajustados['x2'],
            'x₃': resultados_ajustados['x3']
        })
        
        # Crear tabla comparativa
        df = pd.DataFrame(lista_resultados)
        st.write("### Resultados Comparativos:")
        st.dataframe(df)
        
        # Análisis
        st.write("### Análisis:")
        st.write("""
        1. Relajación LP vs Solución Entera:
           - La relajación LP proporciona una cota superior de la solución entera óptima
           - Típicamente se resuelve más rápido pero puede dar valores no enteros
           
        2. Impacto de la Tolerancia:
           - Una tolerancia más ajustada (0.01%) puede aumentar el tiempo de solución
           - Puede proporcionar soluciones ligeramente diferentes en algunos casos
           
        3. Comparación de Tiempos Computacionales:
           - La relajación LP es típicamente la más rápida
           - Una tolerancia más ajustada generalmente aumenta el tiempo de solución
        """)

if __name__ == "__main__":
    main()