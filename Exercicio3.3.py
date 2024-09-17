import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Dados
gasto_marketing = [800, 1200, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]
vendas = [45, 65, 85, 100, 130, 155, 170, 190, 210, 230, 250, 270]
gasto_marketing = np.array(gasto_marketing)
vendas = np.array(vendas)

# Regressão linear
slope, intercept, r_value, p_value, std_err = stats.linregress(gasto_marketing, vendas)

# Coefficients
β0 = intercept
β1 = slope
print(f'β0 (intercepto): {β0:.2f}')
print(f'β1 (slope): {β1:.2f}')

# Dados para a linha de regressão
linha_regressao = β0 + β1 * gasto_marketing

plt.scatter(gasto_marketing, vendas, color='orange', label='Dados Reais')
plt.plot(gasto_marketing, linha_regressao, color='blue', linestyle='--', label='Linha de Regressão')
plt.title('Gasto em Marketing vs. Número de Vendas com Linha de Regressão')
plt.xlabel('Gasto em Marketing (R$)')
plt.ylabel('Número de Vendas')
plt.legend()
plt.grid(True)
plt.show()
