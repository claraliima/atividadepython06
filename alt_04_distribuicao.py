"""ALTERNATIVA 04 - Histograma normalizado + KDE calculada manualmente.

Diferença em relação à versão com seaborn:
  - sns.histplot(kde=True) faz tudo sozinho; aqui o histograma usa density=True
    (área = 1) e a curva vem de scipy.stats.gaussian_kde, desenhada à parte.
  - O número de classes segue a regra de Sturges em vez de um valor fixo.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import gaussian_kde

RAIZ = Path(__file__).resolve().parent.parent
idades = pd.read_csv(RAIZ / "dados" / "dados_distribuicao.csv")["idade"].to_numpy()

n_classes = int(np.ceil(np.log2(len(idades)) + 1))      # regra de Sturges

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(idades, bins=n_classes, density=True, color="#74c0fc", edgecolor="white")

xs = np.linspace(idades.min() - 5, idades.max() + 5, 300)
ax.plot(xs, gaussian_kde(idades)(xs), color="#1864ab", linewidth=2.5, label="Densidade (KDE)")

ax.axvline(idades.mean(), color="red", linestyle="--", label=f"Média = {idades.mean():.1f}")
ax.axvline(np.median(idades), color="green", linestyle=":", linewidth=2,
           label=f"Mediana = {np.median(idades):.0f}")

ax.set_title(f"Distribuição da idade dos clientes (n = {len(idades)})")
ax.set_xlabel("Idade (anos)")
ax.set_ylabel("Densidade")
ax.legend(frameon=False)

fig.tight_layout()
saida = RAIZ / "graficos" / "alt_04_distribuicao.png"
fig.savefig(saida, dpi=150)
print(f"Salvo em: {saida}")
