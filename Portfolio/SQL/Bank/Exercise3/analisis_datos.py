import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

estudiantes = {
    "ID": [1, 2, 3, 4],
    "Nombre": ["Manuel", "Tania", "Pedro", "Ana"]
}
df_estudiantes = pd.DataFrame(estudiantes)

amigos = {
    "ID": [1, 2, 3, 4],
    "Amigo_ID": [2, 3, 4, 1]
}
df_amigos = pd.DataFrame(amigos)

salario = {
    "ID": [1, 2, 3, 4],
    "Salario": [15200.1, 10060.2, 11500.5, 12120.0]
}
df_salario = pd.DataFrame(salario)

df = pd.merge(df_estudiantes, df_salario, on="ID")

df = pd.merge(df, df_amigos, on="ID")

df = pd.merge(df, df_salario, left_on="Amigo_ID", right_on="ID", suffixes=("", "_Amigo"))

hist_salario = df_salario['Salario'].plot(kind='hist', title='Distribución de Salarios')
fig = plt.gcf()
#save_plot(fig,filename="distribucion_salarios.png", dpi=300, show=False)

media_salario = df["Salario"].mean()
mediana_salario = df["Salario"].median()
desv_est_salario = df["Salario"].std()

estadisticas = {
    "Métrica": ["Media", "Mediana", "Desviación Estándar"],
    "Salario": [media_salario, mediana_salario, desv_est_salario]
}
df_estadisticas = pd.DataFrame(estadisticas)

print(df_estadisticas)

correlacion = df[['Salario', 'Salario_Amigo']].corr()
print("Correlación entre salarios de estudiantes y amigos:\n", correlacion)

fig, ax = plt.subplots()
ax.scatter(df['Salario'], df['Salario_Amigo'])
ax.set_title('Relación entre salario del estudiante y salario del amigo')
ax.set_xlabel('Salario del Estudiante')
ax.set_ylabel('Salario del Amigo')

#save_plot(fig, filename="Relación salarios amigos.png", dpi=300, show=False)
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='Salario', y='Salario_Amigo', data=df, ax=ax)
sns.regplot(x='Salario', y='Salario_Amigo', data=df, ax=ax, scatter=False, color='red')
ax.set_title('Relación entre salario del estudiante y salario del Amigo')
ax.set_xlabel('Salario del estudiante')
ax.set_ylabel('Salario del amigo')

#save_plot(fig, filename="Relación_salario_estudiante_salario_amigo.png", dpi=300, show=False)
cmap = sns.color_palette("Blues", as_cmap= True)
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df[['Salario', 'Salario_Amigo']].corr(), annot=True, cmap=cmap, ax=ax)
ax.set_title('Heatmap de correlación entre salarios')
#save_plot(fig, filename="heatmap_correlacion_salarios.png", dpi=300, show=False)
