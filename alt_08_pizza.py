"""ALTERNATIVA 08 - Gráfico de rosca (donut) com rótulos externos.

Diferença em relação à versão anterior:
  - Pizza com 'width' nas cunhas vira uma rosca, que deixa espaço para o total no centro.
  - Rótulos fora da figura, com nome, valor e percentual calculados à mão.
  - A maior fatia ganha 'explode' para destaque.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_pizza.csv").sort_values("faturamento", ascending=False)

valores = df["faturamento"]
total = valores.sum()
rotulos = [f"{c}\nR$ {v:,.0f} ({v / total:.1%})".replace(",", ".")
           for c, v in zip(df["canal_venda"], valores)]
explode = [0.05] + [0] * (len(df) - 1)

fig, ax = plt.subplots(figsize=(9, 8))
ax.pie(valores, labels=rotulos, explode=explode, startangle=90, counterclock=False,
       colors=plt.cm.Paired.colors, wedgeprops={"width": 0.45, "edgecolor": "white"},
       labeldistance=1.12, textprops={"fontsize": 11})

ax.text(0, 0, f"Total\nR$ {total:,.0f}".replace(",", "."), ha="center", va="center",
        fontsize=15, fontweight="bold")
ax.set_title("Faturamento por canal de venda")

fig.tight_layout()
saida = RAIZ / "graficos" / "alt_08_pizza.png"
fig.savefig(saida, dpi=150, bbox_inches="tight")
print(f"Salvo em: {saida}")
