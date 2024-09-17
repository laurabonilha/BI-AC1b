import matplotlib.pyplot as plt
vendas = [45, 65, 85, 100, 130, 155, 170, 190, 210, 230, 250, 270]
visitas_site = [700, 950, 1100, 1400, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100]

plt.scatter(visitas_site, vendas, color='cyan')
plt.title('Visitas ao Site vs. Número de Vendas')
plt.xlabel('Visitas ao Site')
plt.ylabel('Número de Vendas')
plt.grid(True)
plt.show()
