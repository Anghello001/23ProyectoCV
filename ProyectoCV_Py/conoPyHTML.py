import numpy as np
import plotly.graph_objects as go

# 1. Definir el dominio de los parámetros del Cono
u = np.linspace(0, 3, 100) # Radio u de 0 a 3
v = np.linspace(0, 2 * np.pi, 100) # Ángulo v de 0 a 2*pi
U, V = np.meshgrid(u, v)

# 2. Ecuaciones paramétricas r(u,v)
X = U * np.cos(V)
Y = U * np.sin(V)
Z = 2 * U

# 3. Crear la superficie interactiva en 3D
fig = go.Figure(data=[go.Surface(
    x=X, y=Y, z=Z, 
    colorscale='Plasma', # Usamos 'Plasma' para diferenciarlo del ejemplo 1
    colorbar=dict(title="Eje Z")
)])

# 4. Diseño estético para el reporte
fig.update_layout(
    title={
        'text': "Cono Recto de Revolución (Integrante 3)",
        'y':0.95, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'
    },
    scene=dict(
        xaxis_title='Eje X',
        yaxis_title='Eje Y',
        zaxis_title='Eje Z',
        aspectmode='data' # Mantiene la proporción real de los ejes
    ),
    margin=dict(l=0, r=0, b=0, t=50),
    template="plotly_white"
)

# Exportar a HTML
fig.write_html("cono_revolucion.html")
print("¡Archivo 'cono_revolucion.html' generado exitosamente!")
