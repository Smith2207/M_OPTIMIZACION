import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Set page config
st.set_page_config(
    page_title="Análisis de Convexidad - Paso a Paso",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for neon effects
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to right, #000428, #004e92);
        color: white !important;
    }
    .header {
        text-align: center;
        color: #0ff;
        text-shadow: 0 0 10px #0ff;
        padding: 20px;
        font-size: 3em;
        animation: glow 1.5s ease-in-out infinite alternate;
    }
    .subheader {
        color: #ff00ff;
        text-shadow: 0 0 5px #ff00ff;
        margin-bottom: 20px;
    }
    .step-box {
        background: rgba(0,255,255,0.1);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #0ff;
        margin-bottom: 20px;
    }
    @keyframes glow {
        from {text-shadow: 0 0 5px #0ff, 0 0 10px #0ff;}
        to {text-shadow: 0 0 10px #0ff, 0 0 20px #0ff;}
    }
    .formula {
        color: #0ff;
        font-family: monospace;
        font-size: 1.2em;
        margin: 10px 0;
    }
    .conclusion {
        color: #ff00ff;
        font-weight: bold;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="header">Análisis de Convexidad - Resolución Paso a Paso</h1>', unsafe_allow_html=True)

# Exercise selection
exercises = {
    "Ejercicio 1": "f(x) = 3x + 2",
    "Ejercicio 2": "f(x) = x³",
    "Ejercicio 3": "f(x) = e²ˣ",
    "Ejercicio 4": "f(x) = ln(x)",
    "Ejercicio 5": "f(x) = x⁴ - 2x² + 1"
}

selected_exercise = st.sidebar.selectbox("Selecciona un ejercicio:", list(exercises.keys()))

def show_exercise_1():
    st.markdown('<h2 class="subheader">Demostrar que f(x) = 3x + 2 es convexa en R</h2>', unsafe_allow_html=True)

    steps = {
        "Paso 1 - Primera Derivada": {"explanation": "Calculamos la primera derivada de f(x) = 3x + 2", "formula": "f'(x) = d/dx(3x + 2) = 3"},
        "Paso 2 - Segunda Derivada": {"explanation": "Calculamos la segunda derivada", "formula": "f''(x) = d/dx(3) = 0"},
        "Paso 3 - Análisis": {"explanation": "Como la segunda derivada es constante y no negativa, la función es convexa."},
        "Conclusión": {"explanation": "La función \( f(x) = 3x + 2 \) es convexa en todo \( R \)."}
    }

    current_step = st.radio("Selecciona el paso a visualizar:", list(steps.keys()))

    with st.container():
        st.markdown(f'<div class="step-box">', unsafe_allow_html=True)
        st.markdown(f"### {current_step}")
        st.write(steps[current_step]["explanation"])
        if "formula" in steps[current_step]:
            st.markdown(f'<div class="formula">{steps[current_step]["formula"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Plot for current step
        x = np.linspace(-5, 5, 100)
        y = 3 * x + 2

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='f(x) = 3x + 2',
                                line=dict(color='#00ffff', width=3)))

        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#ffffff'),
            title=dict(text='Gráfica de f(x) = 3x + 2', font=dict(size=20, color='#00ffff')),
            xaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff')
        )

        st.plotly_chart(fig)

    # Interactive section
    st.markdown("### **Prueba con tus propios datos**")
    coef = st.number_input("Ingresa el coeficiente de x (default: 3):", value=3.0)
    intercept = st.number_input("Ingresa el término independiente (default: 2):", value=2.0)

    y_user = coef * x + intercept
    fig_user = go.Figure()
    fig_user.add_trace(go.Scatter(x=x, y=y_user, mode='lines', name=f'f(x) = {coef}x + {intercept}',
                                  line=dict(color='#ff00ff', width=3)))
    fig_user.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#ffffff'),
        title=dict(text=f'Gráfica de f(x) = {coef}x + {intercept}', font=dict(size=20, color='#ff00ff')),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff')
    )
    st.plotly_chart(fig_user)

    # Conclusion with if
    st.markdown("### **Conclusión para tus parámetros**")
    if coef == 0:
        st.markdown(f"Con \( c = {coef} \), la función es una constante y no es ni convexa ni cóncava.")
    else:
        st.markdown(f"Con \( c = {coef} \), la función sigue siendo lineal y convexa en todo \( R \).")



