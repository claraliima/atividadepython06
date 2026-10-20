"""ALTERNATIVA 01 - Barras agrupadas com matplotlib puro.

Diferença em relação à versão com seaborn:
  - seaborn.barplot agrupa sozinho; aqui calculamos as posições das barras
    com numpy (centro do grupo + deslocamento de cada série).
  - Os dados são reorganizados com pivot() para uma tabela categoria x região.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_barras.csv")

# Tabela larga: uma linha por categoria, uma coluna por região
tabela = df.pivot(index="categoria", columns="regiao", values="vendas_medias")
tabela = tabela[["Norte", "Sul", "Leste", "Oeste"]]

n_grupos, n_series = tabela.shape
largura = 0.8 / n_series                       # 0.8 = espaço total de cada grupo
x = np.arange(n_grupos)                        # posição central de cada categoria

fig, ax = plt.subplots(figsize=(12, 6))
cores = plt.cm.tab10.colors

for i, regiao in enumerate(tabela.columns):
    deslocamento = (i - (n_series - 1) / 2) * largura   # centraliza o grupo em x
    barras = ax.bar(x + deslocamento, tabela[regiao], width=largura,
                    label=regiao, color=cores[i])
    ax.bar_label(barras, fmt="%.0f", fontsize=9, padding=2)

ax.set_xticks(x, tabela.index)
ax.set_title("Vendas médias por categoria e região")
ax.set_ylabel("Vendas médias")
ax.legend(title="Região", ncol=4, loc="upper center",
          bbox_to_anchor=(0.5, -0.08), frameon=False)
ax.grid(axis="y", alpha=0.3)
ax.set_axisbelow(True)

fig.tight_layout()
saida = RAIZ / "graficos" / "alt_01_barras.png"
fig.savefig(saida, dpi=150)
print(f"Salvo em: {saida}")
