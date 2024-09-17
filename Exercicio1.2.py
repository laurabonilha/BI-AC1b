import matplotlib.pyplot as plt

# Dados
semanas = list(range(1, 13))
visitas_site = [700, 950, 1100, 1400, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100]

# Gráfico
plt.plot(semanas, visitas_site, marker='o', color='green', linestyle='-', label='Visitas ao Site')
plt.title('Visitas ao Site ao Longo das Semanas')
plt.xlabel('Semana')
plt.ylabel('Visitas ao Site')
plt.legend()
plt.grid(True)
plt.show()