def show_exercise_2():
    st.markdown('<h2 class="subheader">Verificar si f(x) = x³ es convexa, cóncava o ninguna en [0, ∞)</h2>', unsafe_allow_html=True)

    steps = {
        "Paso 1 - Primera Derivada": {"explanation": "Calculamos la primera derivada de f(x) = x³", "formula": "f'(x) = 3x²"},
        "Paso 2 - Segunda Derivada": {"explanation": "Calculamos la segunda derivada", "formula": "f''(x) = 6x"},
        "Paso 3 - Análisis": {"explanation": "En [0, ∞): f''(x) > 0 para x > 0, f''(0) = 0, indicando que es convexa para x > 0."},
        "Conclusión": {"explanation": "La función es convexa para \( x > 0 \) y no es ni convexa ni cóncava en \( x = 0 \)."}
    }

    current_step = st.radio("Selecciona el paso a visualizar:", list(steps.keys()))

    with st.container():
        st.markdown(f'<div class="step-box">', unsafe_allow_html=True)
        st.markdown(f"### {current_step}")
        st.write(steps[current_step]["explanation"])
        if "formula" in steps[current_step]:
            st.markdown(f'<div class="formula">{steps[current_step]["formula"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Plot for current step
        x = np.linspace(0, 2, 100)
        y = x**3

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='f(x) = x³',
                                line=dict(color='#00ffff', width=3)))

        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#ffffff'),
            title=dict(text='Gráfica de f(x) = x³', font=dict(size=20, color='#00ffff')),
            xaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff')
        )
        st.plotly_chart(fig)

    # Interactive section
    st.markdown("### **Prueba con tus propios datos**")
    coef = st.number_input("Ingresa el coeficiente para el exponente cúbico (default: 1):", value=1.0)

    y_user = coef * x**3
    fig_user = go.Figure()
    fig_user.add_trace(go.Scatter(x=x, y=y_user, mode='lines', name=f'f(x) = {coef}x³',
                                  line=dict(color='#ff00ff', width=3)))
    fig_user.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#ffffff'),
        title=dict(text=f'Gráfica de f(x) = {coef}x³', font=dict(size=20, color='#ff00ff')),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff')
    )
    st.plotly_chart(fig_user)

    # Conclusion with if
    st.markdown("### **Conclusión para tus parámetros**")
    if coef > 0:
        st.markdown(f"Con \( c = {coef} \), la función es convexa para \( x > 0 \) y no es convexa ni cóncava en \( x = 0 \).")
    elif coef == 0:
        st.markdown("Con \( c = 0 \), la función se convierte en una constante y no es ni convexa ni cóncava.")
    else:
        st.markdown(f"Con \( c = {coef} \), la función es cóncava para \( x < 0 \) y convexa para \( x > 0 \).")


