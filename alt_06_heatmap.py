"""ALTERNATIVA 06 - Mapa de calor com imshow (sem seaborn).

Diferença em relação à versão com seaborn:
  - sns.heatmap desenha e anota sozinho; aqui usamos ax.imshow() sobre a matriz
    e escrevemos cada número com ax.text(), escolhendo texto claro ou escuro
    conforme o fundo da célula para manter a legibilidade.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_heatmap.csv")

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
matriz = df.pivot(index="dia_semana", columns="horario",
                  values="movimento_clientes").reindex(dias)

fig, ax = plt.subplots(figsize=(11, 7))
img = ax.imshow(matriz.to_numpy(), cmap="viridis", aspect="auto")

ax.set_xticks(range(matriz.shape[1]), matriz.columns)
ax.set_yticks(range(matriz.shape[0]), matriz.index)

limite = matriz.to_numpy().max() / 2
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        valor = matriz.iat[i, j]
        ax.text(j, i, valor, ha="center", va="center",
                color="white" if valor < limite else "black", fontsize=11)

fig.colorbar(img, ax=ax, label="Clientes")
ax.set_title("Movimento de clientes por dia e horário")
ax.set_xlabel("Horário")

fig.tight_layout()
saida = RAIZ / "graficos" / "alt_06_heatmap.png"
fig.savefig(saida, dpi=150)
print(f"Salvo em: {saida}")
