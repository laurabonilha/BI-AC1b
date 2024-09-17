import matplotlib.pyplot as plt

# Dados
visitas_site = [700, 950, 1100, 1400, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100]
gasto_marketing = [800, 1200, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]

plt.scatter(gasto_marketing, visitas_site, color='purple')
plt.title('Gasto em Marketing vs. Visitas ao Site')
plt.xlabel('Gasto em Marketing (R$)')
plt.ylabel('Visitas ao Site')
plt.grid(True)
plt.show()
