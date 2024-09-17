import matplotlib.pyplot as plt

# Dados
semanas = list(range(1, 13))
vendas = [45, 65, 85, 100, 130, 155, 170, 190, 210, 230, 250, 270]

# Gráfico
plt.plot(semanas, vendas, marker='o', color='red', linestyle='-', label='Número de Vendas')
plt.title('Número de Vendas ao Longo das Semanas')
plt.xlabel('Semana')
plt.ylabel('Número de Vendas')
plt.legend()
plt.grid(True)
plt.show()
