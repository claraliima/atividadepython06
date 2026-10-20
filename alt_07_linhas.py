"""ALTERNATIVA 07 - Séries temporais com pandas: pontos por loja + média móvel.

Diferença em relação à versão com seaborn:
  - Os dados viram uma série indexada por data (set_index) e usamos rolling()
    para suavizar. Cada data pertence a uma só loja, então ligar os pontos de
    cada loja gera zigue-zague; mostramos os pontos e uma média móvel de 7 dias
    do conjunto todo, que revela a tendência.
"""
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_linhas.csv", parse_dates=["data"])
df = df.set_index("data").sort_index()

media_movel = df["vendas"].rolling(window=7, min_periods=3).mean()

fig, ax = plt.subplots(figsize=(12, 6))
for loja, cor in [("Loja A", "#1c7ed6"), ("Loja B", "#f08c00")]:
    parte = df[df["loja"] == loja]
    ax.scatter(parte.index, parte["vendas"], s=22, alpha=0.65, color=cor, label=loja)

ax.plot(media_movel.index, media_movel, color="black", linewidth=2.5,
        label="Média móvel (7 dias)")

ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
ax.set_title("Vendas diárias por loja e tendência")
ax.set_ylabel("Vendas")
ax.legend(frameon=False)
ax.grid(alpha=0.3)

fig.tight_layout()
saida = RAIZ / "graficos" / "alt_07_linhas.png"
fig.savefig(saida, dpi=150)
print(f"Salvo em: {saida}")
