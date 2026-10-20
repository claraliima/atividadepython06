"""ALTERNATIVA 09 - Regressão com numpy.polyfit e análise de resíduos.

Diferença em relação à versão com scipy/seaborn:
  - O ajuste é feito com numpy.polyfit e o R² é calculado "na mão"
    (1 - SQ_resíduos / SQ_total), o que ajuda a entender o que ele significa.
  - Um segundo gráfico mostra os resíduos: se não houver padrão, o modelo
    linear é adequado.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_regressao.csv")

x = df["renda_mensal"].to_numpy()
y = df["gasto_mensal"].to_numpy()

a, b = np.polyfit(x, y, deg=1)                 # y = a*x + b
previsto = a * x + b
residuos = y - previsto
r2 = 1 - np.sum(residuos ** 2) / np.sum((y - y.mean()) ** 2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={"width_ratios": [2, 1]})

ax1.scatter(x, y, alpha=0.6, color="#4263eb")
xs = np.linspace(x.min(), x.max(), 100)
ax1.plot(xs, a * xs + b, color="crimson", linewidth=2,
         label=f"y = {a:.3f}x + {b:.0f}  (R² = {r2:.3f})")
ax1.set_title("Gasto × renda")
ax1.set_xlabel("Renda mensal")
ax1.set_ylabel("Gasto mensal")
ax1.legend(frameon=False)

ax2.scatter(previsto, residuos, alpha=0.6, color="#868e96")
ax2.axhline(0, color="crimson")
ax2.set_title("Resíduos")
ax2.set_xlabel("Gasto previsto")
ax2.set_ylabel("Erro (real − previsto)")

for ax in (ax1, ax2):
    ax.grid(alpha=0.3)

fig.tight_layout()
saida = RAIZ / "graficos" / "alt_09_regressao.png"
fig.savefig(saida, dpi=150)
print(f"Salvo em: {saida}")
