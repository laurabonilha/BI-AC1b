import matplotlib.pyplot as plt

# Dados
semanas = list(range(1, 13))
gasto_marketing = [800, 1200, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]

# Gráfico
plt.plot(semanas, gasto_marketing, marker='o', color='blue', linestyle='-', label='Gasto em Marketing')
plt.title('Gasto em Marketing ao Longo das Semanas')
plt.xlabel('Semana')
plt.ylabel('Gasto em Marketing (R$)')
plt.legend()
plt.grid(True)
plt.show()