def show_exercise_3():
    st.markdown('<h2 class="subheader">Demostrar que f(x) = e²ˣ es convexa en R</h2>', unsafe_allow_html=True)
    
    steps = {
        "Paso 1 - Primera Derivada": {"explanation": "Calculamos la primera derivada de f(x) = e²ˣ", "formula": "f'(x) = 2e²ˣ"},
        "Paso 2 - Segunda Derivada": {"explanation": "Calculamos la segunda derivada", "formula": "f''(x) = 4e²ˣ"},
        "Paso 3 - Análisis": {"explanation": "Como e²ˣ > 0 para todo x ∈ R, entonces f''(x) > 0 en todo el dominio."},
        "Conclusión": {"explanation": "La función es estrictamente convexa en R ya que f''(x) > 0 para todo x ∈ R."}
    }
    
    current_step = st.radio("Selecciona el paso a visualizar:", list(steps.keys()))
    
    with st.container():
        st.markdown(f'<div class="step-box">', unsafe_allow_html=True)
        st.markdown(f"### {current_step}")
        st.write(steps[current_step]["explanation"])
        if "formula" in steps[current_step]:
            st.markdown(f'<div class="formula">{steps[current_step]["formula"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Plot for current step
        x = np.linspace(-2, 2, 100)
        y = np.exp(2 * x)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='f(x) = e²ˣ', line=dict(color='#00ffff', width=3)))
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#ffffff'),
            title=dict(text='Gráfica de f(x) = e²ˣ', font=dict(size=20, color='#00ffff')),
            xaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff')
        )
        st.plotly_chart(fig)

    # Interactive section
    st.markdown("### **Prueba con tus propios datos**")
    coef = st.number_input("Ingresa el coeficiente del exponente (default: 2):", value=2.0)

    y_user = np.exp(coef * x)
    fig_user = go.Figure()
    fig_user.add_trace(go.Scatter(x=x, y=y_user, mode='lines', name=f'f(x) = e^{coef}ˣ', line=dict(color='#ff00ff', width=3)))
    fig_user.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#ffffff'),
        title=dict(text=f'Gráfica de f(x) = e^{coef}ˣ', font=dict(size=20, color='#ff00ff')),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff')
    )
    st.plotly_chart(fig_user)

    # Conclusion with if
    st.markdown("### **Conclusión para tus parámetros**")
    if coef > 0:
        st.markdown(f"Con el coeficiente \( c = {coef} \), la función sigue siendo estrictamente convexa, ya que la derivada segunda \( f''(x) = {coef**2}e^{{{coef}x}} \) es positiva en todo \( R \).")
    elif coef == 0:
        st.markdown(f"Con \( c = {coef} \), la función se convierte en una constante \( f(x) = 1 \), que no es ni convexa ni cóncava.")
    else:
        st.markdown(f"Con \( c = {coef} \), la función tiene un decrecimiento exponencial, pero sigue siendo convexa ya que \( f''(x) = {coef**2}e^{{{coef}x}} > 0 \).")


def show_exercise_4():
    st.markdown('<h2 class="subheader">Analizar f(x) = ln(x) en (0, ∞)</h2>', unsafe_allow_html=True)
    
    steps = {
        "Paso 1 - Primera Derivada": {"explanation": "Calculamos la primera derivada de f(x) = ln(x)", "formula": "f'(x) = 1/x"},
        "Paso 2 - Segunda Derivada": {"explanation": "Calculamos la segunda derivada", "formula": "f''(x) = -1/x²"},
        "Paso 3 - Análisis": {"explanation": "Como f''(x) < 0 para todo x > 0, la función es estrictamente cóncava en su dominio."},
        "Conclusión": {"explanation": "La función es cóncava en (0, ∞) ya que f''(x) < 0 en todo su dominio."}
    }
    
    current_step = st.radio("Selecciona el paso a visualizar:", list(steps.keys()))
    
    with st.container():
        st.markdown(f'<div class="step-box">', unsafe_allow_html=True)
        st.markdown(f"### {current_step}")
        st.write(steps[current_step]["explanation"])
        if "formula" in steps[current_step]:
            st.markdown(f'<div class="formula">{steps[current_step]["formula"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Plot for current step
        x = np.linspace(0.1, 5, 100)
        y = np.log(x)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='f(x) = ln(x)', line=dict(color='#00ffff', width=3)))
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#ffffff'),
            title=dict(text='Gráfica de f(x) = ln(x)', font=dict(size=20, color='#00ffff')),
            xaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff')
        )
        st.plotly_chart(fig)

    # Interactive section
    st.markdown("### **Prueba con tus propios datos**")
    shift = st.number_input("Ingresa un desplazamiento para x (default: 0):", value=0.0)

    if shift > -0.1:  # Evitar valores de log negativos
        y_user = np.log(x + shift)
        fig_user = go.Figure()
        fig_user.add_trace(go.Scatter(x=x, y=y_user, mode='lines', name=f'f(x) = ln(x + {shift})', line=dict(color='#ff00ff', width=3)))
        fig_user.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#ffffff'),
            title=dict(text=f'Gráfica de f(x) = ln(x + {shift})', font=dict(size=20, color='#ff00ff')),
            xaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff')
        )
        st.plotly_chart(fig_user)

    # Conclusion
    st.markdown("### **Conclusión para tus parámetros**")
    if shift > -0.1:
        st.markdown(f"Con el desplazamiento \( x + {shift} \), la función sigue siendo cóncava en su dominio mientras \( x + {shift} > 0 \).")

