"""ALTERNATIVA 02 - Boxplot com matplotlib puro + pontos individuais (jitter).

Diferença em relação à versão com seaborn:
  - ax.boxplot() recebe uma LISTA de arrays (um por departamento).
  - Os pontos reais são sobrepostos com um pequeno ruído horizontal (jitter),
    para mostrar a densidade dos dados e não só o resumo estatístico.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_boxplot.csv")

grupos = {nome: g["salario"].to_numpy() for nome, g in df.groupby("departamento")}
nomes = list(grupos)

rng = np.random.default_rng(42)                # semente fixa = resultado reprodutível
fig, ax = plt.subplots(figsize=(10, 6.5))

bp = ax.boxplot(grupos.values(), tick_labels=nomes, patch_artist=True, widths=0.5,
                showfliers=False, medianprops={"color": "black", "linewidth": 2})
for caixa, cor in zip(bp["boxes"], plt.cm.Pastel1.colors):
    caixa.set_facecolor(cor)

for i, valores in enumerate(grupos.values(), start=1):
    ruido = rng.normal(i, 0.06, size=len(valores))
    ax.scatter(ruido, valores, s=14, alpha=0.5, color="#333333", zorder=3)
    ax.scatter(i, valores.mean(), marker="D", color="red", s=60, zorder=4,
               label="Média" if i == 1 else None)

ax.set_title("Distribuição salarial por departamento")
ax.set_ylabel("Salário mensal")
ax.yaxis.set_major_formatter(lambda v, _: f"R$ {v:,.0f}".replace(",", "."))
ax.legend(frameon=False)
ax.grid(axis="y", alpha=0.3)

fig.tight_layout()
saida = RAIZ / "graficos" / "alt_02_boxplot.png"
fig.savefig(saida, dpi=150)
print(f"Salvo em: {saida}")
