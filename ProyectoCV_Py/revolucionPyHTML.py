import numpy as np
import plotly.graph_objects as go

# 1. Definir las constantes geométricas
a = 2  # Radio del cilindro (x = a)
h = 5  # Altura del cilindro (z = h)

# 2. Definir el dominio corregido de los parámetros
v = np.linspace(0, 2 * np.pi, 100) # Ángulo v de 0 a 2*pi
u = np.linspace(0, h, 50)          # Altura u de 0 a h
V, U = np.meshgrid(v, u)

# 3. Ecuaciones paramétricas del cilindro
X = a * np.cos(V)
Y = a * np.sin(V)
Z = U

# 4. Crear la superficie interactiva en 3D
fig = go.Figure(data=[go.Surface(
    x=X, y=Y, z=Z, 
    colorscale='Viridis', # Usamos una paleta distinta a la del cono
    colorbar=dict(title="Eje Z")
)])

# 5. Diseño estético y limpio para el reporte
fig.update_layout(
    title={
        'text': "Cilindro de Revolución (Integrante 2)",
        'y':0.95, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'
    },
    scene=dict(
        xaxis_title='Eje X',
        yaxis_title='Eje Y',
        zaxis_title='Eje Z',
        aspectmode='data' # Mantiene la proporción geométrica real
    ),
    margin=dict(l=0, r=0, b=0, t=50),
    template="plotly_white"
)

# 6. Exportar a HTML para GitHub Pages
fig.write_html("cilindro_revolucion.html")
print("¡Archivo 'cilindro_revolucion.html' generado exitosamente!")