def show_exercise_5():
    st.markdown('<h2 class="subheader">Analizar f(x) = x⁴ - 2x² + 1</h2>', unsafe_allow_html=True)
    
    steps = {
        "Paso 1 - Primera Derivada": {"explanation": "Calculamos la primera derivada de f(x) = x⁴ - 2x² + 1", "formula": "f'(x) = 4x³ - 4x"},
        "Paso 2 - Segunda Derivada": {"explanation": "Calculamos la segunda derivada", "formula": "f''(x) = 12x² - 4"},
        "Paso 3 - Puntos Críticos": {"explanation": "Encontramos los puntos donde f''(x) = 0", "formula": "x = ±√(1/3) ≈ ±0.577"},
        "Conclusión": {"explanation": "La función es convexa en (-∞, -√(1/3)) ∪ (√(1/3), ∞) y cóncava en (-√(1/3), √(1/3))."}
    }
    
    # Seleccionar paso
    current_step = st.radio("Selecciona el paso a visualizar:", list(steps.keys()))
    
    with st.container():
        st.markdown(f"### {current_step}")
        st.write(steps[current_step]["explanation"])
        if "formula" in steps[current_step]:
            st.markdown(f'**Fórmula:** {steps[current_step]["formula"]}')
        
        # Graficar función original
        x = np.linspace(-2, 2, 500)
        y = x**4 - 2 * x**2 + 1
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='f(x) = x⁴ - 2x² + 1', line=dict(color='#00ffff', width=3)))
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#ffffff'),
            title=dict(text='Gráfica de f(x) = x⁴ - 2x² + 1', font=dict(size=20, color='#00ffff')),
            xaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff')
        )
        st.plotly_chart(fig)

    # Sección interactiva para modificar parámetros
    st.markdown("### **Prueba con tus propios datos**")
    coef_x2 = st.number_input("Ingresa el coeficiente de x² (default: -2):", value=-2.0)
    coef_const = st.number_input("Ingresa el término constante (default: 1):", value=1.0)

    # Recalcular y graficar con parámetros personalizados
    y_user = x**4 + coef_x2 * x**2 + coef_const
    fig_user = go.Figure()
    fig_user.add_trace(go.Scatter(x=x, y=y_user, mode='lines', name=f'f(x) = x⁴ + {coef_x2}x² + {coef_const}', line=dict(color='#ff00ff', width=3)))
    fig_user.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#ffffff'),
        title=dict(text=f'Gráfica de f(x) = x⁴ + {coef_x2}x² + {coef_const}', font=dict(size=20, color='#ff00ff')),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ffffff')
    )
    st.plotly_chart(fig_user)

    # Conclusión dinámica basada en los parámetros
    st.markdown("### **Conclusión para tus parámetros**")
    if coef_x2 > 0:
        st.markdown(f"Con un coeficiente de x² positivo ({coef_x2}), la función tiene un comportamiento más convexo.")
    elif coef_x2 < 0:
        st.markdown(f"Con un coeficiente de x² negativo ({coef_x2}), la función presenta intervalos de concavidad más marcados.")
    else:
        st.markdown("El término cuadrático no afecta la concavidad o convexidad de la función.")
    
    if coef_const > 0:
        st.markdown(f"El término constante positivo ({coef_const}) desplaza la función hacia arriba.")
    elif coef_const < 0:
        st.markdown(f"El término constante negativo ({coef_const}) desplaza la función hacia abajo.")
    else:
        st.markdown("El término constante no afecta la posición vertical de la función.")


if selected_exercise == "Ejercicio 1":
    show_exercise_1()
elif selected_exercise == "Ejercicio 2":
    show_exercise_2()
elif selected_exercise == "Ejercicio 3":
    show_exercise_3()
elif selected_exercise == "Ejercicio 4":
    show_exercise_4()
elif selected_exercise == "Ejercicio 5":
    show_exercise_5()