import matplotlib.pyplot as plt

gasto_marketing = [800, 1200, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]
vendas = [45, 65, 85, 100, 130, 155, 170, 190, 210, 230, 250, 270]


plt.scatter(gasto_marketing, vendas, color='orange')
plt.title('Gasto em Marketing vs. Número de Vendas')
plt.xlabel('Gasto em Marketing (R$)')
plt.ylabel('Número de Vendas')
plt.grid(True)
plt.show()
