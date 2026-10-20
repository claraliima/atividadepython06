"""ALTERNATIVA 05 - Frequência usando a API de plot do próprio pandas.

Diferença em relação à versão anterior:
  - value_counts().plot.bar() desenha direto da Series (pandas chama o matplotlib).
  - Barras na vertical e com ordem alfabética invertida por contagem,
    mais uma linha de frequência acumulada (diagrama de Pareto) no eixo secundário.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_frequencia.csv")

contagem = df["tipo_atendimento"].value_counts()
acumulado = contagem.cumsum() / contagem.sum() * 100

fig, ax = plt.subplots(figsize=(10, 6))
contagem.plot.bar(ax=ax, color="#5c7cfa", rot=0, width=0.7)
ax.bar_label(ax.containers[0], padding=3)
ax.set_ylabel("Número de chamados")
ax.set_xlabel("")

ax2 = ax.twinx()                                   # segundo eixo Y (0 a 100%)
ax2.plot(range(len(acumulado)), acumulado.values, color="#e8590c", marker="o")
ax2.set_ylim(0, 105)
ax2.set_ylabel("Frequência acumulada (%)")

ax.set_title("Pareto: chamados por tipo de atendimento")

fig.tight_layout()
saida = RAIZ / "graficos" / "alt_05_frequencia.png"
fig.savefig(saida, dpi=150)
print(f"Salvo em: {saida}")
