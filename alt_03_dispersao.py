"""ALTERNATIVA 03 - Dispersão com laço por grupo + linha de tendência de cada grupo.

Diferença em relação à versão com seaborn:
  - Em vez de hue=, percorremos os grupos com groupby() e chamamos ax.scatter()
    uma vez por grupo (controle total sobre cor, marcador e rótulo).
  - Acrescenta uma reta de tendência por sexo, ajustada com numpy.polyfit.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_dispersao.csv")

estilo = {"Feminino": ("#c2255c", "o"), "Masculino": ("#1864ab", "s")}

fig, ax = plt.subplots(figsize=(10, 7))

for sexo, grupo in df.groupby("sexo"):
    cor, marcador = estilo[sexo]
    ax.scatter(grupo["altura_cm"], grupo["peso_kg"], color=cor, marker=marcador,
               alpha=0.6, s=45, label=sexo)

    # Ajuste de reta (grau 1): peso = a * altura + b
    a, b = np.polyfit(grupo["altura_cm"], grupo["peso_kg"], deg=1)
    xs = np.linspace(grupo["altura_cm"].min(), grupo["altura_cm"].max(), 50)
    ax.plot(xs, a * xs + b, color=cor, linewidth=2)

ax.set_title("Altura × peso, com tendência por sexo")
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (kg)")
ax.legend(title="Sexo")
ax.grid(alpha=0.3)

fig.tight_layout()
saida = RAIZ / "graficos" / "alt_03_dispersao.png"
fig.savefig(saida, dpi=150)
print(f"Salvo em: {saida}")
